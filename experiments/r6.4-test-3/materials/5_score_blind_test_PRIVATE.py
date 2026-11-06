#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SILEX r6.4 blind test: PRIVATE SCORER for the reading booklet (form RB-1) and the writing booklet (form WB-1).

*** PRIVATE. This file holds the answer key and the writing rubric. Do not upload it to GitHub, do not paste it
*** (or any report made with --key or --verbose) into a chat with a model that is to be tested.

What it does
  Reading sheets (forms R+ and R-): reads the final block "Q7: B | 80" of a model's reply and gives the strict score
  (exact answers), the partial score, the three anchors, the score without anchors ("core"), the score per part,
  the calibration of the confidence numbers, and how often the model fell for the designer's expected wrong answer.
  Writing sheets (form W+): takes the fenced block under each heading W1..W8, runs the lines through the r6.4 checker
  (file silex_check_r6.4.py, Python 3, standard library only) and marks them against the rubric (68 points).
  Open question Z1 is marked by hand; --z1-export writes the accounts, shuffled and without model names.

How to run
  python3 5_score_blind_test_PRIVATE.py --selftest --checker PATH/silex_check_r6.4.py
  python3 5_score_blind_test_PRIVATE.py --checker PATH/silex_check_r6.4.py Claude_Rminus.txt Claude_Rplus.txt Claude_Wplus.txt ...
  A file name is  <Model>_<Form>.txt  with Form = Rplus, Rminus or Wplus (a run number may follow: Claude_Rminus_2.txt).
  Any other file name:  Model:Form=path   for example   "Claude:R-=my reply.txt"   or   Grok:W+#2=grok2.txt

Options
  --checker PATH     the r6.4 checker (SHA-256 below). Found by itself if it is next to this file, in ./tools or ../tools.
  --verbose          item by item, with the key
  --key              print the key (reading answers and the reference answers of the writing tasks), then stop
  --json FILE        everything, as JSON
  --csv FILE         one row per sheet
  --z1-export PREFIX write PREFIX_marking.md (accounts of Z1, shuffled) and PREFIX_codes.json (code -> sheet)
  --seed N           seed of the shuffle (default 1)
  --selftest         run the scorer on the key itself (perfect reading sheet, designer picks, reference writing answers)

Python 3.8 or later. No other package.
"""
import sys, os, re, json, csv, math, random, hashlib, argparse, importlib.util

SCORER_VERSION = 'RB-1 / WB-1, scorer 1.1'
GRAMMAR_SHA256 = '4cb2db0f2f43e09f3000b7416c17bcafec41d8e60a96f5f95aec09a7f798d799'
CHECKER_SHA256 = '6e8d6c3c8cfa996b215b358b2e40012217a1d032beefdc904f9d3b93f3193193'
READING_BODY = 'edcec880d947'          # first 12 hex digits of the SHA-256 of the body shared by booklets R+ and R-
WRITING_BODY = '31742d8d1766'          # the same for booklet W+

# ------------------------------------------------------------------------------------------------------------------------
# THE KEY
# ------------------------------------------------------------------------------------------------------------------------
KEY = {'reading': [{'id': 'Q1',
              'part': 'A',
              'kind': 'mc',
              'answer': 'D',
              'anchor': True,
              'meta': {'sec': ['3.8'], 'trap': 'none: English reading is enough', 'est': 'high', 'chance': 0.2}},
             {'id': 'Q2',
              'part': 'A',
              'kind': 'mc',
              'answer': 'B',
              'anchor': True,
              'meta': {'sec': ['3.2'], 'trap': 'none: English reading is enough', 'est': 'high', 'chance': 0.2}},
             {'id': 'Q3',
              'part': 'A',
              'kind': 'mc',
              'answer': 'C',
              'anchor': True,
              'meta': {'sec': ['2.2'], 'trap': 'none: header is readable from its shape', 'est': 'high', 'chance': 0.2}},
             {'id': 'Q4',
              'part': 'B',
              'kind': 'mc',
              'answer': 'E',
              'anchor': False,
              'meta': {'sec': ['1.6', '3.9'],
                       'trap': 'at(stretch,X) means throughout; during means at some time within',
                       'est': 'medium',
                       'chance': 0.2}},
             {'id': 'Q5',
              'part': 'B',
              'kind': 'mc',
              'answer': 'D',
              'anchor': False,
              'meta': {'sec': ['2.5', '3.8'],
                       'trap': 'rej of a message declines every request and proposal in it; it never denies a claim',
                       'est': 'low',
                       'chance': 0.2}},
             {'id': 'Q6',
              'part': 'B',
              'kind': 'mc',
              'answer': 'C',
              'anchor': False,
              'meta': {'sec': ['2.5', '1.5.5'],
                       'trap': 'ans answers only a question line; a request is answered with will or rej',
                       'est': 'low',
                       'chance': 0.2}},
             {'id': 'Q7',
              'part': 'B',
              'kind': 'mc',
              'answer': 'D',
              'anchor': False,
              'meta': {'sec': ['1.5.4', '3.8'], 'trap': 'a label belongs to the message that defines it', 'est': 'low', 'chance': 0.2}},
             {'id': 'Q8',
              'part': 'B',
              'kind': 'mc',
              'answer': 'B',
              'anchor': False,
              'meta': {'sec': ['2.4', '3.12'],
                       'trap': 'to marks a line as for someone; every receiver still gets the whole message; not secrecy',
                       'est': 'medium',
                       'chance': 0.2}},
             {'id': 'Q9',
              'part': 'B',
              'kind': 'mc',
              'answer': 'A',
              'anchor': False,
              'meta': {'sec': ['2.4', '1.7'], 'trap': 'You is tested once for every receiver', 'est': 'medium', 'chance': 0.2}},
             {'id': 'Q10',
              'part': 'B',
              'kind': 'mc',
              'answer': 'B',
              'anchor': False,
              'meta': {'sec': ['1.8', '3.9'], 'trap': 'a claim used as a time gives the time and is not asserted', 'est': 'medium', 'chance': 0.2}},
             {'id': 'Q11',
              'part': 'B',
              'kind': 'mc',
              'answer': 'E',
              'anchor': False,
              'meta': {'sec': ['2.5', '3.7'], 'trap': 'a plan is a plan, not an agreement and not a proposal', 'est': 'medium', 'chance': 0.2}},
             {'id': 'Q12',
              'part': 'B',
              'kind': 'mc',
              'answer': 'A',
              'anchor': False,
              'meta': {'sec': ['1.5.2', '3.2'],
                       'trap': 'crit binds a variable only inside its claim; nested quantifier order',
                       'est': 'medium',
                       'chance': 0.2}},
             {'id': 'Q13',
              'part': 'C',
              'kind': 'set',
              'answer': ['c', 'e', 'g'],
              'anchor': False,
              'meta': {'sec': ['1.8', '3.10'],
                       'trap': 'know and cause assert their claims; bel say hyp prob supp do not',
                       'est': 'medium',
                       'chance': 0.00392156862745098}},
             {'id': 'Q14',
              'part': 'C',
              'kind': 'set',
              'answer': ['d'],
              'anchor': False,
              'meta': {'sec': ['1.4.6', '1.8', '3.10', '4.13'],
                       'trap': 'ent asserts none of its claims; only the bare formula is asserted',
                       'est': 'low',
                       'chance': 0.03225806451612903}},
             {'id': 'Q15',
              'part': 'C',
              'kind': 'set',
              'answer': ['c', 'e'],
              'anchor': False,
              'meta': {'sec': ['2.5', '1.8', '3.10'],
                       'trap': 'the reason of rej and the claim of err are asserted; the claim of clr is not',
                       'est': 'low',
                       'chance': 0.015873015873015872}},
             {'id': 'Q16',
              'part': 'D',
              'kind': 'mc',
              'answer': 'C',
              'anchor': False,
              'meta': {'sec': ['1.1', '1.5.5'],
                       'trap': 'the header is not a line; blank and comment lines do not count',
                       'est': 'medium',
                       'chance': 0.2}},
             {'id': 'Q17',
              'part': 'D',
              'kind': 'list',
              'answer': ['Ana1.2', 'error', 'error', 'error', 'Cy1.2'],
              'anchor': False,
              'meta': {'sec': ['1.5.5'],
                       'trap': 'the short form needs a re that names exactly one whole message; saw does not count',
                       'est': 'low',
                       'chance': 0.01}},
             {'id': 'Q18',
              'part': 'D',
              'kind': 'set',
              'answer': ['c', 'd', 'e'],
              'anchor': False,
              'meta': {'sec': ['2.2', '2.3'],
                       'trap': 'saw names the latest message read from an agent and includes the earlier ones; it is not a reply',
                       'est': 'medium',
                       'chance': 0.03225806451612903}},
             {'id': 'Q19',
              'part': 'E',
              'kind': 'verdict',
              'answer': ['E-QUOTE', 'ok', 'E-QUOTE', 'ok', 'E-NAME', 'ok', 'E-QUOTE', 'E-QUOTE'],
              'anchor': False,
              'meta': {'sec': ['1.4.5', '1.9'],
                       'trap': 'the, tomorrow, my and a stray brace are E-QUOTE; an undefined label is E-NAME; other is a different word from the',
                       'est': 'low',
                       'chance': 2.3256803936137784e-09}},
             {'id': 'Q20',
              'part': 'E',
              'kind': 'verdict',
              'answer': ['E-ARITY', 'E-LEX', 'E-KIND', 'E-REDEF', 'E-SYN', 'E-KIND', 'ok'],
              'anchor': False,
              'meta': {'sec': ['3.8', '1.2', '3.1', '1.5.1', '1.8'],
                       'trap': 'will has one place; promise is no root; not takes no line; a value is not a line',
                       'est': 'low',
                       'chance': 2.790816472336534e-08}},
             {'id': 'Q21',
              'part': 'E',
              'kind': 'verdict',
              'answer': ['ok', 'E-KIND', 'E-TIME', 'ok', 'E-KIND', 'ok', 'E-TIME'],
              'anchor': False,
              'meta': {'sec': ['1.6', '3.9'],
                       'trap': 'compact date-time is a time; 20261112 is a number; impossible dates are E-TIME',
                       'est': 'low',
                       'chance': 2.790816472336534e-08}},
             {'id': 'Q22',
              'part': 'E',
              'kind': 'verdict',
              'answer': ['E-CODE', 'ok', 'E-CODE', 'E-MATH', 'E-KIND', 'ok', 'E-MATH', 'E-KIND'],
              'anchor': False,
              'meta': {'sec': ['1.4.6', '3.6'],
                       'trap': 'closed list of program languages; Python must parse; raw text in code may hold the; words and/or are not joins; a '
                               'number or an act alone is no line',
                       'est': 'low',
                       'chance': 2.3256803936137784e-09}},
             {'id': 'Q23',
              'part': 'E',
              'kind': 'verdict',
              'answer': ['ok', 'E-KIND', 'E-HEAD', 'E-HEAD', 'ok', 'E-KIND'],
              'anchor': False,
              'meta': {'sec': ['1.5.5', '2.2', '2.4'],
                       'trap': 'short numbers only in six roots; ack and retr have no short form; re is a header word; to names a receiver',
                       'est': 'low',
                       'chance': 3.3489797668038406e-07}},
             {'id': 'Q24',
              'part': 'E',
              'kind': 'verdict',
              'answer': ['E-HEAD', 'ok', 'E-HEAD', 'E-HEAD', 'E-HEAD', 'ok', 'E-LEX'],
              'anchor': False,
              'meta': {'sec': ['2.2', '1.2'],
                       'trap': 'no name twice; All stands alone; the sender is not Me; a message cannot answer itself; pri takes hi mid lo',
                       'est': 'low',
                       'chance': 2.790816472336534e-08}},
             {'id': 'Q25',
              'part': 'F',
              'kind': 'set',
              'answer': ['c', 'e', 'f', 'g', 'h'],
              'anchor': False,
              'meta': {'sec': ['2.1', '2.3'],
                       'trap': 'send times give no order; a line that points at a message with agree puts it before; saw covers earlier messages of '
                               'that agent; chains',
                       'est': 'low',
                       'chance': 0.00392156862745098}},
             {'id': 'Q26',
              'part': 'F',
              'kind': 'set',
              'answer': ['a', 'b', 'd', 'e'],
              'anchor': False,
              'meta': {'sec': ['2.3'],
                       'trap': 'same-sender order, saw, pointing line and chains; Milo1 is not reached',
                       'est': 'low',
                       'chance': 0.03225806451612903}},
             {'id': 'Q27',
              'part': 'F',
              'kind': 'set',
              'answer': ['b'],
              'anchor': False,
              'meta': {'sec': ['2.5', '2.6', '1.5.5'],
                       'trap': 'adopted when every receiver it was sent to has agreed; a to line has its own receivers; silence is not agreement',
                       'est': 'low',
                       'chance': 0.14285714285714285}},
             {'id': 'Q28',
              'part': 'F',
              'kind': 'list',
              'answer': ['rest', 'force', 'force'],
              'anchor': False,
              'meta': {'sec': ['2.3', '2.6'],
                       'trap': 'a retraction has force only for messages that follow it; send times do not count',
                       'est': 'low',
                       'chance': 0.125}},
             {'id': 'Q29',
              'part': 'F',
              'kind': 'mc',
              'answer': 'A',
              'anchor': False,
              'meta': {'sec': ['1.1', '1.5.5', '6.5'],
                       'trap': 'counting the header as line 1 makes every reference one too high, and it still passes when that line exists',
                       'est': 'medium',
                       'chance': 0.2}},
             {'id': 'Q30',
              'part': 'F',
              'kind': 'set',
              'answer': ['b', 'd'],
              'anchor': False,
              'meta': {'sec': ['2.4', '1.7'],
                       'trap': 'joining gives nothing written before; only messages that name the agent (or All) are received',
                       'est': 'medium',
                       'chance': 0.06666666666666667}},
             {'id': 'Q31',
              'part': 'F',
              'kind': 'set',
              'answer': ['a', 'b', 'd'],
              'anchor': False,
              'meta': {'sec': ['1.7', '2.6'],
                       'trap': 'All means every agent on the roster at that time except the sender',
                       'est': 'medium',
                       'chance': 0.06666666666666667}},
             {'id': 'Q32',
              'part': 'G',
              'kind': 'set',
              'answer': ['c', 'd', 'f', 'h'],
              'anchor': False,
              'meta': {'sec': ['1.4.6', '3.3'],
                       'trap': '^ groups to the right; -x^2 is -(x^2); log(x,b) is the logarithm of x to base b; & binds before | and => binds '
                               'after; prod and int argument order',
                       'est': 'low',
                       'chance': 0.00392156862745098}},
             {'id': 'Z1',
              'part': 'Z',
              'kind': 'free',
              'answer': None,
              'anchor': False,
              'meta': {'sec': ['1.5.5', '2.2', '2.4', '2.5', '1.8', '3.9', '3.7'],
                       'trap': 'a dozen conventions in one message',
                       'est': 'low',
                       'chance': None}}],
 'writing': [{'id': 'W1',
              'title': 'A reply to two messages',
              'context': ['msg(Kai,Lena,Milo,1)\npls(Milo,"drain tank three")\nis("pump","leaking")\nsug(at(2026-11-12,"replace pump"))',
                          'msg(Lena,Kai,Milo,1)\nis("gauge","stuck")\nis("tank three","empty")\nyn(is("valve","open"))'],
              'rubric': [['w1.hdr', 1, 'Header: sender Milo, receivers Kai and Lena, serial 1, and it names Kai1 and Lena1 in re or saw.'],
                         ['w1.agree', 1, 'agree(Kai1.3): the proposal line, in full (re names two messages, so no short number).'],
                         ['w1.rej', 1, 'rej(Kai1.1, ...): the request line, not the whole message (rej of Kai1 would decline the proposal too).'],
                         ['w1.why',
                          1,
                          'The reason of rej is asserted and says Milo is not permitted to open valve six: not(may(Me,"open valve six")) or '
                          'must(Me,not(...)).'],
                         ['w1.err', 1, "err(Lena1.2, ...): points at Lena's claim about tank three."],
                         ['w1.full',
                          1,
                          'What is so is stated: an asserted claim that tank three is full (the second place of err, or a claim line).'],
                         ['w1.ans', 1, 'ans(Lena1.3, yes): answers the question line.'],
                         ['w1.clean',
                          1,
                          'No pointing line (agree rej err ans clr retr unk) aimed at any line other than Kai1.3, Kai1.1, Lena1.2, Lena1.3.']],
              'loose': False,
              'reference': 'msg(Milo,Kai,Lena,1,re(Kai1,Lena1))\n'
                           'agree(Kai1.3)\n'
                           'rej(Kai1.1,not(may(Me,"open valve six")))\n'
                           'err(Lena1.2,is("tank three","full"))\n'
                           'ans(Lena1.3,yes)',
              'traps': 're names two messages: every reference must be written in full. The header is not a line. rej names the request line; rej of '
                       'the whole message would also decline the proposal. The reason of rej is asserted and is not(may(...)). ans answers a '
                       'question line.'},
             {'id': 'W2',
              'title': 'Asserting and only mentioning',
              'context': [],
              'rubric': [['w2.hdr', 1, 'Header: sender Pia, receivers Quin and Rae, serial 1.'],
                         ['w2.bel', 1, 'bel(Me or Pia, ...) about the cache being stale, and no plain claim line says it.'],
                         ['w2.say', 1, 'say(Rae, ...) about the backup being finished, and no plain claim line says it.'],
                         ['w2.fact', 1, 'A plain claim line (not inside bel, say, hyp, assume, if, ...) that the disk is full.'],
                         ['w2.assume', 1, 'assume(...) that the deploy failed (not hyp), and no plain claim line says it.'],
                         ['w2.pls', 1, 'pls(Quin, ...) to restart the cache.'],
                         ['w2.by', 1, 'The deadline is by(2026-11-06T17:00, ...) round the act (Friday is 2026-11-06; the compact spelling counts).'],
                         ['w2.sug', 1, 'sug(...) to freeze deploys, not pls and not hyp.'],
                         ['w2.at', 1, 'The freeze is at(2026-11-09, ...): a date alone is the whole day (not during, not a clock time).']],
              'loose': False,
              'reference': 'msg(Pia,Quin,Rae,1)\n'
                           'bel(Me,is("cache","stale"))\n'
                           'say(Rae,fin("backup"))\n'
                           'is("disk","full")\n'
                           'assume(is("deploy","failed"))\n'
                           'pls(Quin,by(2026-11-06T17:00,"restart cache"))\n'
                           'sug(at(2026-11-09,"freeze deploys"))',
              'traps': 'bel, say and assume keep a claim from being asserted; hyp is not assume; sug is for the sender and the receivers together; '
                       'Friday and Monday must be dates worked out from today; a date alone is the whole day.'},
             {'id': 'W3',
              'title': 'Eight sentences, one line each',
              'context': [],
              'rubric': [['w3.s1', 1, 'Line 1: not(all(sensors, calibrated)), or some(sensors, not calibrated).'],
                         ['w3.s2',
                          1,
                          'Line 2: exactly one of two claims (eith), or an equivalent made of and, or, not; the claims are pump A running and pump B '
                          'running.'],
                         ['w3.s3',
                          1,
                          'Line 3: all(minus(tanks, tank seven), sealed), or all(tanks, crit(x, if(not(eq(x, tank seven)), is(x, sealed)))).'],
                         ['w3.s4', 1, 'Line 4: over(pct(cnt(filt(samples, contaminated)), cnt(samples)), 40), or the same with a fraction and 0.4.'],
                         ['w3.s5a', 1, 'Line 5: all(pumps, crit(x, some(tanks ..., crit(y, ...)))): a nested quantifier with two bound variables.'],
                         ['w3.s5b', 1, 'Line 5: one relation (feeds) inside has both variables as its places.'],
                         ['w3.s6a', 1, 'Line 6: during(2026-11-09T01:00/2026-11-09T05:00, ...): a stretch with during (not at).'],
                         ['w3.s6b', 1, 'Line 6: rep(3, ...) inside it, about the restart of the cleanup job.'],
                         ['w3.s7a', 1, 'Line 7: a request (pls) whose act is by(t, "send report to {Me}") (the quote reaches Me with braces).'],
                         ['w3.s7b', 1, 'Line 7: t is now plus one hour: plus(now, PT1H) or PT60M.'],
                         ['w3.s8a', 1, 'Line 8: a well-formed formula claim in single quotes (or and(...) of formula claims).'],
                         ['w3.s8b', 1, 'Line 8: it means the same as sum(i^2,i,1,n)<=91 & mod(n,2)=0 for n = 1..14 (tested by evaluation).']],
              'loose': True,
              'reference': 'not(all("sensors","calibrated"))\n'
                           'eith(is("pump a","running"),is("pump b","running"))\n'
                           'all(minus("tanks","tank seven"),"sealed")\n'
                           'over(pct(cnt(filt("samples","contaminated")),cnt("samples")),40)\n'
                           'all("pumps",crit(o1,some("tanks",crit(o2,is(o1,"feeds",o2)))))\n'
                           'during(2026-11-09T01:00/2026-11-09T05:00,rep(3,fin("restart of cleanup job")))\n'
                           'pls(by(plus(now,PT1H),"send report to {Me}"))\n'
                           "'sum(i^2,i,1,n)<=91 & mod(n,2)=0'",
              'traps': 'not(all(...)) for not every; eith for exactly one; minus for except; pct and cnt for a percentage; crit for nested '
                       'quantifiers; during with rep for a count inside a stretch; {Me} and by(plus(now,...)) for me and within an hour; * is never '
                       'left out and ^ is a power in a formula.'},
             {'id': 'W4',
              'title': 'A step-by-step answer',
              'context': ['msg(Ana,Ben,1)\nassume(\'2*x-3=11\')\nwhat(val("x","value"))'],
              'rubric': [['w4.bhdr', 1, 'Ben1: header Ben to Ana, serial 1, re(Ana1) (so that short line numbers are allowed).'],
                         ['w4.s1', 1, 'Ben1: an ent whose first place is Ana1.1 and whose claim is a formula that is true when x is 7.'],
                         ['w4.s2', 1, 'Ben1: the next ent rests on the line just before it (Ben1.k) and concludes x=7.'],
                         ['w4.reasons', 1, 'All three ent lines (two of Ben, one of Ana) carry a reason in the third place.'],
                         ['w4.ans', 1, 'Ben1: ans(Ana1.2, 7) (or x=7): the answer to the question line.'],
                         ['w4.ahdr', 1, 'Ana2: header Ana to Ben, serial 2, re(Ben1).'],
                         ['w4.chk', 1, "Ana2: ent resting on Ben's x=7 line, concluding 2*7-3=11 (or the same with the sides swapped or 14-3=11)."],
                         ['w4.agree', 1, "Ana2: agree pointing at Ben's ans line (Ben1.3 when the steps are two)."]],
              'loose': False,
              'reference': 'msg(Ben,Ana,1,re(Ana1))\n'
                           'ent(Ana1.1,\'2*x=14\',"add 3 to both sides")\n'
                           'ent(Ben1.1,\'x=7\',"divide both sides by 2")\n'
                           'ans(2,7)\n'
                           '---\n'
                           'msg(Ana,Ben,2,re(Ben1))\n'
                           'ent(Ben1.2,\'2*7-3=11\',"substitute 7 for x")\n'
                           'agree(3)',
              'traps': "The header is not a line: Ben's ans is line 3 of his message, so agree(3). ent takes the premise line by its reference. * is "
                       'never left out. ans(2,7): the 2 is a line of Ana1, the 7 is the answer.'},
             {'id': 'W5',
              'title': 'A program, a command and a corrected program',
              'context': [],
              'rubric': [['w5.ahdr', 1, 'Ana1: header Ana to Ben, serial 1.'],
                         ['w5.adef', 1, 'Ana1: def(label, code("python", ...)): a named program, not a request to run it.'],
                         ['w5.alines',
                          1,
                          'Ana1: the lines of the program are exactly the given ones (one quote per line, indentation kept, quote marks doubled).'],
                         ['w5.arev', 1, 'Ana1: pls(Ben, "... {label} ...") asking for a review, the quote reaching her label in braces.'],
                         ['w5.arun', 1, 'Ana1: pls(Ben, code("bash", "grep -c ERROR app.log")): a request to run the command.'],
                         ['w5.bhdr', 1, 'Ben1: header Ben to Ana, serial 1, re(Ana1).'],
                         ['w5.berr', 1, 'Ben1: err pointing at the line of Ana1 that holds the program (line 1; the header is not a line).'],
                         ['w5.bwhy', 1, 'Ben1: err has a second place that says what is wrong (it mentions negative).'],
                         ['w5.bdef', 1, 'Ben1: def(label, code("python", ...)) with a label of his own.'],
                         ['w5.blines', 1, 'Ben1: the lines of the corrected program are exactly the given ones.'],
                         ['w5.buse', 1, 'Ben1: pls(Ana, "... {his label} ... {Ana1.her label} ..."): his label bare, hers with Ana1 in front.'],
                         ['w5.bwill', 1, 'Ben1: will(code("bash", "grep -c ERROR app.log")): the promise.']],
              'loose': False,
              'reference': 'msg(Ana,Ben,1)\n'
                           'def(a1,code("python","def label(n):","    if n == 0:","        return ""none""","    return f""item {n}"""))\n'
                           'pls(Ben,"review {a1}")\n'
                           'pls(Ben,code("bash","grep -c ERROR app.log"))\n'
                           '---\n'
                           'msg(Ben,Ana,1,re(Ana1))\n'
                           'err(1,q"negative number gives item text, not negative")\n'
                           'def(a1,code("python","def label(n):","    if n == 0:","        return ""none""","    if n < 0:","        return '
                           '""negative""","    return f""item {n}"""))\n'
                           'pls(Ana,"use {a1} in place of {Ana1.a1}")\n'
                           'will(code("bash","grep -c ERROR app.log"))',
              'traps': 'A program sent without a request is def(a1,code(...)); pls(Ben,code(...)) asks for a run. Each line of the program is its '
                       'own quote and a quote mark inside is doubled. Braces inside code are raw, but {a1} in an ordinary quote is a reference, and '
                       "another message's label is written {Ana1.a1}. will has one place.",
              'progs': ['def label(n):\n    if n == 0:\n        return "none"\n    return f"item {n}"',
                        'def label(n):\n    if n == 0:\n        return "none"\n    if n < 0:\n        return "negative"\n    return f"item {n}"'],
              'cmd': 'grep -c ERROR app.log'},
             {'id': 'W6',
              'title': 'Headers that fix an order',
              'context': [],
              'rubric': [['w6.hdr',
                          1,
                          'All six headers are well formed, with the right sender, serial and receivers (the other two agents, or All).'],
                         ['w6.pairs', 1, 'No pair of messages is ordered that the facts leave unordered (no extra precedence).'],
                         ['w6.all', 1, 'Every precedence the facts give is shown (nothing missing).'],
                         ['w6.re', 1, 'The re of each header names exactly the message it replies to (none for Ana1 and Ben1).']],
              'loose': False,
              'reference': 'msg(Ana,Ben,Cy,1)\n'
                           'msg(Ben,Ana,Cy,1)\n'
                           'msg(Cy,Ana,Ben,1,re(Ana1),saw(Ben1))\n'
                           'msg(Ana,Ben,Cy,2,re(Cy1))\n'
                           'msg(Ben,Ana,Cy,2,re(Ana1),saw(Cy1))\n'
                           'msg(Cy,Ana,Ben,2,re(Ana2),saw(Ben2))',
              'traps': 're is a reply, saw is a read. saw(Ben2) includes Ben1. Chains give the rest. A saw that the facts do not give makes two '
                       'concurrent messages ordered.'},
             {'id': 'W7',
              'title': 'A long name used in two messages',
              'context': [],
              'rubric': [['w7.hdr', 1, 'Headers: Kai to Lena and Milo, serials 1 and 2.'],
                         ['w7.def', 1, 'Kai1: a label defined on the full name (o1"east wing cold storage freezer", or def(o1,"...")).'],
                         ['w7.once', 1, 'Kai1: the full name appears exactly once in all its quotes.'],
                         ['w7.claim', 1, 'Kai1: a plain claim line that the freezer (by its label) is above zero.'],
                         ['w7.insp', 1, 'Kai1: pls(Lena, by(2026-11-06T17:00, "inspect {label}")): the quote reaches the label by braces.'],
                         ['w7.none', 1, 'Kai2: the full name does not appear.'],
                         ['w7.ref', 1, 'Kai2: a quote reaches the label of Kai1 as {Kai1.label} (with the message in front).'],
                         ['w7.move', 1, 'Kai2: pls(Milo, ...) to move the samples.']],
              'loose': False,
              'reference': 'msg(Kai,Lena,Milo,1)\n'
                           'is(o1"east wing cold storage freezer","above zero")\n'
                           'pls(Lena,by(2026-11-06T17:00,"inspect {o1}"))\n'
                           '---\n'
                           'msg(Kai,Lena,Milo,2)\n'
                           'pls(Milo,"move samples out of {Kai1.o1}")',
              'traps': 'A label is defined by the first quote that carries it (o1"...") and then used alone or as {o1}. In another message it is '
                       'written with its message, {Kai1.o1}; a bare {o1} in Kai2 is undefined (E-NAME). Friday is worked out from today.'},
             {'id': 'W8',
              'title': 'A message that adds an agent',
              'context': ['msg(Dee,Eli,Fay,1)\nis("checkout","down")\nhyp(cause("cache layer","outage"))\nwhat(val("database","replication lag"))',
                          'msg(Eli,Dee,Fay,1,re(Dee1))\nans(3,2)'],
              'rubric': [['w8.hdr', 1, 'Header: Dee to Eli, Fay and Gus, serial 2.'],
                         ['w8.join', 1, 'join(Gus).'],
                         ['w8.ask', 1, 'to(Gus, pls("restart cache")) or pls(Gus, "restart cache"): the request is for Gus.'],
                         ['w8.only', 1, 'Nobody else is asked: no pls with the restart that is addressed to every receiver.'],
                         ['w8.retr',
                          1,
                          'retr(Dee1.2): the hypothesis line of her first message, in full (retr has no short form; the header is not a line).'],
                         ['w8.clr', 1, 'clr pointing at Eli1.1 (clr(1,...) with re(Eli1), or clr(Eli1.1,...)).'],
                         ['w8.unit', 1, 'The clr has a second place that names the unit as what is unclear.']],
              'loose': False,
              'reference': 'msg(Dee,Eli,Fay,Gus,2,re(Eli1))\n'
                           'join(Gus)\n'
                           'to(Gus,pls("restart cache"))\n'
                           'retr(Dee1.2)\n'
                           'clr(1,q"unit of replication lag figure")',
              'traps': 'Gus is named in the header of the message that joins him. A plain pls(...) is for every receiver; the request for Gus alone '
                       'is to(Gus,...) or pls(Gus,...). retr has no short form. Eli1 has one line, so clr must say line 1.'}],
 'picks': {'Q1': ['D', True],
           'Q2': ['B', True],
           'Q3': ['C', True],
           'Q4': ['E', True],
           'Q5': ['C', False],
           'Q6': ['E', False],
           'Q7': ['B', False],
           'Q8': ['D', False],
           'Q9': ['A', True],
           'Q10': ['E', False],
           'Q11': ['B', False],
           'Q12': ['A', True],
           'Q13': [['c', 'e', 'g'], True],
           'Q14': [['a', 'd', 'e'], False],
           'Q15': [['b', 'c', 'e'], False],
           'Q16': ['B', False],
           'Q17': [['Ana1.2', 'error', 'Ana1.2', 'Ana1.2', 'Cy1.2'], False],
           'Q18': [['a', 'e'], False],
           'Q19': [['ok', 'ok', 'ok', 'ok', 'E-NAME', 'ok', 'ok', 'E-QUOTE'], False],
           'Q20': [['ok', 'E-LEX', 'ok', 'E-REDEF', 'E-SYN', 'ok', 'ok'], False],
           'Q21': [['ok', 'ok', 'E-TIME', 'ok', 'E-KIND', 'ok', 'E-TIME'], False],
           'Q22': [['ok', 'ok', 'E-CODE', 'ok', 'ok', 'ok', 'ok', 'ok'], False],
           'Q23': [['ok', 'ok', 'E-HEAD', 'ok', 'ok', 'ok'], False],
           'Q24': [['E-HEAD', 'ok', 'ok', 'E-HEAD', 'ok', 'ok', 'E-HEAD'], False],
           'Q25': [['c', 'd', 'e', 'f', 'g', 'h'], False],
           'Q26': [['a', 'b', 'c', 'd', 'e'], False],
           'Q27': [['a', 'b'], False],
           'Q28': [['force', 'force', 'force'], False],
           'Q29': ['D', False],
           'Q30': [['b', 'd'], True],
           'Q31': [['a', 'b', 'c', 'd'], False],
           'Q32': [['b', 'c', 'd', 'e', 'f', 'h'], False]},
 'selftest': {'perfect': 32, 'perfect_core': 29, 'picks_strict': 8, 'picks_core': 5, 'writing_reference': 68},
 'z1_checklist': ["Header: from Rae to Kai and Lena; Rae's third message; urgent (pri hi).",
                  'It answers Kai2 (re) and Rae had read Lena1 (saw).',
                  'agree(2) means agree with line 2 of Kai2 (short form, because re names exactly one whole message).',
                  'rej(1,...) declines line 1 of Kai2 (a request or proposal); the reason, that Rae may not open the vault, is asserted.',
                  'The seal-caused-leak line is a hypothesis: not asserted; Rae suspects it.',
                  'prob(...,lo): the sender puts it at low probability (unlikely); still not asserted as fact.',
                  'The if line is tested separately for Kai and for Lena (You per receiver): each who is on call is asked to check the seal.',
                  'after(fin("flush"),...) says Kai samples water after the flush ends; it does not assert that the flush has finished.',
                  'sug(...) proposes replacing the seal at 10:00 on 2026-11-12 for the sender and the receivers; nothing is adopted until both Kai '
                  'and Lena have agreed.'],
 'z1_message': 'msg(Rae,Kai,Lena,3,re(Kai2),saw(Lena1),pri(hi))\n'
               'agree(2)\n'
               'rej(1,not(may(Me,"open vault")))\n'
               'hyp(cause("seal","leak"))\n'
               'prob(cause("seal","leak"),lo)\n'
               'if(is(You,"on call"),pls(You,"check seal"))\n'
               'after(fin("flush"),act(Kai,"sample water"))\n'
               'sug(at(2026-11-12T10:00,"replace seal"))'}

READING = KEY['reading']
WRITING = KEY['writing']
WKEY = dict((t['id'], t) for t in WRITING)
PICKS = KEY['picks']

# ------------------------------------------------------------------------------------------------------------------------
# THE CHECKER (loaded when it is first needed)
# ------------------------------------------------------------------------------------------------------------------------
CHECKER_NOTE = []

def find_checker(explicit=None):
    here = os.path.dirname(os.path.abspath(__file__))
    names = ['silex_check_r6.4.py']
    cands = []
    if explicit:
        cands.append(explicit)
    if os.environ.get('SILEX_CHECKER'):
        cands.append(os.environ['SILEX_CHECKER'])
    for d in ('.', 'tools', '../tools', here, os.path.join(here, 'tools'), os.path.join(here, '..', 'tools'),
              os.path.expanduser('~/SILEX/tools'), os.path.expanduser('~/silex/tools')):
        for n in names:
            cands.append(os.path.join(d, n))
    for c in cands:
        if c and os.path.isfile(c):
            return c
    return None

class _Checker(object):
    mod = None
    path = None
    explicit = None
    def __getattr__(self, name):
        if _Checker.mod is None:
            load_checker(_Checker.explicit)
        return getattr(_Checker.mod, name)

def load_checker(explicit=None):
    if _Checker.mod is not None:
        return _Checker.mod
    path = find_checker(explicit)
    if not path:
        raise RuntimeError('the r6.4 checker (silex_check_r6.4.py) was not found; give its place with --checker PATH')
    raw = open(path, 'rb').read()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != CHECKER_SHA256:
        CHECKER_NOTE.append('WARNING: %s is not the checker this scorer was built with (SHA-256 %s, expected %s). '
                            'Writing scores may differ from the intended ones.' % (path, sha[:16] + '...', CHECKER_SHA256[:16] + '...'))
    spec = importlib.util.spec_from_file_location('silex_check_r64', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    _Checker.mod, _Checker.path = mod, path
    return mod

sxc = _Checker()

# ------------------------------------------------------------------------------------------------------------------------
# THE WRITING RUBRIC AND SCORER
# ------------------------------------------------------------------------------------------------------------------------
# ---- rubric of the WRITING part (inlined into the scorer) -------------------------------------------------------------
# Needs: sxc (the r6.4 checker module) and WKEY (dict task id -> data of the writing key, e.g. WKEY['W5']['progs'])
# (sxc is the checker loaded above; WKEY is the writing key)
import re as _re

_NAME = _re.compile(r'^([A-Z][a-z]*\d+|#\d+)(?:\.(\d+))?')

class Msg(object):
    pass

def build(texts):
    """texts (context first, then the answer) -> list of Msg.  A line or header earns credit only when the checker gives it
       `ok` and no conversation-level problem is attached to it."""
    rep = sxc.check_conversation([(1, t) for t in texts], need_header=True)
    bad = {}                                         # name -> set of line numbers (0 = the message as a whole)
    why = {}                                         # (name, line number) -> the problems themselves
    other = []
    for p in rep['across_messages']:
        m = _NAME.match(p)
        if m:
            bad.setdefault(m.group(1), set()).add(int(m.group(2)) if m.group(2) else 0)
            why.setdefault((m.group(1), int(m.group(2)) if m.group(2) else 0), []).append(p)
        else:
            other.append(p)
    out = []
    for i, t in enumerate(texts):
        mm = rep['messages'][i]
        m = Msg()
        m.text, m.index = t, i
        m.name, m.sender, m.recv, m.serial = mm['name'], mm['sender'], list(mm['receivers']), mm['serial']
        key = m.name or ('#%d' % (i + 1))
        m.hv = mm['header']['verdict'] if mm['header'] else 'E-HEAD'
        m.hok = (m.hv == 'ok') and (0 not in bad.get(key, ()))
        m.verd = [l['verdict'] for l in mm['lines']]
        m.src = [l['source'] for l in mm['lines']]
        an = sxc.analyse(t)
        m.trees = list(an['lines']) if an else []
        m.labels = set(an['labels']) if an else set()
        m.conv_why = dict((ln, why[(key, ln)]) for (k2, ln) in why if k2 == key)
        m.ok = []
        for j, v in enumerate(m.verd):
            tree = m.trees[j] if j < len(m.trees) else None
            m.ok.append(v == 'ok' and tree is not None and (j + 1) not in bad.get(key, ()))
        m.re_names, m.saw_names, m.re_whole = [], [], []
        try:
            items = sxc.parse(t)
            h = items[0][1] if items and items[0][0] == 'ok' else None
        except Exception:
            h = None
        if h is not None and h.t == 'app' and h.v == 'msg':
            for a in h.args:
                if a.t == 'app' and a.v in ('re', 'saw'):
                    names = [x.v for x in a.args if x.t == 'ref']
                    (m.re_names if a.v == 're' else m.saw_names).extend(names)
                    if a.v == 're':
                        m.re_whole = [x for x in names if '.' not in x]
        out.append(m)
    return out, other

# ---------------------------------------------------------------- tree helpers
def walk(t):
    yield t
    for a in t.args:
        for x in walk(a):
            yield x

def is_app(t, v, n=None):
    return t is not None and t.t == 'app' and t.v == v and (n is None or len(t.args) == n)

def qtexts(t):
    return [n.v for n in walk(t) if n.t == 'str' and n.pre != "'"]

def low(t):
    return ' | '.join(qtexts(t)).lower()

def toks(t):
    return set(_re.findall(r"[a-z0-9]+", low(t)))

def tok_has(t, *prefixes):
    tk = toks(t)
    return all(any(x.startswith(p) for x in tk) for p in prefixes)

def refs(t):
    return [n.v for n in walk(t) if n.t == 'ref']

def lines(m):
    """(number, tree) of the valid lines of a message"""
    return [(j + 1, m.trees[j]) for j in range(len(m.ok)) if m.ok[j]]

def find(m, pred):
    return [(j, t) for j, t in lines(m) if pred(t)]

def agent(t, *names):
    return t is not None and t.t == 'agent' and (not names or t.v in names)

def num(t):
    try:
        return float(t.v) if t is not None and t.t == 'num' else None
    except ValueError:
        return None

def tnorm(s):
    s = sxc.ext_time(s)
    return '/'.join(_re.sub(r'(T\d\d:\d\d):00(?=$|[Z+-])', r'\1', p) for p in s.split('/'))

def dur_sec(s):
    m = _re.match(r'^P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)W)?(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?$', s)
    if not m:
        return None
    y, mo, w, d, h, mi, se = [int(x) if x else 0 for x in m.groups()]
    return ((y * 365 + mo * 30 + w * 7 + d) * 24 + h) * 3600 + mi * 60 + se

def whole_day(s, day):
    s = tnorm(s)
    if s == day:
        return True
    if '/' in s:
        a, b = s.split('/')
        nxt = day[:8] + '%02d' % (int(day[8:10]) + 1)
        return a == day + 'T00:00' and b in (day + 'T23:59', day + 'T24:00', nxt + 'T00:00', day + 'T23:59:59')
    return False

# ---------------------------------------------------------------- what a line asserts (1.8)
SPEECH = {'pls', 'will', 'rej', 'sug', 'agree', 'yn', 'what', 'which', 'why', 'ans', 'unk', 'hyp', 'assume', 'retr', 'ack', 'err', 'clr',
          'join', 'leave', 'to', 'def'}
MENTION = {'bel', 'say', 'want', 'plan', 'must', 'should', 'may', 'can', 'need', 'prob', 'supp', 'ent', 'would', 'if'}

def plain_claim(t):
    """a line that is a claim of its own (asserted): not a speech act and not a root that only mentions"""
    if t is None:
        return False
    if t.t == 'str' and t.pre == "'":
        return True
    return t.t == 'app' and t.v not in SPEECH and t.v not in MENTION and t.v not in ('msg',)

def has_neg(t):
    return any(n.t == 'app' and n.v == 'not' for n in walk(t))

def asserted(m):
    """claims that the lines of m assert: plain claim lines, the reason of rej, the claim of err (know and cause assert too, 1.8)"""
    out = []
    for j, t in lines(m):
        if plain_claim(t):
            out.append(t)
        elif t.t == 'app' and t.v in ('rej', 'err') and len(t.args) == 2:
            out.append(t.args[1])
    return out

def asserts_tokens(m, *prefixes, **kw):
    pos = kw.get('neg_ok', False)
    return any(tok_has(c, *prefixes) and (pos or not has_neg(c)) for c in asserted(m))

# ---------------------------------------------------------------- headers
def hdr_ok(m, sender, recv, serial):
    if m is None or not m.hok or m.sender != sender or m.serial != serial:
        return False
    return set(m.recv) == set(recv) and len(m.recv) == len(set(recv))

def pick(msgs, sender, serial):
    for m in msgs:
        if m.sender == sender and m.serial == serial:
            return m
    return None

def names_in_header(m):
    return set(x.split('.')[0] for x in m.re_names + m.saw_names)

# ---------------------------------------------------------------- propositional form (W3 line 2)
def prop_fn(t, classify):
    if t.t == 'app' and t.v in ('and', 'or', 'eith') and t.args:
        fs = [prop_fn(a, classify) for a in t.args]
        if t.v == 'and':
            return lambda e: all(f(e) for f in fs)
        if t.v == 'or':
            return lambda e: any(f(e) for f in fs)
        return lambda e: sum(1 for f in fs if f(e)) == 1
    if t.t == 'app' and t.v == 'not' and len(t.args) == 1:
        f = prop_fn(t.args[0], classify)
        return lambda e: not f(e)
    k = classify(t)
    if k is None:
        raise ValueError('unknown atom')
    return lambda e: e[k]

# ---------------------------------------------------------------- a small evaluator for formulas in single quotes
class FmErr(Exception):
    pass

_FT = _re.compile(r'\s*(?:(?P<num>\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?P<name>[A-Za-z][A-Za-z0-9_]*)|(?P<op><=>|=>|<=|>=|!=|[-+*/^()=<>,&|]))')

def fm_parse(s):
    toks_, pos = [], 0
    while s[pos:].strip():
        m = _FT.match(s, pos)
        if not m:
            raise FmErr('bad character')
        k = m.lastgroup
        toks_.append((k, m.group(k)))
        pos = m.end()
    st = [0]
    def peek():
        return toks_[st[0]] if st[0] < len(toks_) else ('end', '')
    def take():
        t = peek(); st[0] += 1; return t
    def isop(*ops):
        t = peek(); return t[0] == 'op' and t[1] in ops
    def formula():
        a = implication()
        if isop('<=>'):
            take(); b = implication(); return ('iff', a, b)
        return a
    def implication():
        a = disj()
        if isop('=>'):
            take(); b = disj(); return ('imp', a, b)
        return a
    def disj():
        a = conj()
        while isop('|'):
            take(); a = ('or', a, conj())
        return a
    def conj():
        a = cmp_()
        while isop('&'):
            take(); a = ('and', a, cmp_())
        return a
    def cmp_():
        a = expr()
        if isop('=', '!=', '<', '>', '<=', '>='):
            op = take()[1]; b = expr(); return ('cmp', op, a, b)
        return a
    def expr():
        a = term()
        while isop('+', '-'):
            op = take()[1]; a = ('bin', op, a, term())
        return a
    def term():
        a = unary()
        while isop('*', '/'):
            op = take()[1]; a = ('bin', op, a, unary())
        return a
    def unary():
        if isop('-'):
            take(); return ('neg', unary())
        a = atom()
        if isop('^'):
            take(); return ('bin', '^', a, unary())
        return a
    def atom():
        t = take()
        if t[0] == 'num':
            return ('num', float(t[1]))
        if t[0] == 'name':
            if isop('('):
                take(); args = []
                while True:
                    args.append(expr())
                    u = take()
                    if u == ('op', ')'):
                        break
                    if u != ('op', ','):
                        raise FmErr('bad call')
                return ('call', t[1], args)
            return ('name', t[1])
        if t == ('op', '('):
            a = formula()
            if take() != ('op', ')'):
                raise FmErr('bracket')
            return a
        raise FmErr('unexpected')
    a = formula()
    if peek()[0] != 'end':
        raise FmErr('trailing')
    return a

def fm_free(a, bound=()):
    k = a[0]
    if k == 'name':
        return set() if a[1] in bound or a[1] in ('pi', 'e') else {a[1]}
    if k == 'call':
        if a[1] in ('sum', 'prod') and len(a[2]) == 4 and a[2][1][0] == 'name':
            i = a[2][1][1]
            return fm_free(a[2][0], tuple(bound) + (i,)) | fm_free(a[2][2], bound) | fm_free(a[2][3], bound)
        s = set()
        for x in a[2]:
            s |= fm_free(x, bound)
        return s
    s = set()
    for x in a[1:]:
        if isinstance(x, tuple):
            s |= fm_free(x, bound)
    return s

def _gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def fm_eval(a, env):
    import math
    k = a[0]
    if k == 'num':
        return a[1]
    if k == 'name':
        if a[1] == 'pi': return math.pi
        if a[1] == 'e': return math.e
        return env[a[1]]
    if k == 'neg':
        return -fm_eval(a[1], env)
    if k == 'bin':
        x, y = fm_eval(a[2], env), fm_eval(a[3], env)
        op = a[1]
        if op == '+': return x + y
        if op == '-': return x - y
        if op == '*': return x * y
        if op == '/': return x / y
        return x ** y
    if k == 'cmp':
        x, y = fm_eval(a[2], env), fm_eval(a[3], env)
        op = a[1]
        eps = 1e-9 * max(1.0, abs(x), abs(y))
        if op == '=': return abs(x - y) <= eps
        if op == '!=': return abs(x - y) > eps
        if op == '<': return x < y - eps
        if op == '>': return x > y + eps
        if op == '<=': return x <= y + eps
        return x >= y - eps
    if k == 'and': return bool(fm_eval(a[1], env)) and bool(fm_eval(a[2], env))
    if k == 'or': return bool(fm_eval(a[1], env)) or bool(fm_eval(a[2], env))
    if k == 'imp': return (not fm_eval(a[1], env)) or bool(fm_eval(a[2], env))
    if k == 'iff': return bool(fm_eval(a[1], env)) == bool(fm_eval(a[2], env))
    if k == 'call':
        f, args = a[1], a[2]
        if f in ('sum', 'prod'):
            if len(args) != 4 or args[1][0] != 'name':
                raise FmErr('sum')
            lo, hi = int(round(fm_eval(args[2], env))), int(round(fm_eval(args[3], env)))
            acc = 0 if f == 'sum' else 1
            for i in range(lo, hi + 1):
                e2 = dict(env); e2[args[1][1]] = float(i)
                v = fm_eval(args[0], e2)
                acc = acc + v if f == 'sum' else acc * v
            return acc
        v = [fm_eval(x, env) for x in args]
        if f == 'mod' and len(v) == 2: return v[0] % v[1]
        if f == 'abs' and len(v) == 1: return abs(v[0])
        if f == 'sqrt' and len(v) == 1: return math.sqrt(v[0])
        if f == 'fact' and len(v) == 1: return float(math.factorial(int(round(v[0]))))
        if f == 'gcd' and len(v) == 2: return float(_gcd(int(v[0]), int(v[1])))
        if f == 'min' and v: return min(v)
        if f == 'max' and v: return max(v)
        if f == 'floor' and len(v) == 1: return float(math.floor(v[0]))
        if f == 'ceil' and len(v) == 1: return float(math.ceil(v[0]))
        raise FmErr('function ' + f)
    raise FmErr('node')

def fm_truth(src, **env):
    """the truth of a formula claim for the given values, or None when it cannot be evaluated"""
    try:
        a = fm_parse(src)
        return bool(fm_eval(a, dict((k, float(v)) for k, v in env.items())))
    except Exception:
        return None

def fm_free_names(src):
    try:
        return fm_free(fm_parse(src))
    except Exception:
        return None

def fm_same_in(src, expected_fn, var, values):
    """does the formula src, with its one free name read as var, have the truth that expected_fn gives, for all values?"""
    fr = fm_free_names(src)
    if fr is None or len(fr) != 1:
        return False
    name = list(fr)[0]
    for v in values:
        t = fm_truth(src, **{name: v})
        if t is None or t != expected_fn(v):
            return False
    return True

def fm_compact(src):
    return _re.sub(r'\s+', '', src)

# ---------------------------------------------------------------- the rubric
RUBRIC = {}
def rub(rid):
    def deco(fn):
        RUBRIC[rid] = fn
        return fn
    return deco

def _pointers(m):
    return [(j, t) for j, t in lines(m) if t.t == 'app' and t.v in ('agree', 'rej', 'err', 'ans', 'clr', 'retr', 'unk')]

def _ref0(t):
    return t.args[0].v if t.args and t.args[0].t == 'ref' else None

# ---- W1
def _w1m(A, C):
    return pick(A, 'Milo', 1)

@rub('w1.hdr')
def _(A, C):
    m = _w1m(A, C)
    return hdr_ok(m, 'Milo', {'Kai', 'Lena'}, 1) and {'Kai1', 'Lena1'} <= names_in_header(m)

@rub('w1.agree')
def _(A, C):
    m = _w1m(A, C)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'agree', 1) and _ref0(t) == 'Kai1.3'))

@rub('w1.rej')
def _(A, C):
    m = _w1m(A, C)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'rej') and _ref0(t) == 'Kai1.1'))

def _perm_denied(t, who, *words):
    inner = None
    if is_app(t, 'not', 1) and is_app(t.args[0], 'may', 2):
        inner = t.args[0]
    elif is_app(t, 'must', 2) and is_app(t.args[1], 'not', 1):
        inner = t
    if inner is None or not agent(inner.args[0], *who):
        return False
    return tok_has(inner, *words)

@rub('w1.why')
def _(A, C):
    m = _w1m(A, C)
    if not m:
        return False
    for j, t in find(m, lambda t: is_app(t, 'rej', 2) and _ref0(t) == 'Kai1.1'):
        if _perm_denied(t.args[1], ('Me', 'Milo'), 'open', 'valve') and ({'six', '6'} & toks(t.args[1])):
            return True
    return False

@rub('w1.err')
def _(A, C):
    m = _w1m(A, C)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'err') and _ref0(t) == 'Lena1.2'))

@rub('w1.full')
def _(A, C):
    m = _w1m(A, C)
    if not m:
        return False
    for j, t in lines(m):
        c = t.args[1] if (is_app(t, 'err', 2) and _ref0(t) == 'Lena1.2') else (t if plain_claim(t) else None)
        if c is not None and tok_has(c, 'tank', 'three', 'full') and not has_neg(c):
            return True
    return False

@rub('w1.ans')
def _(A, C):
    m = _w1m(A, C)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'ans', 2) and _ref0(t) == 'Lena1.3' and t.args[1].t == 'atom' and t.args[1].v == 'yes'))

@rub('w1.clean')
def _(A, C):
    m = _w1m(A, C)
    if not m:
        return False
    ps = _pointers(m)
    return bool(ps) and all(_ref0(t) in ('Kai1.3', 'Kai1.1', 'Lena1.2', 'Lena1.3') for j, t in ps)

# ---- W2
def _w2m(A, C):
    return pick(A, 'Pia', 1)

@rub('w2.hdr')
def _(A, C):
    return hdr_ok(_w2m(A, C), 'Pia', {'Quin', 'Rae'}, 1)

@rub('w2.bel')
def _(A, C):
    m = _w2m(A, C)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'bel', 2) and agent(t.args[0], 'Me', 'Pia') and tok_has(t.args[1], 'cache', 'stale'))) \
        and not asserts_tokens(m, 'cache', 'stale')

@rub('w2.say')
def _(A, C):
    m = _w2m(A, C)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'say', 2) and agent(t.args[0], 'Rae') and tok_has(t.args[1], 'backup'))) \
        and not asserts_tokens(m, 'backup')

@rub('w2.fact')
def _(A, C):
    m = _w2m(A, C)
    return bool(m) and any(plain_claim(t) and tok_has(t, 'disk', 'full') and not has_neg(t) for j, t in lines(m))

@rub('w2.assume')
def _(A, C):
    m = _w2m(A, C)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'assume', 1) and tok_has(t.args[0], 'deploy', 'fail'))) \
        and not asserts_tokens(m, 'deploy', 'fail')

def _w2pls(m):
    return find(m, lambda t: is_app(t, 'pls', 2) and agent(t.args[0], 'Quin') and tok_has(t.args[1], 'restart', 'cache'))

@rub('w2.pls')
def _(A, C):
    m = _w2m(A, C)
    return bool(m) and bool(_w2pls(m))

@rub('w2.by')
def _(A, C):
    m = _w2m(A, C)
    if not m:
        return False
    for j, t in _w2pls(m):
        if any(is_app(n, 'by', 2) and n.args[0].t == 'time' and tnorm(n.args[0].v) == '2026-11-06T17:00' and tok_has(n.args[1], 'restart', 'cache')
               for n in walk(t.args[1])):
            return True
    return False

def _w2sug(m):
    return find(m, lambda t: is_app(t, 'sug', 1) and tok_has(t, 'deploy') and (tok_has(t, 'freez') or tok_has(t, 'froz')))

@rub('w2.sug')
def _(A, C):
    m = _w2m(A, C)
    return bool(m) and bool(_w2sug(m))

@rub('w2.at')
def _(A, C):
    m = _w2m(A, C)
    if not m:
        return False
    for j, t in _w2sug(m):
        if any(is_app(n, 'at', 2) and n.args[0].t == 'time' and whole_day(n.args[0].v, '2026-11-09') for n in walk(t)):
            return True
    return False

# ---- W3 (the answer is loose lines; A is [pseudo message] built by build_loose)
def _L(A, i):
    m = A[0] if A else None
    if m is None or i >= len(m.ok) or not m.ok[i]:
        return None
    return m.trees[i]

@rub('w3.s1')
def _(A, C):
    t = _L(A, 0)
    if t is None:
        return False
    if is_app(t, 'not', 1) and is_app(t.args[0], 'all', 2) and tok_has(t, 'sensor', 'calibrat'):
        return True
    if is_app(t, 'some', 2) and tok_has(t.args[0], 'sensor'):
        c = t.args[1]
        return (is_app(c, 'not', 1) and tok_has(c, 'calibrat')) or tok_has(c, 'uncalibrat') or tok_has(c, 'not', 'calibrat')
    return False

def _pump_atom(t):
    tk = toks(t)
    if 'pump' in tk and any(x.startswith('run') for x in tk):
        if 'a' in tk and 'b' not in tk: return 'A'
        if 'b' in tk and 'a' not in tk: return 'B'
    return None

@rub('w3.s2')
def _(A, C):
    t = _L(A, 1)
    if t is None:
        return False
    try:
        f = prop_fn(t, _pump_atom)
    except ValueError:
        return False
    import itertools
    for a, b in itertools.product([False, True], repeat=2):
        if f({'A': a, 'B': b}) != (a != b):
            return False
    return True

@rub('w3.s3')
def _(A, C):
    t = _L(A, 2)
    if not is_app(t, 'all', 2):
        return False
    g, c = t.args
    seven = lambda x: bool({'seven', '7'} & toks(x))
    if is_app(g, 'minus', 2) and tok_has(g.args[0], 'tank') and seven(g.args[1]) and tok_has(c, 'seal'):
        return True
    if tok_has(g, 'tank') and is_app(c, 'crit', 2) and tok_has(c, 'seal') and seven(c) and \
            any(n.t == 'app' and n.v in ('not', 'or', 'if') for n in walk(c.args[1])):
        return True
    return False

@rub('w3.s4')
def _(A, C):
    t = _L(A, 3)
    if not is_app(t, 'over', 2) or not tok_has(t, 'sample', 'contaminat'):
        return False
    a, b = t.args
    has = lambda x, r: any(is_app(n, r) for n in walk(x))
    if num(b) == 40 and has(a, 'pct') and has(a, 'cnt') and has(a, 'filt'):
        return True
    if num(b) == 0.4 and has(a, 'div') and has(a, 'cnt') and has(a, 'filt'):
        return True
    if is_app(b, 'times') and has(a, 'cnt') and has(a, 'filt') and any(num(x) == 0.4 for x in b.args):
        return True
    if num(b) == 40 and has(a, 'times') and has(a, 'div') and has(a, 'filt'):
        return True
    return False

def _s5(t):
    """-> (found quantifier structure, relation has both variables)"""
    if not (is_app(t, 'all', 2) and tok_has(t.args[0], 'pump') and is_app(t.args[1], 'crit', 2) and t.args[1].args[0].t == 'label'):
        return False, False
    v1, body = t.args[1].args[0].v, t.args[1].args[1]
    for n in walk(body):
        if not is_app(n, 'some'):
            continue
        v2 = rel = g = None
        if len(n.args) == 2 and is_app(n.args[1], 'crit', 2) and n.args[1].args[0].t == 'label':
            g, v2, rel = n.args[0], n.args[1].args[0].v, n.args[1].args[1]
        elif len(n.args) == 1 and is_app(n.args[0], 'filt', 2) and is_app(n.args[0].args[1], 'crit', 2) and n.args[0].args[1].args[0].t == 'label':
            g, v2, rel = n.args[0].args[0], n.args[0].args[1].args[0].v, n.args[0].args[1].args[1]
        if g is None or not tok_has(g, 'tank'):
            continue
        both = any(x.t == 'app' and {v1, v2} <= set(y.v for y in x.args if y.t == 'label') and tok_has(x, 'feed') for x in walk(rel))
        return True, both
    return False, False

@rub('w3.s5a')
def _(A, C):
    t = _L(A, 4)
    return t is not None and _s5(t)[0]

@rub('w3.s5b')
def _(A, C):
    t = _L(A, 4)
    return t is not None and _s5(t)[1]

@rub('w3.s6a')
def _(A, C):
    t = _L(A, 5)
    return is_app(t, 'during', 2) and t.args[0].t == 'time' and tnorm(t.args[0].v) == '2026-11-09T01:00/2026-11-09T05:00'

@rub('w3.s6b')
def _(A, C):
    t = _L(A, 5)
    return is_app(t, 'during', 2) and t.args[0].t == 'time' and tnorm(t.args[0].v) == '2026-11-09T01:00/2026-11-09T05:00' and \
        any(is_app(n, 'rep', 2) and num(n.args[0]) == 3 and tok_has(n, 'restart', 'cleanup') for n in walk(t.args[1]))

def _s7(t):
    if t is None or not is_app(t, 'pls') or not (len(t.args) == 1 or (len(t.args) == 2 and agent(t.args[0], 'You'))):
        return None
    x = t.args[-1]
    if is_app(x, 'by', 2) and tok_has(x, 'report') and '{me}' in low(x):
        return x
    return None

@rub('w3.s7a')
def _(A, C):
    return _s7(_L(A, 6)) is not None

@rub('w3.s7b')
def _(A, C):
    x = _s7(_L(A, 6))
    if x is None:
        return False
    tm = x.args[0]
    return is_app(tm, 'plus', 2) and any(n.t == 'atom' and n.v == 'now' for n in tm.args) and \
        any(n.t == 'dur' and dur_sec(n.v) == 3600 for n in tm.args)

def _w3_formulas(t):
    if t is None:
        return None
    if t.t == 'str' and t.pre == "'":
        return [t.v]
    if is_app(t, 'and') and t.args and all(a.t == 'str' and a.pre == "'" for a in t.args):
        return [a.v for a in t.args]
    return None

@rub('w3.s8a')
def _(A, C):
    return _w3_formulas(_L(A, 7)) is not None

@rub('w3.s8b')
def _(A, C):
    fs = _w3_formulas(_L(A, 7))
    if not fs:
        return False
    names = set()
    for f in fs:
        fr = fm_free_names(f)
        if fr is None:
            return False
        names |= fr
    if len(names) != 1:
        return False
    nm = list(names)[0]
    for n in range(1, 15):
        want = (sum(i * i for i in range(1, n + 1)) <= 91) and n % 2 == 0
        got = True
        for f in fs:
            r = fm_truth(f, **{nm: n})
            if r is None:
                return False
            got = got and r
        if got != want:
            return False
    return True

# ---- W4
def _w4(A):
    return pick(A, 'Ben', 1), pick(A, 'Ana', 2)

def _ents(m):
    return find(m, lambda t: is_app(t, 'ent') and len(t.args) >= 2)

def _w4_steps(b):
    """-> (line number and tree of step 1, of step 2) or Nones"""
    e = [(j, t) for j, t in _ents(b) if _ref0(t) is not None]
    s1 = next(((j, t) for j, t in e if _ref0(t) == 'Ana1.1'), (None, None))
    s2 = (None, None)
    if s1[0] is not None:
        s2 = next(((j, t) for j, t in e if _ref0(t) == 'Ben1.%d' % s1[0] and j > s1[0]), (None, None))
    return s1, s2

@rub('w4.bhdr')
def _(A, C):
    b, a = _w4(A)
    return hdr_ok(b, 'Ben', {'Ana'}, 1) and b.re_whole == ['Ana1'] and b.re_names == ['Ana1']

@rub('w4.s1')
def _(A, C):
    b, a = _w4(A)
    if not b:
        return False
    (j, t), _s2 = _w4_steps(b)
    if t is None:
        return False
    f = t.args[1]
    if not (f.t == 'str' and f.pre == "'"):
        return False
    if fm_compact(f.v) in ('x=7', '7=x'):
        return False
    fr = fm_free_names(f.v)
    return fr == {'x'} and fm_truth(f.v, x=7) is True

@rub('w4.s2')
def _(A, C):
    b, a = _w4(A)
    if not b:
        return False
    s1, (j, t) = _w4_steps(b)
    return t is not None and t.args[1].t == 'str' and t.args[1].pre == "'" and fm_compact(t.args[1].v) in ('x=7', '7=x')

@rub('w4.reasons')
def _(A, C):
    b, a = _w4(A)
    if not b or not a:
        return False
    es = _ents(b) + _ents(a)
    return len(es) >= 3 and all(len(t.args) == 3 and t.args[2].t == 'str' and t.args[2].pre != "'" for j, t in es)

def _w4_ans(b):
    for j, t in find(b, lambda t: is_app(t, 'ans', 2) and _ref0(t) == 'Ana1.2'):
        v = t.args[1]
        if (num(v) == 7) or (v.t == 'str' and v.pre == "'" and fm_compact(v.v) in ('x=7', '7=x')):
            return j
    return None

@rub('w4.ans')
def _(A, C):
    b, a = _w4(A)
    return bool(b) and _w4_ans(b) is not None

@rub('w4.ahdr')
def _(A, C):
    b, a = _w4(A)
    return hdr_ok(a, 'Ana', {'Ben'}, 2) and a.re_whole == ['Ben1'] and a.re_names == ['Ben1']

@rub('w4.chk')
def _(A, C):
    b, a = _w4(A)
    if not b or not a:
        return False
    s1, (j2, t2) = _w4_steps(b)
    if j2 is None:
        return False
    for j, t in _ents(a):
        if _ref0(t) != 'Ben1.%d' % j2:
            continue
        f = t.args[1]
        if f.t == 'str' and f.pre == "'":
            tk = set(_re.findall(r'\d+(?:\.\d+)?', f.v))
            if fm_free_names(f.v) == set() and fm_truth(f.v) is True and {'7', '11'} <= tk:
                return True
    return False

@rub('w4.agree')
def _(A, C):
    b, a = _w4(A)
    if not b or not a:
        return False
    k = _w4_ans(b)
    return k is not None and bool(find(a, lambda t: is_app(t, 'agree', 1) and _ref0(t) == 'Ben1.%d' % k))

# ---- W5
def _code(t):
    if is_app(t, 'code') and t.args and all(x.t == 'str' for x in t.args):
        return t.args[0].v, [x.v.rstrip() for x in t.args[1:]]
    return None

def _w5_msgs(A):
    return pick(A, 'Ana', 1), pick(A, 'Ben', 1)

def _w5_def(m, prog):
    """-> (line, label, ok-lines) of a def of a python program in m"""
    for j, t in find(m, lambda t: is_app(t, 'def', 2) and t.args[0].t == 'label' and _code(t.args[1]) is not None):
        lang, ls = _code(t.args[1])
        if lang == 'python':
            return j, t.args[0].v, ls == [x.rstrip() for x in prog.split('\n')]
    return None, None, False

@rub('w5.ahdr')
def _(A, C):
    a, b = _w5_msgs(A)
    return hdr_ok(a, 'Ana', {'Ben'}, 1)

@rub('w5.adef')
def _(A, C):
    a, b = _w5_msgs(A)
    return bool(a) and _w5_def(a, WKEY['W5']['progs'][0])[0] is not None

@rub('w5.alines')
def _(A, C):
    a, b = _w5_msgs(A)
    return bool(a) and _w5_def(a, WKEY['W5']['progs'][0])[2]

@rub('w5.arev')
def _(A, C):
    a, b = _w5_msgs(A)
    if not a:
        return False
    j, lab, ok = _w5_def(a, WKEY['W5']['progs'][0])
    if lab is None:
        return False
    return bool(find(a, lambda t: is_app(t, 'pls', 2) and agent(t.args[0], 'Ben') and t.args[1].t == 'str' and t.args[1].pre != "'"
                     and '{%s}' % lab in t.args[1].v and tok_has(t.args[1], 'review')))

@rub('w5.arun')
def _(A, C):
    a, b = _w5_msgs(A)
    cmd = WKEY['W5']['cmd']
    return bool(a) and bool(find(a, lambda t: is_app(t, 'pls', 2) and agent(t.args[0], 'Ben') and _code(t.args[1]) == ('bash', [cmd])))

@rub('w5.bhdr')
def _(A, C):
    a, b = _w5_msgs(A)
    return hdr_ok(b, 'Ben', {'Ana'}, 1) and b.re_whole == ['Ana1'] and b.re_names == ['Ana1']

def _w5_err(a, b):
    j, lab, ok = _w5_def(a, WKEY['W5']['progs'][0])
    if j is None:
        return None
    return find(b, lambda t: is_app(t, 'err') and _ref0(t) == 'Ana1.%d' % j)

@rub('w5.berr')
def _(A, C):
    a, b = _w5_msgs(A)
    return bool(a) and bool(b) and bool(_w5_err(a, b))

@rub('w5.bwhy')
def _(A, C):
    a, b = _w5_msgs(A)
    if not (a and b):
        return False
    return any(len(t.args) == 2 and tok_has(t.args[1], 'negativ') for j, t in (_w5_err(a, b) or []))

@rub('w5.bdef')
def _(A, C):
    a, b = _w5_msgs(A)
    return bool(b) and _w5_def(b, WKEY['W5']['progs'][1])[0] is not None

@rub('w5.blines')
def _(A, C):
    a, b = _w5_msgs(A)
    return bool(b) and _w5_def(b, WKEY['W5']['progs'][1])[2]

@rub('w5.buse')
def _(A, C):
    a, b = _w5_msgs(A)
    if not (a and b):
        return False
    ja, la, _o = _w5_def(a, WKEY['W5']['progs'][0])
    jb, lb, _o2 = _w5_def(b, WKEY['W5']['progs'][1])
    if la is None or lb is None:
        return False
    return bool(find(b, lambda t: is_app(t, 'pls', 2) and agent(t.args[0], 'Ana') and t.args[1].t == 'str' and t.args[1].pre != "'"
                     and '{%s}' % lb in t.args[1].v and '{Ana1.%s}' % la in t.args[1].v))

@rub('w5.bwill')
def _(A, C):
    a, b = _w5_msgs(A)
    cmd = WKEY['W5']['cmd']
    return bool(b) and bool(find(b, lambda t: is_app(t, 'will', 1) and _code(t.args[0]) == ('bash', [cmd])))

# ---- W6
W6_EXPECT = {                      # message -> the whole messages its re names
    'Ana1': [], 'Ben1': [], 'Cy1': ['Ana1'], 'Ana2': ['Cy1'], 'Ben2': ['Ana1'], 'Cy2': ['Ana2']}
W6_FACTS = [('Cy1', ['Ana1', 'Ben1']), ('Ana2', ['Cy1']), ('Ben2', ['Ana1', 'Cy1']), ('Cy2', ['Ana2', 'Ben2'])]

def _closure(pairs, names):
    E = set(pairs)
    for n in names:
        s, k = n[:-1], int(n[-1])
        for m in names:
            if m[:-1] == s and int(m[-1]) < k:
                E.add((m, n))
    ch = True
    while ch:
        ch = False
        for (a, b) in list(E):
            for (c, d) in list(E):
                if b == c and (a, d) not in E:
                    E.add((a, d)); ch = True
    return E

W6_NAMES = ['Ana1', 'Ben1', 'Cy1', 'Ana2', 'Ben2', 'Cy2']
W6_E = _closure([(x, y) for y, xs in W6_FACTS for x in xs], W6_NAMES)

def _w6(A):
    got = dict((m.name, m) for m in A if m.name and m.hok)
    return got

def _w6_E(got):
    pairs = []
    for n in W6_NAMES:
        m = got.get(n)
        if m is None:
            continue
        for r in names_in_header(m):
            if r in W6_NAMES and r != n:
                pairs.append((r, n))
    return _closure(pairs, W6_NAMES)

@rub('w6.hdr')
def _(A, C):
    got = _w6(A)
    if set(got) != set(W6_NAMES):
        return False
    for n in W6_NAMES:
        m = got[n]
        others = {'Ana', 'Ben', 'Cy'} - {m.sender}
        if not m.hok or not (set(m.recv) == others or m.recv == ['All']):
            return False
    return True

@rub('w6.pairs')
def _(A, C):
    got = _w6(A)
    return set(got) == set(W6_NAMES) and _w6_E(got) <= W6_E

@rub('w6.all')
def _(A, C):
    got = _w6(A)
    return set(got) == set(W6_NAMES) and W6_E <= _w6_E(got)

@rub('w6.re')
def _(A, C):
    got = _w6(A)
    return set(got) == set(W6_NAMES) and all(sorted(set(got[n].re_names)) == sorted(W6_EXPECT[n]) for n in W6_NAMES)

# ---- W7
LONG = 'east wing cold storage freezer'

def _norm(s):
    return _re.sub(r'\s+', ' ', s.lower()).strip()

def _w7(A):
    return pick(A, 'Kai', 1), pick(A, 'Kai', 2)

def _w7_label(k1):
    """-> (line, label) of the first valid line that defines a label on the full name"""
    for j, t in lines(k1):
        for n in walk(t):
            if n.t == 'str' and n.pre != "'" and _re.fullmatch(r'[ogacnqtd][0-9]+', n.pre or '') and _norm(n.v) == LONG:
                return j, n.pre
            if is_app(n, 'def', 2) and n.args[0].t == 'label' and n.args[1].t == 'str' and _norm(n.args[1].v) == LONG:
                return j, n.args[0].v
    return None, None

@rub('w7.hdr')
def _(A, C):
    k1, k2 = _w7(A)
    return hdr_ok(k1, 'Kai', {'Lena', 'Milo'}, 1) and hdr_ok(k2, 'Kai', {'Lena', 'Milo'}, 2)

@rub('w7.def')
def _(A, C):
    k1, k2 = _w7(A)
    return bool(k1) and _w7_label(k1)[1] is not None

@rub('w7.once')
def _(A, C):
    k1, k2 = _w7(A)
    if not k1:
        return False
    cnt = 0
    for j, t in lines(k1):
        for q in qtexts(t):
            cnt += _norm(q).count(LONG)
    return cnt == 1

@rub('w7.claim')
def _(A, C):
    k1, k2 = _w7(A)
    if not k1:
        return False
    j0, lab = _w7_label(k1)
    if lab is None:
        return False
    for j, t in lines(k1):
        if not plain_claim(t) or has_neg(t):
            continue
        uses = any((n.t == 'label' and n.v == lab) or (n.t == 'str' and n.pre == lab) or (n.t == 'str' and _norm(n.v) == LONG) for n in walk(t))
        zero = 'zero' in toks(t) or any(num(n) == 0 for n in walk(t))
        if uses and zero:
            return True
    return False

@rub('w7.insp')
def _(A, C):
    k1, k2 = _w7(A)
    if not k1:
        return False
    j0, lab = _w7_label(k1)
    if lab is None:
        return False
    for j, t in find(k1, lambda t: is_app(t, 'pls', 2) and agent(t.args[0], 'Lena')):
        for n in walk(t.args[1]):
            if is_app(n, 'by', 2) and n.args[0].t == 'time' and tnorm(n.args[0].v) == '2026-11-06T17:00' and \
                    any(x.t == 'str' and '{%s}' % lab in x.v and tok_has(x, 'inspect') for x in walk(n.args[1])):
                return True
    return False

@rub('w7.none')
def _(A, C):
    k1, k2 = _w7(A)
    return bool(k2) and LONG not in _norm(k2.text)

@rub('w7.ref')
def _(A, C):
    k1, k2 = _w7(A)
    if not (k1 and k2):
        return False
    j0, lab = _w7_label(k1)
    if lab is None:
        return False
    return any(x.t == 'str' and x.pre != "'" and '{Kai1.%s}' % lab in x.v for j, t in lines(k2) for x in walk(t))

@rub('w7.move')
def _(A, C):
    k1, k2 = _w7(A)
    return bool(k2) and bool(find(k2, lambda t: is_app(t, 'pls', 2) and agent(t.args[0], 'Milo') and tok_has(t.args[1], 'move', 'sample')))

# ---- W8
def _w8(A):
    return pick(A, 'Dee', 2)

@rub('w8.hdr')
def _(A, C):
    return hdr_ok(_w8(A), 'Dee', {'Eli', 'Fay', 'Gus'}, 2)

@rub('w8.join')
def _(A, C):
    m = _w8(A)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'join') and any(agent(x, 'Gus') for x in t.args)))

def _w8_ask(t):
    """a line that asks Gus alone to restart the cache"""
    if is_app(t, 'to', 2) and agent(t.args[0], 'Gus') and is_app(t.args[1], 'pls') and tok_has(t.args[1], 'restart', 'cache'):
        p = t.args[1]
        return len(p.args) == 1 or (len(p.args) == 2 and agent(p.args[0], 'Gus', 'You'))
    if is_app(t, 'pls', 2) and agent(t.args[0], 'Gus') and tok_has(t.args[1], 'restart', 'cache'):
        return True
    return False

@rub('w8.ask')
def _(A, C):
    m = _w8(A)
    return bool(m) and bool(find(m, _w8_ask))

@rub('w8.only')
def _(A, C):
    m = _w8(A)
    if not m or not find(m, _w8_ask):
        return False
    for j, t in lines(m):
        if tok_has(t, 'restart', 'cache') and (is_app(t, 'pls') or is_app(t, 'to')) and not _w8_ask(t):
            return False
    return True

@rub('w8.retr')
def _(A, C):
    m = _w8(A)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'retr', 1) and _ref0(t) == 'Dee1.2'))

@rub('w8.clr')
def _(A, C):
    m = _w8(A)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'clr') and _ref0(t) == 'Eli1.1'))

@rub('w8.unit')
def _(A, C):
    m = _w8(A)
    return bool(m) and bool(find(m, lambda t: is_app(t, 'clr', 2) and _ref0(t) == 'Eli1.1' and tok_has(t.args[1], 'unit')))


# ---- scoring of the WRITING part (inlined into the scorer; needs rubric_w, sxc, and the key WK = dict task -> data) ------
import re as _re2

_TASK_HEAD = _re2.compile(r'^[\s#>*_`\-\[\(\|]*(?:task\s*)?W\s*([1-8])(?![0-9])', _re2.I)
_FENCE = _re2.compile(r'^\s*(`{3,}|~{3,})\s*([^`]*)$')

def extract_blocks(text):
    """-> dict 'W1'.. -> list of fenced blocks (strings), assigned by the nearest heading line 'W<n>' before the block
       (or by a task id in the info string of the fence)"""
    out, cur, inb, fch, buf, tid = {}, None, False, '', [], None
    for line in text.replace('\r\n', '\n').split('\n'):
        if inb:
            s = line.strip()
            if s.startswith(fch) and set(s) <= set(fch[0]):
                out.setdefault(tid, []).append('\n'.join(buf)) if tid else None
                inb, buf = False, []
            else:
                buf.append(line)
            continue
        m = _FENCE.match(line)
        if m:
            info = m.group(2).strip()
            mi = _re2.match(r'^(?:task\s*)?W\s*([1-8])\b', info, _re2.I)
            tid = ('W' + mi.group(1)) if mi else cur
            inb, fch, buf = True, m.group(1), []
            continue
        h = _TASK_HEAD.match(line)
        if h and len(line.strip()) < 120:
            cur = 'W' + h.group(1)
    return out

def _has_header_line(b):
    return any(l.strip().startswith('msg(') for l in b.split('\n'))

def _squash(s):
    return _re2.sub(r'\s+', '', s)

def answer_texts(tid, blocks, ctx_texts, loose):
    if loose:
        text = '\n'.join(blocks)
        text = '\n'.join(_re2.sub(r'^\s*\d+[.)]\s+', '', l) for l in text.split('\n'))
        return text
    texts = []
    ctxs = set(_squash(c) for c in ctx_texts)
    for b in blocks:
        for s, t in sxc.split_messages(b):
            t = t.strip('\n')
            if _squash(t) in ctxs:
                continue
            texts.append(t)
    return texts

def loose_msg(text):
    """a pseudo message for loose lines: tree and verdict of every top-level expression, in order"""
    m = Msg()
    m.text, m.index, m.name, m.sender, m.recv, m.serial = text, 0, None, None, [], None
    m.hv, m.hok, m.labels, m.re_names, m.saw_names, m.re_whole = 'ok', True, set(), [], [], []
    items = sxc.parse(text)
    res = sxc.check(text, need_header=False)
    if items and items[0][0] == 'ok' and items[0][1].t == 'app' and items[0][1].v == 'msg':      # a header was added: it is not a line
        items, res = items[1:], res[1:]
    m.trees, m.verd, m.ok, m.src = [], [], [], []
    m.conv_why = {}
    tl = text.split('\n')
    for (kind, x), r in zip(items, res):
        m.trees.append(x if kind == 'ok' else None)
        m.verd.append(r['verdict'])
        m.ok.append(r['verdict'] == 'ok' and kind == 'ok')
        m.src.append('\n'.join(tl[r['line'] - 1:r['last']]).strip())
    return m

def score_task(tid, blocks, K):
    """K: key of the task (dict with context (list of texts), rubric [[id, pts, desc]], loose bool).  -> dict"""
    loose = bool(K.get('loose'))
    ctx = K.get('context') or []
    res = dict(task=tid, got={}, pts=0, max=sum(p for _, p, _ in K['rubric']), lines=0, lines_ok=0, codes={}, problems=[], present=bool(blocks),
               bad=[], notes=[])
    if not blocks:
        for rid, p, d in K['rubric']:
            res['got'][rid] = False
        return res
    if len(blocks) > 1:
        res['notes'].append('%d fenced blocks under this heading (the booklet asks for one)' % len(blocks))
    if not loose:
        msg_blocks = [b for b in blocks if _has_header_line(b)]
        if msg_blocks and len(msg_blocks) < len(blocks):
            res['notes'].append('%d block(s) without a message header were left out' % (len(blocks) - len(msg_blocks)))
            blocks = msg_blocks
        if any(_re2.match(r'^\s*\d+[.)]\s', l) for b in blocks for l in b.split('\n')):
            res['notes'].append('numbered lines inside the block (the booklet asks for none); the numbers were not removed')
    if any(l.lstrip().startswith('#') for b in blocks for l in b.split('\n')):
        res['notes'].append('comment lines inside the block (the booklet asks for none); they do not count as lines')
    at = answer_texts(tid, blocks, ctx, loose)
    if loose:
        m = loose_msg(at)
        A, C, other = [m], [], []
        msgs = [m]
    else:
        msgs, other = build(list(ctx) + at)
        C, A = msgs[:len(ctx)], msgs[len(ctx):]
    for m in A:
        n_l = len(m.ok)
        res['lines'] += n_l + (0 if loose else 1)
        res['lines_ok'] += sum(1 for x in m.ok if x) + (0 if loose else (1 if m.hok else 0))
        for v in m.verd:
            if v != 'ok':
                res['codes'][v] = res['codes'].get(v, 0) + 1
        if not loose and m.hv != 'ok':
            res['codes'][m.hv] = res['codes'].get(m.hv, 0) + 1
    res['problems'] = list(other)
    for m in A:
        nm = m.name or ('line' if loose else '?')
        cw = getattr(m, 'conv_why', {})
        if not loose and m.hv != 'ok':
            res['bad'].append((nm, 'header', m.text.split('\n')[0].strip(), m.hv))
        elif not loose and not m.hok:
            res['bad'].append((nm, 'header', m.text.split('\n')[0].strip(), 'conversation: ' + '; '.join(cw.get(0, ['a problem with the message']))[:200]))
        for j, v in enumerate(m.verd):
            srcj = m.src[j] if j < len(m.src) else ''
            if v != 'ok':
                res['bad'].append((nm, j + 1, srcj, v))
            elif j < len(m.ok) and not m.ok[j]:
                res['bad'].append((nm, j + 1, srcj, 'conversation: ' + '; '.join(cw.get(j + 1, ['a problem with the line']))[:200]))
    for rid, p, d in K['rubric']:
        try:
            ok = bool(RUBRIC[rid](A, C))
        except Exception as e:                      # a malformed answer must not stop the scoring
            ok = False
            res['problems'].append('rubric %s: %s' % (rid, e))
        res['got'][rid] = ok
        if ok:
            res['pts'] += p
    return res


# ------------------------------------------------------------------------------------------------------------------------
# THE READING SCORER
# ------------------------------------------------------------------------------------------------------------------------
# ---- scoring of the READING part (inlined into the scorer) ------------------------------------------------------------
import re as _re3

_QLINE = _re3.compile(r'^[\s>*_\-•`#]*\**\s*Q\s*0*(\d{1,2})\s*\**\s*[:)=.–—\-]\s*(.*)$', _re3.I)
_VERD = _re3.compile(r'\bok\b|\bE\s*[-_‐-―]?\s*(?:SYN|LEX|ARITY|KIND|NAME|REDEF|HEAD|TIME|QUOTE|CODE|MATH)\b', _re3.I)

def parse_sheet(text):
    """-> dict 'Q7' -> (answer text, confidence or None); the last line for a question wins (the final block comes last)"""
    out = {}
    for line in text.replace('\r\n', '\n').split('\n'):
        m = _QLINE.match(line.rstrip())
        if not m:
            continue
        qid, rest = 'Q' + str(int(m.group(1))), m.group(2).strip().strip('`').strip()
        rest = _re3.sub(r'\*\*|__', '', rest)
        conf = None
        if '|' in rest:
            ans, _, tail = rest.rpartition('|')
            mc = _re3.search(r'(\d{1,3})(?:\.\d+)?\s*%?', tail)
            if mc:
                conf = max(0, min(100, int(mc.group(1))))
            else:
                ans = rest
        else:
            mc = _re3.search(r'conf(?:idence)?\s*[:=]?\s*(\d{1,3})', rest, _re3.I)
            ans = rest
            if mc:
                conf = max(0, min(100, int(mc.group(1))))
                ans = rest[:mc.start()]
            else:
                m2 = _re3.search(r'[\s,;(\[]+(\d{1,3})\s*%\s*[)\]]?\s*$', rest) or _re3.search(r'\s\((\d{1,3})\)\s*$', rest)
                if m2:
                    conf = max(0, min(100, int(m2.group(1))))
                    ans = rest[:m2.start()]
        out[qid] = (ans.strip(' ,;'), conf)
    return out

def _norm_verdict(tok):
    t = tok.strip().lower()
    if t == 'ok':
        return 'ok'
    t = _re3.sub(r'[^a-z]', '', t[1:] if t.startswith('e') else t)
    return 'E-' + t.upper()

def normalise(kind, raw, n=None):
    """-> normal form of an answer: 'B' | frozenset of letters | list of lower-case words | None when nothing can be read"""
    if raw is None:
        return None
    raw = raw.strip()
    if kind == 'mc':
        m = _re3.match(r'^\W*([A-Ea-e])(?![A-Za-z0-9])', raw)
        if m:
            return m.group(1).upper()
        m = _re3.search(r'(?<![A-Za-z0-9])([A-E])(?![A-Za-z0-9])', raw)
        return m.group(1) if m else None
    if kind == 'set':
        low = raw.lower()
        if _re3.search(r'\bnone\b|\bno one\b|\bnothing\b', low) and not _re3.search(r'(?<![a-z])[a-h](?![a-z])', _re3.sub(r'\bnone\b|\bnothing\b|\bno one\b', '', low)):
            return frozenset()
        only = _re3.sub(r'[^a-z]', '', low)
        if _re3.fullmatch(r'[a-h]+', only) and _re3.fullmatch(r'[^A-Za-z]*([a-hA-H][^A-Za-z]*)+', raw) and len(only) > 1 and not _re3.search(r'[A-Za-z]{2}', _re3.sub(r'[^A-Za-z]+', ' ', raw).replace(' ', '')[:0]):
            letters = set(only)
        else:
            letters = set(_re3.findall(r'(?<![a-z])([a-h])(?![a-z])', low))
        return frozenset(letters) if letters or low.strip() == '' else None
    if kind == 'verdict':
        toks = [_norm_verdict(t) for t in _VERD.findall(raw)]
        return toks or None
    if kind == 'list':
        toks = _re3.findall(r'[A-Za-z]+[0-9]*(?:\.[0-9]+)?', raw)
        if n and len(toks) == 2 * n and all(len(t) == 1 for t in toks[0::2]):
            toks = toks[1::2]
        out = []
        for t in toks:
            m = _re3.match(r'^([A-Za-z]+)([0-9]+(?:\.[0-9]+)?)$', t)
            out.append((m.group(1).capitalize() + m.group(2)) if m else t.lower())
        return out or None
    return None

def key_form(item):
    a = item['answer']
    if item['kind'] == 'mc':
        return a
    if item['kind'] == 'set':
        return frozenset(a)
    if item['kind'] == 'list':
        return [(x.capitalize() if _re3.match(r'^[A-Za-z]+[0-9]', x) else x.lower()) for x in a]
    if item['kind'] == 'verdict':
        return list(a)
    return None

def score_item(item, got):
    """-> (strict 0/1, partial 0..1)"""
    key = key_form(item)
    if got is None or key is None:
        return 0, 0.0
    k = item['kind']
    if k == 'mc':
        return (1, 1.0) if got == key else (0, 0.0)
    if k == 'set':
        if got == key:
            return 1, 1.0
        return 0, max(0.0, (len(got & key) - len(got - key)) / float(len(key))) if key else 0.0
    n = len(key)
    g = list(got)[:n] + [None] * max(0, n - len(got))
    right = sum(1 for a, b in zip(g, key) if a is not None and str(a).lower() == str(b).lower())
    return (1, 1.0) if (right == n and len(got) == n) else (0, right / float(n))

def score_reading(text, items):
    sheet = parse_sheet(text)
    rows, strict, partial = [], 0, 0.0
    for it in items:
        if it['id'] == 'Z1':
            continue
        raw, conf = sheet.get(it['id'], (None, None))
        got = normalise(it['kind'], raw, len(it['answer']) if it['kind'] in ('list', 'verdict') else None)
        s, p = score_item(it, got)
        rows.append(dict(id=it['id'], part=it['part'], anchor=bool(it.get('anchor')), strict=s, partial=p, conf=conf, raw=raw, got=got,
                         present=raw is not None, chance=it['meta'].get('chance') or 0.0, est=it['meta'].get('est')))
    return rows

def summarise_reading(rows):
    n = len(rows)
    strict = sum(r['strict'] for r in rows)
    anchors = [r for r in rows if r['anchor']]
    core = [r for r in rows if not r['anchor']]
    cal = [(r['conf'] / 100.0, r['strict']) for r in rows if r['conf'] is not None and r['present']]
    parts = {}
    for r in rows:
        d = parts.setdefault(r['part'], [0, 0])
        d[0] += r['strict']; d[1] += 1
    out = dict(n=n, strict=strict, partial=sum(r['partial'] for r in rows),
               anchors=sum(r['strict'] for r in anchors), n_anchors=len(anchors),
               core=sum(r['strict'] for r in core), n_core=len(core),
               missing=[r['id'] for r in rows if not r['present']], parts=parts,
               chance=sum(r['chance'] for r in rows), n_conf=len(cal))
    if cal:
        out['brier'] = sum((c - y) ** 2 for c, y in cal) / len(cal)
        out['mean_conf'] = sum(c for c, y in cal) / len(cal)
        out['acc_conf'] = sum(y for c, y in cal) / len(cal)
        out['high_conf_wrong'] = sum(1 for c, y in cal if c >= 0.8 and y == 0)
        out['high_conf_n'] = sum(1 for c, y in cal if c >= 0.8)
    return out


# ------------------------------------------------------------------------------------------------------------------------
# SHEETS: names, forms
# ------------------------------------------------------------------------------------------------------------------------
_FORM = r'(?:R\+|R-|W\+|R[ _\-]?plus|R[ _\-]?minus|W[ _\-]?plus)'
_NAME_RE = re.compile(r'^(?P<model>.+?)[ _\-]+(?P<form>' + _FORM + r')(?:[ _\-#]*(?P<run>\d+))?$', re.I)
_LABEL_RE = re.compile(r'^(?P<model>.+):(?P<form>' + _FORM + r')(?:#(?P<run>\d+))?$', re.I)

def norm_form(s):
    t = s.lower().replace('plus', '+').replace('minus', '-')
    t = re.sub(r'[^rw+\-]', '', t)
    t = re.sub(r'-(?=[+-])', '', t)
    return {'r+': 'R+', 'r-': 'R-', 'w+': 'W+'}.get(t)

def sheet_id(arg):
    """-> (model, form, run, path)"""
    if '=' in arg:
        lab, _, path = arg.partition('=')
        m = _LABEL_RE.match(lab.strip())
        if m:
            return m.group('model').strip(), norm_form(m.group('form')), int(m.group('run') or 1), path
    stem = os.path.splitext(os.path.basename(arg))[0]
    m = _NAME_RE.match(stem)
    if m:
        return m.group('model').strip(), norm_form(m.group('form')), int(m.group('run') or 1), arg
    raise ValueError('cannot tell the model and the form from the name "%s"; use  Model:Form=path  (Form is R+, R- or W+)' % arg)

def read_text(path):
    with open(path, 'rb') as f:
        return f.read().decode('utf-8-sig', 'replace')

# ------------------------------------------------------------------------------------------------------------------------
# READING: report
# ------------------------------------------------------------------------------------------------------------------------
BY_ID = dict((it['id'], it) for it in READING)

def pick_equal(it, got, pick):
    if got is None:
        return False
    k = it['kind']
    if k == 'mc':
        return got == pick
    if k == 'set':
        return got == frozenset(pick)
    return [str(x).lower() for x in got] == [str(x).lower() for x in pick]

def show(it, v):
    if v is None:
        return '(unreadable)'
    k = it['kind']
    if k == 'mc':
        return str(v)
    if k == 'set':
        return ','.join(sorted(v)) if v else 'none'
    return ', '.join(str(x) for x in v)

def key_text(it):
    a = it['answer']
    if it['kind'] == 'mc':
        return a
    if it['kind'] == 'set':
        return ','.join(sorted(a))
    return ', '.join(a)

def z1_account(text):
    lines = text.replace('\r\n', '\n').split('\n')
    last_q1 = None
    for i, l in enumerate(lines):
        m = _QLINE.match(l.rstrip())
        if m and int(m.group(1)) == 1:
            last_q1 = i
    head = lines[:last_q1] if last_q1 is not None else lines
    zi = None
    for i, l in enumerate(head):
        if re.match(r'^[\s#>*_`\-]*(?:open\s+question[\s:.\-]*)?Z\s*1\b', l, re.I) or re.match(r'^[\s#>*_`\-]*open\s+question', l, re.I):
            zi = i
    if zi is not None:
        head = head[zi:]
    # the fence line that opens the final block (and blank lines) belongs to the block, not to the account
    while head and (not head[-1].strip() or re.match(r'^\s*(?:`{3,}|~{3,})[\w+-]*\s*$', head[-1])):
        head.pop()
    acc = '\n'.join(head).strip()
    return acc[-7000:] if len(acc) > 7000 else acc

def score_reading_sheet(text):
    rows = score_reading(text, READING)
    s = summarise_reading(rows)
    lure, lure_n = [], 0
    for r in rows:
        it = BY_ID[r['id']]
        pk = PICKS.get(r['id'])
        if pk and not pk[1]:
            lure_n += 1
            if not r['strict'] and pick_equal(it, r['got'], pk[0]):
                lure.append(r['id'])
    s['lure'], s['lure_n'] = lure, lure_n
    s['picks_strict'] = KEY['selftest']['picks_strict']
    acc = z1_account(text)
    s['z1_chars'] = len(acc)
    return rows, s, acc

def fmt_pct(a, b):
    return '%d%%' % int(round(100.0 * a / b)) if b else '-'

def report_reading(tag, path, rows, s, verbose):
    o = []
    o.append('[%s]  %s' % (tag, path))
    o.append('  strict %d/%d = %s    core (without the 3 anchors) %d/%d    anchors %d/%d    partial credit %.1f' % (
        s['strict'], s['n'], fmt_pct(s['strict'], s['n']), s['core'], s['n_core'], s['anchors'], s['n_anchors'], s['partial']))
    o.append('  for comparison: a random guesser gets about %.1f; the designer expects about %d from a reader who knows only English' % (s['chance'], s['picks_strict']))
    o.append('  parts: ' + '  '.join('%s %d/%d' % (k, v[0], v[1]) for k, v in sorted(s['parts'].items())))
    if 'brier' in s:
        o.append('  confidence: mean %d%%, accuracy %d%%, Brier %.3f (0.250 = always saying 50), sure (80 or more) on %d answers and wrong on %d of them; numbers given for %d of %d answers' % (
            round(100 * s['mean_conf']), round(100 * s['acc_conf']), s['brier'], s['high_conf_n'], s['high_conf_wrong'], s['n_conf'], s['n']))
    else:
        o.append('  confidence: none found')
    wrong = [r['id'] for r in rows if not r['strict'] and r['present']]
    o.append('  wrong (%d): %s' % (len(wrong), ' '.join(wrong) or '-'))
    o.append('  not found in the reply (%d): %s' % (len(s['missing']), ' '.join(s['missing']) or '-'))
    o.append('  gave exactly the designer\'s expected wrong answer on %d of %d such items: %s' % (len(s['lure']), s['lure_n'], ' '.join(s['lure']) or '-'))
    o.append('  Z1: %s' % ('an account of %d characters found above the final block (mark it by hand)' % s['z1_chars'] if s['z1_chars'] > 40 else 'no account found'))
    if verbose:
        o.append('  item   ok  conf  said -> key')
        for r in rows:
            it = BY_ID[r['id']]
            said = show(it, r['got']) if r['present'] else '(missing)'
            o.append('  %-5s  %s  %4s  %s -> %s%s' % (r['id'], '+' if r['strict'] else '-', ('%d' % r['conf']) if r['conf'] is not None else '', said, key_text(it),
                                                     '' if r['strict'] or r['partial'] == 0 else '   (partial %.2f)' % r['partial']))
    return '\n'.join(o)

# ------------------------------------------------------------------------------------------------------------------------
# WRITING: report
# ------------------------------------------------------------------------------------------------------------------------
_CURLY = {'\u201c': '"', '\u201d': '"', '\u201e': '"', '\u2018': "'", '\u2019': "'"}

def score_writing_sheet(text):
    blocks = extract_blocks(text)
    n_curly = 0
    for tid in blocks:
        fixed = []
        for b in blocks[tid]:
            for k, v in _CURLY.items():
                n_curly += b.count(k)
                b = b.replace(k, v)
            fixed.append(b)
        blocks[tid] = fixed
    res = []
    for t in WRITING:
        res.append(score_task(t['id'], blocks.get(t['id'], []), t))
    if n_curly:
        res[0]['notes'].append('sheet: %d curly quotation marks inside the blocks were replaced by straight ones before checking (a copying effect of some interfaces)' % n_curly)
    return res

def writing_totals(res):
    return dict(pts=sum(r['pts'] for r in res), max=sum(r['max'] for r in res),
                lines=sum(r['lines'] for r in res), lines_ok=sum(r['lines_ok'] for r in res))

def _where(nm, ln):
    """Where a line the checker rejected stands: 'Kai1 line 2', 'Kai1 header', or 'line 6' for lines that have no message."""
    if ln == 'header':
        return '%s header' % nm
    if not nm or nm == 'line':
        return 'line %s' % ln
    return '%s line %s' % (nm, ln)

def report_writing(tag, path, res, verbose):
    tot = writing_totals(res)
    o = []
    o.append('[%s]  %s' % (tag, path))
    o.append('  points %d/%d = %s    lines the checker accepts %d/%d (header lines included)' % (
        tot['pts'], tot['max'], fmt_pct(tot['pts'], tot['max']), tot['lines_ok'], tot['lines']))
    o.append('  per task: ' + '  '.join('%s %d/%d' % (r['task'], r['pts'], r['max']) for r in res))
    codes = {}
    for r in res:
        for c, n in r['codes'].items():
            codes[c] = codes.get(c, 0) + n
    o.append('  verdicts of the checker on the lines that failed: ' + (', '.join('%s x%d' % (c, n) for c, n in sorted(codes.items())) or 'none'))
    absent = [r['task'] for r in res if not r['present']]
    if absent:
        o.append('  no block found for: ' + ' '.join(absent))
    for r in res:
        for n in r['notes']:
            o.append('  note %s: %s' % (r['task'], n))
        for p in r['problems']:
            o.append('  problem %s: %s' % (r['task'], p))
    if verbose:
        for t, r in zip(WRITING, res):
            o.append('  %s %s  %d/%d' % (t['id'], t['title'], r['pts'], r['max']))
            for rid, pts, desc in t['rubric']:
                o.append('     %s %-9s %s' % ('+' if r['got'].get(rid) else '-', rid, desc))
            for nm, ln, src, v in r['bad']:
                o.append('     checker: %s  %s   %s' % (_where(nm, ln), v, (src or '').replace('\n', ' ')[:110]))
    else:
        for r in res:
            for nm, ln, src, v in r['bad'][:3]:
                o.append('  rejected in %s: %s  %s   %s' % (r['task'], _where(nm, ln), v, (src or '').replace('\n', ' ')[:90]))
    return '\n'.join(o)

# ------------------------------------------------------------------------------------------------------------------------
# SELFTEST
# ------------------------------------------------------------------------------------------------------------------------
def fmt_answer(it, ans):
    k = it['kind']
    if k == 'mc':
        return ans
    if k == 'set':
        return ','.join(sorted(ans))
    return ', '.join(ans)

def sheet_from(fn, conf=70):
    lines = []
    for it in READING:
        if it['id'] == 'Z1':
            continue
        lines.append('Q%s: %s | %d' % (it['id'][1:], fmt_answer(it, fn(it)), conf))
    return '\n'.join(lines)

def writing_doc(answers):
    out = []
    for tid in sorted(answers):
        out.append('### %s\n\n```\n%s\n```\n' % (tid, answers[tid].strip('\n')))
    return '\n'.join(out)

def selftest(checker):
    ok = True
    st = KEY['selftest']
    print('SELFTEST')
    rows, s, _ = score_reading_sheet(sheet_from(lambda it: it['answer']))
    good = (s['strict'] == st['perfect'] and s['core'] == st['perfect_core'] and s['anchors'] == 3 and abs(s['partial'] - st['perfect']) < 1e-9)
    print('  reading, a sheet with the key answers: strict %d/%d (expected %d)  ->  %s' % (s['strict'], s['n'], st['perfect'], 'ok' if good else 'FAILED'))
    ok &= good
    rows, s, _ = score_reading_sheet(sheet_from(lambda it: PICKS[it['id']][0]))
    good = (s['strict'] == st['picks_strict'] and s['core'] == st['picks_core'] and s['anchors'] == 3)
    print('  reading, a sheet with the designer\'s expected unaided answers: strict %d/%d, core %d/%d (expected %d and %d)  ->  %s' % (
        s['strict'], s['n'], s['core'], s['n_core'], st['picks_strict'], st['picks_core'], 'ok' if good else 'FAILED'))
    ok &= good
    by = dict((it['id'], it) for it in READING)
    q13 = by['Q13']['answer']
    q17 = ', '.join('(%s) %s' % ('abcde'[i], x) for i, x in enumerate(by['Q17']['answer']))
    q19 = ' '.join((v.replace('-', '_') if i % 2 == 0 else v.upper() if i % 3 == 0 else v.lower()) for i, v in enumerate(by['Q19']['answer']))
    messy = '\n'.join(['preamble Q3: not an answer', '**Q1**: **%s** | 95%%' % by['Q1']['answer'], 'q2: %s (90%%)' % by['Q2']['answer'].lower(),
                       'Q 3) %s, conf 80' % by['Q3']['answer'], 'Q13. %s and %s | 60' % (', '.join(q13[:-1]), q13[-1]), 'Q17: %s | 30' % q17, 'Q19: %s | 10' % q19])
    rows, s, _ = score_reading_sheet(messy)
    got = dict((r['id'], r['strict']) for r in rows)
    good = all(got[q] == 1 for q in ('Q1', 'Q2', 'Q3', 'Q13', 'Q17', 'Q19'))
    print('  reading, a sheet with untidy lines (bold, brackets, percent signs, "and", spaced letters, lower case): %s' % ('ok' if good else 'FAILED'))
    ok &= good
    try:
        load_checker(checker)
    except Exception as e:
        print('  writing: not run (%s)' % e)
        return False
    for n in CHECKER_NOTE:
        print('  ' + n)
    ref = dict((t['id'], t['reference']) for t in WRITING)
    res = score_writing_sheet(writing_doc(ref))
    tot = writing_totals(res)
    good = (tot['pts'] == st['writing_reference'] and tot['pts'] == tot['max'] and tot['lines_ok'] == tot['lines'])
    print('  writing, the reference answers: %d/%d points, %d/%d lines accepted (expected %d)  ->  %s' % (
        tot['pts'], tot['max'], tot['lines_ok'], tot['lines'], st['writing_reference'], 'ok' if good else 'FAILED'))
    ok &= good
    res = score_writing_sheet('')
    tot = writing_totals(res)
    good = tot['pts'] == 0
    print('  writing, an empty reply: %d points  ->  %s' % (tot['pts'], 'ok' if good else 'FAILED'))
    ok &= good
    naive = dict(ref)
    naive['W1'] = ref['W1'].replace('agree(Kai1.3)', 'agree(3)')
    res = score_writing_sheet(writing_doc(naive))
    good = res[0]['pts'] < res[0]['max'] and sum(1 for r in res[1:] if r['pts'] == r['max']) == len(res) - 1
    print('  writing, a damaged W1 loses points and nothing else changes  ->  %s' % ('ok' if good else 'FAILED'))
    ok &= good
    print('SELFTEST %s' % ('PASSED' if ok else 'FAILED'))
    return ok

# ------------------------------------------------------------------------------------------------------------------------
# SUMMARY, Z1 EXPORT, KEY PRINT
# ------------------------------------------------------------------------------------------------------------------------
def summary_table(results):
    models = []
    for r in results:
        if r['model'] not in models:
            models.append(r['model'])
    def cell(model, form, f):
        vals = [f(r) for r in results if r['model'] == model and r['form'] == form]
        return '/'.join(vals) if vals else '-'
    head = ['model', 'R- strict', 'R- core', 'R+ strict', 'R+ core', 'core gain', 'W+ points', 'W+ lines ok']
    rows = []
    for m in models:
        def gain():
            a = [r for r in results if r['model'] == m and r['form'] == 'R-']
            b = [r for r in results if r['model'] == m and r['form'] == 'R+']
            if a and b:
                return '%+d' % (b[0]['s']['core'] - a[0]['s']['core'])
            return '-'
        rows.append([m,
                     cell(m, 'R-', lambda r: '%d/%d' % (r['s']['strict'], r['s']['n'])),
                     cell(m, 'R-', lambda r: '%d/%d' % (r['s']['core'], r['s']['n_core'])),
                     cell(m, 'R+', lambda r: '%d/%d' % (r['s']['strict'], r['s']['n'])),
                     cell(m, 'R+', lambda r: '%d/%d' % (r['s']['core'], r['s']['n_core'])),
                     gain(),
                     cell(m, 'W+', lambda r: '%d/%d' % (r['t']['pts'], r['t']['max'])),
                     cell(m, 'W+', lambda r: '%d/%d' % (r['t']['lines_ok'], r['t']['lines']))])
    w = [max(len(str(x[i])) for x in [head] + rows) for i in range(len(head))]
    out = ['SUMMARY   (reading: strict = all 32 questions, core = the 29 without the anchors; writing: rubric points and checker-accepted lines)']
    out.append('  ' + '  '.join(str(head[i]).ljust(w[i]) for i in range(len(head))))
    out.append('  ' + '  '.join('-' * w[i] for i in range(len(head))))
    for r in rows:
        out.append('  ' + '  '.join(str(r[i]).ljust(w[i]) for i in range(len(head))))
    out.append('  yardsticks: random guesser about %.1f of 32 strict; English-only reader (designer\'s expectation) about %d of 32 strict and %d of 29 core.' % (
        sum(it['meta'].get('chance') or 0.0 for it in READING if it['id'] != 'Z1'), KEY['selftest']['picks_strict'], KEY['selftest']['picks_core']))
    return '\n'.join(out)

def z1_export(prefix, results, seed):
    zs = [r for r in results if r['kind'] == 'R' and r['z1_chars'] > 40]
    rnd = random.Random(seed)
    order = list(range(len(zs)))
    rnd.shuffle(order)
    codes, md = {}, []
    chk = KEY['z1_checklist']
    md.append('# Z1: accounts to mark by hand\n')
    md.append('Mark each account against the nine points below: 1 if the account has the point right, 0 if it is missing or wrong. '
              'The accounts carry codes, not model names. The codes are in %s_codes.json; do not open that file before marking.\n' % prefix)
    md.append('| # | Point |\n| --- | --- |')
    for i, c in enumerate(chk, 1):
        md.append('| %d | %s |' % (i, c.replace('|', '/')))
    md.append('')
    md.append('The message under question:\n\n```text\n%s\n```\n' % KEY['z1_message'])
    for n, i in enumerate(order, 1):
        r = zs[i]
        code = 'Z1-%s' % chr(64 + n) if n <= 26 else 'Z1-%d' % n
        codes[code] = r['tag']
        md.append('## %s\n' % code)
        md.append('```text\n%s\n```\n' % r['z1'].replace('```', "'''"))
        md.append('Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _\n')
    open(prefix + '_marking.md', 'w', encoding='utf-8').write('\n'.join(md))
    json.dump(codes, open(prefix + '_codes.json', 'w'), indent=1)
    return len(zs)

def print_key():
    print('READING KEY (form RB-1, body checksum %s)' % READING_BODY)
    for it in READING:
        if it['id'] == 'Z1':
            continue
        print('  %-4s %s' % (it['id'], key_text(it)))
    print('\nWRITING REFERENCE ANSWERS (form WB-1, body checksum %s); each earns full marks' % WRITING_BODY)
    for t in WRITING:
        print('\n%s %s' % (t['id'], t['title']))
        print(t['reference'].strip('\n'))

# ------------------------------------------------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------------------------------------------------
def jsonable(x):
    if isinstance(x, (set, frozenset)):
        return sorted(x)
    if isinstance(x, tuple):
        return [jsonable(i) for i in x]
    if isinstance(x, dict):
        return dict((str(k), jsonable(v)) for k, v in x.items())
    if isinstance(x, list):
        return [jsonable(i) for i in x]
    return x

def main(argv=None):
    ap = argparse.ArgumentParser(description='SILEX r6.4 blind test: private scorer', add_help=True)
    ap.add_argument('sheets', nargs='*', help='reply files (Model_Rplus.txt, Model_Rminus.txt, Model_Wplus.txt) or Model:Form=path')
    ap.add_argument('--checker')
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--key', action='store_true')
    ap.add_argument('--json')
    ap.add_argument('--csv')
    ap.add_argument('--z1-export', dest='z1')
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args(argv)
    _Checker.explicit = a.checker
    if a.version:
        print(SCORER_VERSION, '| reading body', READING_BODY, '| writing body', WRITING_BODY, '| grammar', GRAMMAR_SHA256[:12], '| checker', CHECKER_SHA256[:12])
        return 0
    if a.key:
        print_key()
        return 0
    if a.selftest:
        return 0 if selftest(a.checker) else 1
    if not a.sheets:
        ap.print_help()
        return 2
    results, errors = [], []
    for arg in a.sheets:
        try:
            model, form, run, path = sheet_id(arg)
        except ValueError as e:
            errors.append(str(e)); continue
        if not os.path.isfile(path):
            errors.append('file not found: %s' % path); continue
        text = read_text(path)
        tag = '%s %s%s' % (model, form, '' if run == 1 else ' #%d' % run)
        if form in ('R+', 'R-'):
            rows, s, acc = score_reading_sheet(text)
            if s['n'] and len(s['missing']) == s['n']:
                errors.append('%s: no answer lines of the form "Q7: B | 80" were found in %s' % (tag, path))
            results.append(dict(kind='R', model=model, form=form, run=run, tag=tag, path=path, rows=rows, s=s, z1=acc, z1_chars=s['z1_chars']))
        else:
            try:
                load_checker(a.checker)
            except Exception as e:
                errors.append('%s: %s' % (tag, e)); continue
            res = score_writing_sheet(text)
            if not any(r['present'] for r in res):
                errors.append('%s: no fenced block under headings W1 to W8 was found in %s' % (tag, path))
            results.append(dict(kind='W', model=model, form=form, run=run, tag=tag, path=path, res=res, t=writing_totals(res)))
    for n in CHECKER_NOTE:
        print(n + '\n')
    for r in results:
        if r['kind'] == 'R':
            print(report_reading(r['tag'], r['path'], r['rows'], r['s'], a.verbose))
        else:
            print(report_writing(r['tag'], r['path'], r['res'], a.verbose))
        print()
    if len(results) > 1:
        print(summary_table(results))
        print()
    if a.json:
        out = []
        for r in results:
            d = dict((k, v) for k, v in r.items() if k not in ('z1',))
            out.append(jsonable(d))
        json.dump(dict(scorer=SCORER_VERSION, sheets=out), open(a.json, 'w'), indent=1)
        print('wrote', a.json)
    if a.csv:
        with open(a.csv, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['model', 'form', 'run', 'file', 'strict', 'of', 'core', 'of_core', 'anchors', 'partial', 'brier', 'mean_conf', 'high_conf_wrong', 'lure', 'points', 'max_points', 'lines_ok', 'lines'])
            for r in results:
                if r['kind'] == 'R':
                    s = r['s']
                    w.writerow([r['model'], r['form'], r['run'], r['path'], s['strict'], s['n'], s['core'], s['n_core'], s['anchors'], '%.2f' % s['partial'],
                                '%.3f' % s['brier'] if 'brier' in s else '', '%.2f' % s['mean_conf'] if 'mean_conf' in s else '', s.get('high_conf_wrong', ''), len(s['lure']), '', '', '', ''])
                else:
                    t = r['t']
                    w.writerow([r['model'], r['form'], r['run'], r['path']] + [''] * 10 + [t['pts'], t['max'], t['lines_ok'], t['lines']])
        print('wrote', a.csv)
    if a.z1:
        n = z1_export(a.z1, results, a.seed)
        print('wrote %s_marking.md (%d accounts) and %s_codes.json' % (a.z1, n, a.z1))
    for e in errors:
        print('ERROR:', e, file=sys.stderr)
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
