# SILEX r6.4 — a language for AI agents that talk to one another

**What this is.** SILEX is a formal language for messages between AI agents. A message says who sends it and who receives it, and then says things: claims, questions, requests, promises. Every line is one bracket form `root(arg, arg)` (or a formula in single quotes, 1.4.6) that a program can check and an agent can read without guessing. Any number of agents can talk at the same time. The language says how to tell which message came after which, and what to do when messages cross.

**Contents.** Part 0 Read this first · Part 1 The shape of a message · Part 2 Many agents at once · Part 3 The roots · Part 4 Cookbook: how do I say …? · Part 5 Limits and open choices · Part 6 How this file was checked · Appendix Word index.

---

## Part 0. Read this first

### 0.1 A message

```silex
msg(Ana,Ben,Cy,1)                             # ok — header: Ana writes to Ben and Cy; this is Ana's message number 1
pls(Ben,"run smoke test")                     # ok — Ana asks Ben to run the smoke test
pls(Cy,"run full regression suite")           # ok — Ana asks Cy to run the full regression suite
must(by(2026-11-06T17:00,fin("smoke test")))  # ok — the smoke test must be finished by Friday 5 pm
```

The first line is the **header**. Every other line is a **claim**, a **question** or a **speech act** (a request, a promise, an answer and so on). English words go inside quotes: a quote **names** a thing, an act or a property, and the root around it says what is claimed about it. Everything else (not, if, all, by, must, how many, when) is a root.

### 0.2 Two replies that cross

Ben and Cy answer at the same moment; neither has seen the other's answer.

```silex
msg(Ben,Ana,Cy,1,re(Ana1))  # ok — Ben to Ana and Cy; replying to Ana1
will("run smoke test")      # ok — Ben promises to run it
```

```silex
msg(Cy,Ana,Ben,1,re(Ana1))                                              # ok — Cy to Ana and Ben; replying to Ana1 as well
rej("run full regression suite",not(may(Me,"write to job scheduler")))  # ok — Cy declines: Cy may not write to the job scheduler
```

`re(Ana1)` says which message each one answers. Neither header names the other's message, so the two are **concurrent**: no reader may assume that Ben knew what Cy wrote. Ana's next message names both (`saw(Ben1,Cy1)`) and then it is clear that she has read both. Part 2 gives the rules.

### 0.3 The six ideas

1. **One header, then lines.** `msg(from, to, …)` names the sender and the receivers; a serial number, a send time and the details `re(…)`, `saw(…)`, `pri(…)` may follow.
2. **One line, one form.** A line is `root(arg, arg, …)`, or a formula in single quotes (1.4.6). Outside a formula there are no operators and no precedence, and no punctuation except brackets, commas and quotes. A line never runs over onto the next.
3. **Roots carry the structure.** About 100 roots say logic (`not and or if`), quantity (`all some none many over cnt`), time (`at before after by during`), modality (`must can want`), belief (`bel know prob unk`), questions (`yn what which why`) and speech acts (`pls will rej sug agree ans`).
4. **English carries the content.** A quote such as `"production servers"` is a **scaffold**: English that names what the root is about. A scaffold fixes nothing else; the roots around it do all the logic. Where a root would be wasted on a plain phrase, the phrase stays English. Any claim at all can also be written whole as `q"…"` (1.4.5), so nothing is unsayable; but a root that says it should be used. Two things carry text that is not English, exactly as it is written: a program (the root `code`) and a formula (a quote in single marks, as in `'x^2-5*x+6=0'`) (1.4.6).
5. **Kinds keep lines honest.** Every place in a root takes a *kind* (agent, thing, group, act, number, time, criterion, claim, …). A program can say whether a line is well formed (`ok`) or which rule it breaks (`E-KIND`, `E-ARITY` …) without understanding a word of the English.
6. **No clock is shared.** Agents do not see messages in one order. Only serials, `re` and `saw` give an order, and where they give none the messages are concurrent.

### 0.3.1 Rulings kept from the Owner

Roots are plain-English words shortened where long (`hyp`, `cnt`); the bracket form `root(arg, …)` is the only form for a root (a formula in single quotes is a value, 1.4.6); a scaffold has no "the" (*"production servers"*, not *"the production servers"*; "a" and "an" stay); the header `msg(from, to)` stays; fewer tokens with no loss of meaning; a line reference is written `Ana3.2`, or as a bare number after `re` (1.5.5), with no shorter spelling for the sender's own lines or for runs of lines.

### 0.4 What the numbers are

| | English | SILEX |
| --- | --- | --- |
| The 84 test sentences (Part 4), one line each, header left out (cl100k tokens) | 700 | 955 (1.36×) |
| The same sentences, eight to a message, headers counted | 701 | 1,042 (1.49×) |

The count is a close estimate, not the bill: the three tokenizers used (two OpenAI vocabularies and an older Anthropic one) are not the tokenizer of a current Claude model. Part 6 says how.

### 0.5 How to read the code in this file

A fenced block marked `silex` is **one message**: its first line is the header. A block marked `sx` is a few loose lines whose header is not shown. The comment after `#` on each line begins with the verdict of the checker (`ok`, or the error code) and then says in English what the line means. A line that says `E-…` is wrong on purpose: it shows the error. Comments are for this file only; real messages carry none.

---

## Part 1. The shape of a message

### 1.1 Messages and lines

A **message** is a few lines of text. The first line is the **header** `msg(from, to, …)` (2.2). Every other line holds one expression and says one thing.

- One line is one expression. A line never continues on the next: every bracket closes on the line it opens (`E-SYN` otherwise).
- Blank lines are ignored. `#` outside a quote starts a comment that runs to the end of the line; comments do not count as lines and real messages carry none.
- White space outside quotes means nothing. The shortest form has none: `is("server","patched")`. Spaces after commas cost tokens (measured, 6.2) and add no meaning.
- The first line after the header is line 1. `Ana3.2` is line 2 of message `Ana3` (2.2). The header is never a line: in a message of a header and four lines, the lines are 1, 2, 3 and 4, not 2, 3, 4 and 5. A writer who counts the header sends every reference one too high, and it still passes the checker when that line exists (6.5).

### 1.2 The ten forms of an expression

| Form | Written | Kind |
| --- | --- | --- |
| application | `is("server","patched")` | what the root returns (Part 3) |
| atom | `now` `yes` `no` `hi` `mid` `lo` `_` | per atom (1.7) |
| agent | `Ana` `Bob` `Me` `You` `All` | Ag |
| quote | `"production servers"` `g"…"` `o1"…"` | by place or class letter (1.4); raw text in `code` (1.4.6) |
| formula | `'x^2=4'` `'x>0 & x<10'` `'2^10-1'` | `Cl` with a comparison, else `Nu`; raw text (1.4.6) |
| label | `o1` `g2` | by class letter (1.5) |
| number | `12` `0.95` `-3` | Nu (a whole number in the first place of `agree ans err clr rej unk` can be a line, 1.5.5) |
| time | `2026-11-06T17:00` `20261106T1700` `2026-11-06` `2026-11-03T22:00/2026-11-04T06:00` | Tm |
| duration | `PT20M` `P1D` | Du |
| reference | `Ana3` `Ana3.2` `Ana3.o1` | Rf (a label: its own kind) |

**Spelling.** A root is lower-case letters only (`cnt`, `during`); it is followed at once by `(`. An agent is a capital and lower-case letters (`Ana`, `Cy`). A message name is an agent and a number (`Ana3`). A label is one class letter and digits (`o1`). A lower-case word that is not a root or an atom is `E-LEX`; a root with no bracket is `E-ARITY`; the error message names the nearest roots. A formula is written between single quote marks and holds no quote mark.

### 1.3 Kinds and places

Every place of every root takes a kind. A checker needs nothing else to give a verdict.

| Kind | What it is | Example |
| --- | --- | --- |
| `Ag` | an agent | `Ana` `Me` `All` |
| `Th` | a thing: an object, person, place, event, anything talked about as one | `"web server"` |
| `Gr` | a group of things | `"production servers"` `grp(a,b)` |
| `Ac` | an act | `"run smoke test"` `code("bash","make")` |
| `Nu` | a number | `12` `cnt(g)` `hi` |
| `Tm` | a time | `2026-11-06` `now` |
| `Du` | a duration | `PT20M` |
| `Cr` | a criterion: the name of a property or a relation | `"patched"` `"depends on"` |
| `Cl` | a claim: something that is true or false | `is(…)` |
| `Q` | a question | `yn(…)` |
| `Ln` | a line: a claim, a question or a speech act | `pls(…)` |
| `Rf` | a reference to a message or one of its lines | `Ana3` `Ana3.2` |
| `Va` | any value: every kind above except `Q` and `Ln` | |

Eight more kinds are named in the tables of Part 3 and nowhere else:

| Kind | What it is | Example |
| --- | --- | --- |
| `X` | a place that takes a claim, an act or a line | the second place of `if` and of `at` |
| `Vr` | a new label that the root binds, for use inside its other place | `o1` in `crit(o1,P)` |
| `Nm` | a new label that the root defines | `g1` in `def(g1,…)` |
| `Hd` | a part of a header: `msg`, or a detail `re`, `saw`, `pri` | `re(Ana1)` |
| `An` | an answer to a yes-or-no question | `yes` `no` |
| `Dg` | a degree | `hi` `mid` `lo` |
| `Un` | unspecified | `_` |
| `Rw` | a plain quote carried as it is, not read as English | the lines of `code(…)` |

How a kind fits a place: an `Ag` fits a `Th` place; a `Cl` or a `Q` fits an `Ln` place; a `Dg` fits a `Nu` place; an `An` fits a `Va` place; a value that is looked up (`val`, `func` and `best` give `Va`) has a kind that only the thing decides, so it fits any place that takes a number, time, duration, group, thing or criterion; `_` fits every place; `Cl|Ac` is a place that takes either. An `Rf` fits any place that takes a claim, a question, a line or a value: it stands for what that message or line says; in the first place of `ent` one `Rf` that names a line stands for the premises (3.10). In the first place of six roots a bare whole number is read as an `Rf` (1.5.5). A place written in square brackets, `[Cr]`, may be left out; a place written `Cl…` takes one or more.

### 1.4 Quotes

#### 1.4.1 What a quote is

A **quote** is English between double quotation marks. It **names** something: a thing, a group, an act, a property, a time. It is also called a **scaffold**, because the roots stand on it. A quote is written where it is used, and the same quote used twice in a message names the same thing.

```sx
all("production servers","patched")  # ok — every member of the group "production servers" is a "patched" one
will("run smoke test")               # ok — the quote is an act here: the sender promises to do it
over(cnt("production servers"),10)   # ok — the group "production servers" has more than 10 members
```

#### 1.4.2 What kind a quote has

The place decides. A bare quote needs no class letter where the place leaves no doubt.

| The place takes | A bare quote there is |
| --- | --- |
| only `Gr`, `Ac`, `Cr`, `Nu`, `Tm` or `Du` | that kind |
| `Th` or `Va` | a thing |
| `X` (claim, act or line) | an act |
| several kinds | the first that fits of: act, time, thing |
| only `Cl`, `Q`, `Ln`, `Rf` or `Ag` | not allowed (`E-KIND`) |

A root with several forms (`plus`, `minus`, `avg`, `max`) takes the form that makes the line fit. In `all(minus("servers","staging server"),"patched")` (4.10) `all` needs a group, so `minus` is its group form and its quotes are a group and a thing. When more than one form fits, the English decides, or a class letter says: `minus(g"servers","staging server")`.

```sx
is("server","patched")                        # ok — first place takes any value: "server" is a thing; second takes a criterion: "patched" is one
if(is("build","failed"),pls("notify {Ana}"))  # ok — pls takes an act, so "notify Ana" is an act
at("Friday 5 pm",fin("backup"))               # ok — the first place takes a time or a claim: a bare quote is a time
all(g"servers",c"patched")                    # ok — the same as all("servers","patched"): the letters only say it again
cause("cache layer","outage")                 # ok — cause takes any value: two things
not(q"cache is empty")                        # ok — a claim written whole in English needs q
all("production servers",12)                  # E-KIND — a number is not a criterion
```

#### 1.4.3 Class letters

A **class letter** in front of a quote states the kind. It is needed where the rule above gives the wrong kind or none.

| Letter | Kind | Example |
| --- | --- | --- |
| `o` | thing | `o"server in rack 4"` |
| `g` | group | `g"production servers"` |
| `a` | act | `a"run check"` |
| `n` | number | `n"queue length"` |
| `c` | criterion | `c"patched"` |
| `q` | claim | `q"cache is empty"` |
| `t` | time | `t"Friday 5 pm"` |
| `d` | duration | `d"about a day"` |

#### 1.4.4 Claims in English: the hatch

`q"…"` writes a whole claim in English. It is the **hatch** that makes every claim sayable: whatever the roots cannot say, `q"…"` carries as English. It is not wrong, but it hides structure from a checker and from a reader who works on structure; use it only where no root says the thing. `E-KIND` is given when a bare quote stands where only a claim fits, so the hatch is always a visible choice.

#### 1.4.5 What goes inside a quote

- **No "the"** (the Owner's ruling): *"production servers"*, not *"the production servers"*. "A" and "an" stay, so that *a server* is not *the server*. A quote with "the" in it is `E-QUOTE`. The raw quotes of `code` and a formula in single quotes (1.4.6) are the exception.
- **No word whose meaning depends on who speaks or when**: no *I, me, you, we, my, this, here, today, yesterday, tomorrow*. Write `{Me}`, `{You}`, `{Ana}` or a date (`2026-11-03`). Such a word is `E-QUOTE`.
- **References in braces.** `{o1}`, `{Ben5.o1}`, `{Ana}`, `{Me}`, `{12}`, `{2026-11-06}` and `{PT5M}` inside a quote stand for that name, agent, number, time or duration, so the English can mention what the line already names. A label must be defined before it is used. A literal brace is doubled: `{{` `}}`. Any other brace is `E-QUOTE`.
- **A quote mark inside a quote is doubled**: `"say ""ok"""`.
- **Tense and time** stay in the English when they are not the point (*"restart service"*) and go into a time root when they are (`by(2026-11-06,…)`).

```sx
pls(Ben,"send logs of 2026-11-03 to {Me}")  # ok — {Me} is the sender, whoever reads the line later
pls(Ben,"restart {o9")                      # E-QUOTE — a single brace
```

**Look for *the* before sending.** It is the commonest slip (both test writers made it, 6.9), and it hides in short phrases: *the caller*, *the two*, *keep the raise form*. Write *caller*, *both*, *keep raise form*. The rule holds for `q"…"` as well.

```sx
pls(Ben,"restart service")        # ok — no article
pls(Ben,"restart the service")    # E-QUOTE — a quote with the
will("keep raise form")           # ok
will("keep the raise form")       # E-QUOTE — the
```

#### 1.4.6 Text that is not English: programs and formulas

A program and a formula carry text exactly as it is written, because the English rules above would break it. Inside `code(…)` and inside a formula the text is **raw**: the rules of 1.4.5 do not apply (a program may say *the*, *my* or *this*, and may use braces), and nothing in it is read as a reference. A quote of `code` is a plain quote, with no class letter and no label, and a quote mark inside it is doubled (`""`). A formula holds no quote mark at all.

**A program: `code(language, line, line …)`.** The first quote names the language and each other quote is one line of the program, with its indentation. The language is one of `python javascript typescript bash sql json yaml html css c cpp java go rust diff text`; any other is `E-CODE`. For Python the checker reads the syntax too: the lines, with any indentation they all share taken off, must parse as Python 3, or the line is `E-CODE`. A part of a program can be sent (a loop body, indented as a whole) if it parses on its own; `else:` alone does not. The other languages are carried as they are. A program is the act of running it, so `code(…)` has the kind of an act (`Ac`): `pls(Ben,code(…))` asks Ben to run it and `will(code(…))` promises to. To send a program without asking for anything, or to point at it later, name it with `def`: `def(a1,code(…))` is a line, `a1` stands for the program in this message, `{a1}` inside a quote reaches it (`"review {a1}"`), and `Ana3.a1` reaches it from another message.

**A formula: `'formula'`.** A formula stands between single quote marks, in the usual written form, in ASCII. It is a value in its own right, with no root round it: its kind is `Cl` when it is a claim and `Nu` when it is a number.

| Part | Written |
| --- | --- |
| numbers | `12` `0.5` `1e-3`: digits on both sides of a point |
| names | letters, digits and `_`, beginning with a letter: `x` `x_1` `alpha` |
| operators | `+ - * / ^` and round brackets. `^` is a power and groups to the right (`2^3^2` is `2^(3^2)`); `-x^2` is `-(x^2)`; `*` is never left out (`2*x`, not `2x`) |
| functions | a name and a bracket: `f(x)` `sqrt(x)` `sum(i^2,i,1,n)`. The names in 3.3 have an agreed meaning; any other name is the writer's own function. The arguments are numbers |
| comparison | one of `=` `!=` `<` `>` `<=` `>=`, once in each claim |
| joining claims | `&` and, `\|` or, `=>` if, `<=>` if and only if. Round brackets group. From the tightest: the arithmetic, a comparison, `&`, `\|`, `=>`, `<=>` |

**Joining claims.** `a=1 & b=2 | c=3` is `(a=1 & b=2) | c=3`, because `&` binds tighter than `|`. `&` and `|` may be repeated (`a=1 & b=2 & c=3`). `=>` and `<=>` take exactly two claims: a chain such as `a=1 => b=2 => c=3` reads two ways (*if a then if b then c*, or *a gives b and b gives c*), so it is `E-MATH` and needs brackets. Each side of a join is a claim, so `x & y` is `E-MATH` (a name alone is a number), and so are `x=>3` (greater or equal is `>=`) and `|x|` (an absolute value is `abs(x)`). There is no sign for *not* inside a formula: use `!=` `<` `>` `<=` `>=`, or put `not(…)` round the whole formula. The words *and*, *or* and *if* are ordinary names in a formula, so they cannot stand between claims (`E-MATH`).

A formula is a claim (`Cl`) when it has a comparison or joins claims, and can be a line; a formula without one is a number (`Nu`) and cannot be a line (`E-KIND`). A formula is checked for form, not for truth: `'2+2=5'` is `ok`. A name in a formula is free: two uses of it in a message mean one thing, as two uses of a quote do (1.4.1). A claim on a line by itself is asserted, as any claim line is (1.8); to offer a formula without asserting it, put it in `hyp(…)`, `assume(…)`, `if(…)`, `bel(…)` or another root that mentions a claim (4.13). The other roots join formulas with claims in English: `and('x>0',is("x","real"))`. A formula on a line of its own is the one line that is not `root(…)` (5.2, item 18).

Neither a program nor a formula runs or solves anything. SILEX gives no authority (5.1): a receiver decides whether to run what it receives, and where.

```sx
will(code("python","def add(a,b):","    return a+b"))   # ok — the sender promises to run a two-line program
pls(Ben,code("python","d = {1: 2}","print(f""{d}"")"))  # ok — braces and quote marks in a program are raw
def(a1,code("bash","make","make test"))                 # ok — a1 names the program for the rest of this message
will(code("python","def f(:"))                          # E-CODE — python does not read this
will(code("cobol","DISPLAY 1"))                         # E-CODE — the language is not on the list
code("python","x = 1")                                  # E-KIND — an act alone is not a line
'x^2-5*x+6=0'                                           # ok — a claim: the formula has a comparison
eq('2^10-1',1023)                                       # ok — a number inside a claim
'x>0 & x<10'                                            # ok — two claims joined: x is between 0 and 10
'x=2 | x=3'                                             # ok — x is 2 or x is 3
'x>0 => x^2>0'                                          # ok — if x is positive, x squared is positive
'x^2=4 <=> x=2 | x=-2'                                  # ok — x squared is 4 if and only if x is 2 or -2
'(x=1 | x=2) & y=3'                                     # ok — brackets group: x is 1 or 2, and y is 3
math("x^2-5*x+6=0")                                     # E-LEX — there is no root math: a formula stands in single quotes
'2x=4'                                                  # E-MATH — write 2*x
'x^2-'                                                  # E-MATH — the formula ends where more is needed
'x>0 and x<5'                                           # E-MATH — write &, not the word and
'x=1 => y=2 => z=3'                                     # E-MATH — a chain of => reads two ways: use brackets
'x & y'                                                 # E-MATH — a join needs claims, and x is a number
'x+1'                                                   # E-KIND — a number alone is not a line
```

### 1.5 Names

#### 1.5.1 Labels

A **label** is one class letter and digits (`o1`, `g2`, `a3`). It is defined by the first quote that carries it, and is used by itself afterwards. The label's letter is its kind.

```sx
and(is(o1"server in rack 4","patched"),is(o1,"tested"))    # ok — o1 is defined at its first use, then used by itself
is(o2,"patched")                                           # E-NAME — o2 was never defined in this message
and(is(o1"web server","up"),is(o1"database server","up"))  # E-REDEF — a second quote cannot reuse the label o1
```

A label is never needed to say the same thing twice, because the same quote means the same thing (1.4.1); it only shortens a long phrase that comes back. Use a label for a phrase of five words or more that occurs again.

#### 1.5.2 Variables

`crit(o1, P)` and `which(o1, P)` **bind** a new label `o1` for use inside `P`, and nowhere else. This is how a line talks about "an x such that …".

```sx
all("servers",crit(o1,is(o1,"hosts","payment service")))  # ok — every server is one that hosts the payment service
which(o1,and(mem(o1,"tests"),is(o1,"failed")))            # ok — which test is a failed one?
```

#### 1.5.3 `def`

`def(label, expression)` gives a name to any expression, so that later lines can use it. The label's letter must fit the expression's kind.

```sx
def(g1,filt("servers","patched"))  # ok — g1 stands for the patched servers
many(g1)                           # ok — g1 has many members
def(n1,g1)                         # E-KIND — n1 is a number name, g1 is a group
```

#### 1.5.4 Labels and lines in other messages

A label belongs to the message that defines it. Another message reaches it as `Ana3.o1`, and a line as `Ana3.2`. This is the only way names travel; there are no names shared by a whole conversation, because under concurrent talk two agents could define one name at once (2.6). **A reference to a line is checked wherever it stands**: in `agree(Ana3.2)`, and also in `ent(Ana3.2,…)` or `grp(Ana3.1,Ana3.2)`, it must name an earlier message or the sender's own, and a line that message has.

```sx
pls(Ben,"reboot {Ana3.o1}")  # ok — inside a quote: the thing Ana named o1 in her message 3
agree(Ana3.2)                # ok — I agree with line 2 of Ana3
```

#### 1.5.5 Line numbers without the name

When the header's `re` names exactly one message, and it is a whole message (`re(Ana1)`, not `re(Ana1.2)`), a bare whole number in the first place of `agree`, `ans`, `err`, `clr`, `rej` or `unk` is a line of that message: `agree(2)` is `agree(Ana1.2)`. It is a second spelling of the same reference. A program expands one into the other, the message means what its full form means, and it still follows Ana1 (2.3).

- It stands only in the first place of those six roots. Everywhere else a number is a number: in `ans(1,12)` the `12` is the answer and the `1` is a line; `over(3,2)` compares numbers.
- It is a whole number from 1. `agree(0)`, `agree(2.5)` and `agree(-1)` are `E-KIND`.
- `re` names exactly one message, and not a line of one. With two names, a line name, or no `re` (a `saw` does not count), the number is `E-KIND`: write the reference in full.
- Lines of any other message, and the sender's own lines, are written in full. `retr` and `ack` have no short form: they point at the sender's own lines or at whole messages. `ack(Ana1)` is right; `ack(2)` is `E-KIND`. The same holds in every other root: `ent(Ben1.8,…)` names the sender's own line 8 in full, and there is no shorter spelling (a leading dot, or a run such as `Ben1.5-7`); the Owner ruled so on 5 November, because a shortened number is easier to misread than a full one (5.2, item 20).

```dialogue
msg(Ana,Ben,Cy,1)                # ok — Ana's 1
yn(is("build","green"))          # ok — line 1: a question
is("disk","full")                # ok — line 2: a claim
---
msg(Ben,Ana,1,re(Ana1))          # ok — re names one whole message
ans(1,yes)                       # ok — the same as ans(Ana1.1,yes)
agree(2)                         # ok — the same as agree(Ana1.2)
---
msg(Cy,Ana,Ben,1,re(Ana1,Ben1))  # ok — re names two messages
agree(2)                         # E-KIND — which message? write Ana1.2
agree(Ana1.2)                    # ok — in full
```

### 1.6 Numbers, times and durations

- **Numbers** are written with a decimal point and no separators: `12`, `0.95`, `-3`. A percentage is the number and the word *percent* in the name (`n"pass rate in percent"`) or `pct(a,b)`. A probability is between 0 and 1.
- **Times** follow ISO 8601: a date `2026-11-06` (the whole day), a date and time `2026-11-06T17:00` (add seconds, or `Z`, or an offset such as `+05:30`, where the zone matters), and an interval of two times `2026-11-03T22:00/2026-11-04T06:00` (the first not after the second). A time without a zone is in the zone the agents have agreed. An impossible time is `E-TIME`.
- **Compact date-times.** ISO 8601 also has a form without hyphens and colons: `20261106T1700` is `2026-11-06T17:00`; `20261106T170030` adds seconds and `20261106T1700+0530` an offset. The two spellings are the same time, either may stand wherever a time stands (even the two ends of one interval), and a program turns one into the other. The short one saves about 4 tokens a time (6.7). The `T` is required: a date alone is written `2026-11-06`, because `20261106` is a number.
- **An instant or a stretch.** A time with a clock part (`T17:00`) is an instant. A date alone is the whole day, and an interval is a stretch. A time root with a stretch reads the same way throughout: `at(stretch, X)` says X holds all through it, and `during(stretch, X)` says X happens at some time within it (3.9).
- **Durations** follow ISO 8601: `PT20M`, `P1D`, `P2W`, `P1DT2H`.
- `now` is the time at which the message was sent. A header that carries a send time (2.2) fixes it; otherwise it is the unspecified moment of sending.
- A time not known exactly is a time quote: `t"Friday 5 pm"`. When the date is known, write the date: a reader should never have to compute *Friday*.

```sx
by(2026-11-06T17:00,fin("smoke test"))                    # ok — a date and a time
during(2026-11-03T22:00/2026-11-04T06:00,fin("restart"))  # ok — an interval: last night
at(2026-13-40,fin("backup"))                              # E-TIME — there is no month 13
by(20261106T1700,fin("smoke test"))                       # ok — the same time as 2026-11-06T17:00
during(20261103T2200/20261104T0600,fin("restart"))        # ok — an interval in the short form
at(20261306T1700,fin("backup"))                           # E-TIME — there is no month 13 in this spelling either
at(20261106,fin("backup"))                                # E-KIND — 20261106 is a number, not a date
for(PT3H,is("service","down"))                            # ok — a duration
```

### 1.7 The atoms

An **atom** is a word that stands alone, with no bracket.

| Atom | Kind | Meaning |
| --- | --- | --- |
| `Me` | Ag | the sender of this message |
| `You` | Ag | each receiver of this message; inside `to(…)`, each agent that line is for |
| `All` | Ag | every agent on the roster except the sender (2.4) |
| `now` | Tm | the time this message was sent |
| `yes` `no` | An | the two answers to a yes-or-no question (fits a value place) |
| `hi` `mid` `lo` | Dg | a high, middle or low degree: for a probability or a priority |
| `_` | Un | unspecified: a value that is not given (*someone*, *something*, *somehow*) |

A name such as `Ana` is an agent atom too: any capitalised word is an agent, whether or not it is on the roster. `Me`, `You` and `All` are reserved.

### 1.8 What a line is

- A **line** is a claim, a question or a speech act (kinds `Cl`, `Q`, `Ln`). A value alone (`12`, `"server"`, `cnt(g)`) is not a line (`E-KIND`).
- A **claim line asserts**: the sender says it is so. The same claim inside another root is **mentioned**, not asserted: `bel(Me,P)` asserts only that the sender believes `P`; `if(P,Q)` asserts neither `P` nor `Q`; `say(Bob,P)` asserts that Bob said it. This is how SILEX tells *I say* from *he says* from *suppose*. The rule holds for every root that takes a claim (`supp`, `ent`, `would`, `prob`, `want`, `plan`, `must`, `can`, and the rest) with two exceptions, because the English words are factive: `know(x,P)` also asserts `P`, and `cause(P,Q)` asserts `P` and `Q` as well as the link between them. For a link that is only possible or imagined, use `if` or `would`.
- A **speech act** (`pls will rej sug agree ans unk hyp assume retr ack err clr join leave`) does its act and asserts only what its own reading says (2.5).
- **Time.** A claim that no time root wraps holds at `now`. Two roots place themselves: `fin(A)` with no time root says A *has finished* (at or before `now`), and `say(x,P)` with no time root does not say when x spoke (put a time root round it: `before(now,say(Bob,P))`). A claim used as a time, as in `after(fin("migration"),…)`, is not asserted: it only gives the time. Tense and dates inside a quote are read as English; when a time matters, use a time root and an ISO time.

```sx
bel(Me,cause("cache layer","outage"))         # ok — asserts that the sender believes it; asserts nothing about the cause
if(is("build","failed"),pls("notify {Ana}"))  # ok — asserts the conditional request; neither the failure nor the request alone
12                                            # E-KIND — a value is not a line
```

### 1.9 Verdicts

A checker gives each line one verdict. `ok` means the line is well formed: its roots are roots, its places have the right kinds, its names are defined. It does not mean the line is true, or that the English in its quotes says what the writer meant.

| Verdict | Meaning | Example |
| --- | --- | --- |
| `ok` | well formed | `is("server","patched")` |
| `E-SYN` | the line is not an expression, or a bracket or a quote is open at the end of the line | `is("server","patched"` |
| `E-LEX` | a word that is not a root or an atom | `hypothesis(is("server","patched"))` |
| `E-ARITY` | a root with the wrong number of places, or with no bracket | `is("server")` |
| `E-KIND` | a place gets a kind it does not take | `all("servers",12)` |
| `E-NAME` | a label that is not defined | `is(o3,"patched")` |
| `E-REDEF` | a label defined twice, or a variable that is already a label | see 1.5.1 |
| `E-HEAD` | the header is wrong, or a header root stands in the body | `msg(Ana,Ana,1)` |
| `E-TIME` | a time that does not exist | `at(2026-13-40,fin("backup"))` |
| `E-QUOTE` | a brace in a quote that is not a reference; a quote with *the*, or with a word that depends on who speaks or when (1.4.5) | `pls(Ben,"restart {o9")` |
| `E-CODE` | in `code(…)`: a language that is not on the list, or Python that does not parse (1.4.6) | `code("python","def f(:")` |
| `E-MATH` | in a formula `'…'`: a formula that is not well formed (1.4.6) | `'x^2-'` |

```sx
is("server","patched"               # E-SYN — the bracket is not closed on the line
hypothesis(is("server","patched"))  # E-LEX — the root is hyp
is("server")                        # E-ARITY — is takes two or three places
all("servers",12)                   # E-KIND — a number is not a criterion
is(o3,"patched")                    # E-NAME — o3 is not defined
re(Ana1)                            # E-HEAD — re stands inside the header only
will(code("python","def f(:"))      # E-CODE — python does not read this
'x^2-'                              # E-MATH — the formula ends where more is needed
```

---

## Part 2. Many agents at once

### 2.1 The model

- **Agents.** Any number of agents take part. An agent has a name (a capital and lower-case letters: `Ana`, `Ben`, `Cy`) and talks by sending messages.
- **Messages.** A message has one sender and one or more receivers, and arrives whole. A message to several receivers is one message, not several copies.
- **The roster** is the list of agents now in the conversation. Everyone knows it. `join` and `leave` change it (2.4). `All` means every agent on the roster except the sender.
- **No shared order.** Messages travel at their own speed. Two receivers may see two messages in different orders, and one receiver may see a later message of one sender before an earlier one. The only order SILEX trusts is the one the headers state (2.3). A send time in a header is a fact about the message; it is not a rule of order, because clocks differ.

### 2.2 The header in full

```text
msg(sender, receiver …, [serial], [time], [re(…)], [saw(…)], [pri(…)])
```

The parts are told apart by their kind, so none is marked; they come in this order.

| Part | Kind | Meaning |
| --- | --- | --- |
| sender | agent name | who writes. Not `Me`, `You` or `All` |
| receivers | one or more agent names, or `All` | who gets the message. Not the sender; no name twice; `All` stands alone |
| serial | whole number from 1 | the number of this message among the sender's own: 1, 2, 3 … The **name** of the message is the sender and the serial: `Ana3` |
| time | ISO time | when it was sent; it fixes `now` for the message |
| `re(M …)` | message or line names | the message answers these (`re(Ana3)`, `re(Ana3.2)`); the sender had read them. When it names exactly one whole message, a bare line number stands for a line of that message (1.5.5) |
| `saw(M …)` | message names | the latest message the sender had read from an agent; earlier ones of that agent are included. It need not list every agent: leave out one whose messages the sender had not read |
| `pri(d)` | `hi` `mid` `lo` | how urgent; `mid` when left out |

A message with no serial has no name and nobody can refer to it; give every message a serial when more than two agents talk. The sender counts its own messages from 1, one more each time.

The sender and every receiver are on the roster when the message is sent. One exception: a message that joins an agent (`join`, 2.4) may name that agent in its header.

```silex
msg(Ana,Ben,Cy,1)  # ok — Ana to two receivers, her message 1
```

```silex
msg(Ben,Ana,Cy,2,2026-11-04T09:03,re(Ana1),saw(Cy1),pri(hi))  # ok — Ben's message 2, sent at 09:03, answering Ana1, having read Cy1, urgent
```

```silex
msg(Ana,All,3)  # ok — Ana to everyone on the roster
```

```silex
msg(Ana,Ana,1)  # E-HEAD — the sender cannot be its own receiver
```

```silex
msg(Ana,Ben,2,re(Ana2))  # E-HEAD — a message cannot answer itself
```

Lines are numbered from 1 after the header, comments and blank lines not counted. `Ana3.2` is line 2 of message `Ana3`; it is also what `re` and the speech acts below use to point at one line.

### 2.3 Order and concurrency

**X precedes Y** when any of these holds, or a chain of them:

1. X and Y have the same sender and X has the smaller serial.
2. Y's header names X in `re(…)` or in `saw(…)`.
3. A line of Y points at X with `ack`, `agree`, `ans`, `err`, `clr`, `rej` or `retr` (2.5): a sender cannot point at what it has not read.

(The chain is what makes `saw(Ben2)` cover Ben1 as well: Ben1 precedes Ben2 by 1, and Ben2 precedes the message that names it by 2.)

Two messages are **concurrent** when neither precedes the other.

What this gives a reader:

- A message answers what its `re` names, and **knows of** every message that precedes it. It does not know of a concurrent message: what it says was said without it.
- A message that names nothing of other agents (no `re`, no `saw`, no pointing line) from a sender that has sent nothing before says that the sender had read nothing. A message of another agent is concurrent with it unless that message names it, directly or by a chain.
- To correct or withdraw a claim, write a message that follows the one corrected (its `re` or `saw` names it) and say so with `retr` or a new claim. A message that does not name it is concurrent with it and corrects nothing.
- A gap in the serials of one sender (1, 2, 4) shows a message that was lost or not yet read. `ack` tells a sender what arrived (2.5).

```silex
msg(Ana,Ben,Cy,2,saw(Ben1,Cy1))  # ok — Ana's 2: it follows Ben1, Cy1 and her own 1
```

Ben1 and Cy1 of Part 0 are concurrent: neither header names the other's message. Ana2 names both, so it follows both, and every reader can tell that Ana had read both when she wrote it.

### 2.4 Who a line is for

- Every receiver gets the whole message.
- `to(Cy, line)` marks one line as for Cy. The other receivers still get it; it is not addressed to them, and `You` inside it means Cy. This is not secrecy: for a private line, send a separate message to that receiver only.
- `You` is each receiver of the message (inside a `to`, each receiver named there). A line that has `You` in it holds, or asks, for each of them separately: `if(…You…, pls(…))` is tested once for every receiver, and each one for whom it holds is asked. `Me` is the sender. `All` is every agent on the roster except the sender.
- `join(Dan)` puts Dan on the roster from this message on, and `leave(Cy)` takes Cy off. An agent that joins receives nothing written before it joined; to bring it up to date, send it a message. The message that joins Dan may have Dan among its receivers (2.2).

```silex
msg(Ana,Ben,Cy,5)                # ok — Ana to Ben and Cy
pls(Ben,"merge release branch")  # ok — a request to Ben
to(Cy,pls("review merge"))       # ok — this line is for Cy: Cy is asked to review the merge
```

```silex
msg(Ana,Ben,Cy,6)            # ok — Ana to Ben and Cy
to(Dan,pls("review merge"))  # E-HEAD — Dan is not a receiver of this message
```

```silex
msg(Ana,All,7)  # ok — Ana to everyone
join(Dan)       # ok — Dan joins the roster
leave(Cy)       # ok — Cy leaves
```

### 2.5 Speech acts

A line is a claim or a speech act. This table says what each does and what a receiver may conclude from it. Part 3 gives the places of each root. In the table `M` is a message name (`Ana3`), a line name (`Ana3.2`) or, in a message whose `re` names exactly one whole message, a bare line number of that message (1.5.5).

| Line | The sender … | A receiver may conclude | Usual reply |
| --- | --- | --- | --- |
| a claim `P` | asserts `P` | the sender says `P` (not that `P` is true) | `agree`, a counter-claim, `yn(P)` |
| `pls(x, A)` `pls(A)` `pls(P)` | asks `x` (or every receiver) to do `A` or to bring `P` about | the sender wants it | `will`, `rej`, `clr`, or the act |
| `will(A)` | undertakes to do `A` | the sender is committed to `A` (by the time a time root names) | |
| `rej(A, P)` `rej(M)` `rej(M, P)` | declines `A`, or the request or proposal in `M`; a message name declines every request and proposal in that message, a line name declines that line; `P`, if given, is the reason and is asserted | the sender will not do it | |
| `sug(A)` `sug(P)` | proposes `A` or `P` to the receivers and itself: *let us* | nothing is adopted yet | `agree`, `rej`, a counter-`sug` |
| `agree(M)` | agrees with message or line `M` | the sender accepts what `M` says or proposes | a proposal is adopted when every receiver it was sent to has agreed |
| `yn(P)` `what(E)` `which(x, P)` `why(P)` | asks | the sender wants the answer | `ans`, `unk`, `clr` |
| `ans(M, V)` | answers question `M` with `V` (`yes`, `no`, a value, a claim) | `V` is the answer | |
| `unk(M)` `unk(P)` | says the answer, or whether `P`, is not known to it | the sender does not know | someone else may answer |
| `hyp(P)` | offers `P` as a hypothesis | the sender suspects `P`; it is not asserted | confirm or deny |
| `assume(P)` | supposes `P` for the lines and messages that follow | `P` is taken as given until retracted | |
| `retr(M)` | takes back a message or a line | it no longer has force | |
| `ack(M …)` | says these messages arrived | they arrived | |
| `err(M)` `err(M, P)` | says message or line `M` has an error; `P` says what and is asserted | the author of `M` is asked to look | `retr`, a new claim |
| `clr(M)` `clr(M, P)` | says `M` is unclear; `P` names what is unclear and is not asserted | the author is asked to restate it | the restatement |
| `join(x …)` `leave(x …)` | changes the roster | | |

Six rules are worth stating on their own.

- **Silence is not agreement.** Nothing is adopted, accepted or done because nobody answered.
- **`rej` declines acts, requests and proposals.** To deny a claim, assert its `not`.
- **`will` speaks for the sender only.** For another agent's intention write `plan(Ben, A)`; for a joint one, `plan(grp(Me, Ben), A)`. A plan is a plan, not an agreement: agreement is `agree`.
- **`sug` speaks for the sender and the receivers together**: *let us*. `pls` speaks to the receivers: *please*.
- **`ans` answers a question, and only a question.** Its first place is a `yn`, `what`, `which` or `why` line. A request (`pls`) is answered with `will` or `rej`; a claim with `agree`, `err` or a claim of its own. `ans(4,a2)` on a line that is a request is wrong, even when `a2` is what was asked for: send it as a `def` and say `will(…)` or assert the result.
- ***Nothing to change* is a claim.** `clr` says a line is unclear and `rej` declines a request, so neither says that a review found nothing to fix. Assert it about the thing reviewed: `val("{Dex6.a1}","review result","no change needed")`.

### 2.6 When messages cross

SILEX gives no rule that picks a winner between concurrent messages, because the winner depends on the work. It gives the means to see that messages are concurrent and to say which one a later message accepts. Five cases:

1. **Crossing claims.** Ana says the build is green while Ben says it is broken, each not having read the other. Both stand. Neither retracts the other. A reader that must decide asks (`what(val("build","status"))`) or waits for a message that names both.
2. **Crossing requests.** Two agents ask Ben for acts that cannot both be done. Ben answers each by name (`re(…)`), accepting one with `will` and declining the other with `rej`.
3. **Crossing proposals.** Two concurrent `sug` lines are both open. A message that names both (`saw`) may `agree` with one and `rej` the other. A proposal is **adopted** when every receiver it was sent to (the receivers of its message, or of its `to`) has said `agree` to it, and not before.
4. **Retraction races.** `retr(M)` has force for every message that follows it (names it, directly or through a chain). A message concurrent with the retraction may still rest on `M`; a reader that holds both can see that, and asks the author or declines the dependent request.
5. **Names.** A label belongs to the message that defines it (1.5.4); no name is shared between messages, so two agents can never define one name at the same moment.

```dialogue
msg(Ana,Ben,Cy,1)               # ok — Ana's 1
pls(Ben,"deploy release")       # ok — Ana asks Ben to deploy
---
msg(Cy,Ben,Ana,1)               # ok — Cy's 1, concurrent with Ana1
pls(Ben,not("deploy release"))  # ok — Cy asks Ben not to deploy
---
msg(Ben,Ana,Cy,1,re(Ana1,Cy1))  # ok — Ben's 1 answers both requests
rej(Ana1)                       # ok — he declines Ana's request
will(not("deploy release"))     # ok — and promises not to deploy
```

```dialogue
msg(Ben,Ana,Cy,1)                                               # ok — Ben's 1
is("backup","finished")                                         # ok — Ben says the backup is finished
---
msg(Ben,Ana,Cy,2)                                               # ok — Ben's 2: it names nothing, so a message that does not name it (Cy1 below) is concurrent with it
retr(Ben1.1)                                                    # ok — he takes line 1 of Ben1 back: it was wrong
---
msg(Cy,Ana,Ben,1,re(Ben1))                                      # ok — Cy's 1: it answers Ben1 and does not name Ben2, so it is concurrent with the retraction
pls(Ana,"delete old backup")                                    # ok — Cy asks Ana to delete the old backup, resting on Ben1.1
---
msg(Ana,Ben,Cy,1,saw(Ben2,Cy1))                                 # ok — Ana's 1: she holds both, and sees the clash
rej("delete old backup",not(know(Me,is("backup","finished"))))  # ok — she declines: she does not know that the backup finished
```

### 2.7 Two worked dialogues

**A. Release night.** Ana leads; Ben and Cy work. Ben1 is written before Ben has read Ana1. Ben4 and Cy2 cross.

```dialogue
msg(Ana,Ben,Cy,1)                                                       # ok — Ana's 1, to Ben and Cy
pls(Ben,"run smoke test")                                               # ok — line 1: Ana asks Ben to run the smoke test
pls(Cy,"run full regression suite")                                     # ok — line 2: and asks Cy to run the full regression suite
---
msg(Ben,Ana,Cy,1)                                                       # ok — Ben's 1, written before he read Ana1: concurrent with it
hyp(is("build","broken"))                                               # ok — Ben suspects the build is broken (a hypothesis, not asserted)
---
msg(Ben,Ana,Cy,2,re(Ana1))                                              # ok — Ben's 2: his answer to Ana1
will("run smoke test")                                                  # ok — Ben promises the smoke test
---
msg(Cy,Ana,Ben,1,re(Ana1))                                              # ok — Cy's 1: Cy's answer to Ana1; concurrent with both of Ben's
rej("run full regression suite",not(may(Me,"write to job scheduler")))  # ok — Cy declines: Cy may not write to the job scheduler
---
msg(Ana,Ben,Cy,2,re(Cy1),saw(Ben2))                                     # ok — Ana's 2: after Cy1 and Ben2 (and so after Ben1)
pls(Ben,"run full regression suite")                                    # ok — she asks Ben to take the regression suite
ack(Ben1)                                                               # ok — and says she got Ben1
---
msg(Ben,Ana,Cy,3,re(Ana2))                                              # ok — Ben's 3
will("run full regression suite")                                       # ok — Ben promises it too
---
msg(Ben,Ana,Cy,4)                                                       # ok — Ben's 4: written without reading anything new
sug(at(2026-11-06,"ship"))                                              # ok — Ben proposes shipping on Friday
---
msg(Cy,Ana,Ben,2)                                                       # ok — Cy's 2: concurrent with Ben4
sug(at(2026-11-09,"ship"))                                              # ok — Cy proposes shipping on Monday
---
msg(Ana,Ben,Cy,3,saw(Ben4,Cy2))                                         # ok — Ana's 3: she has read both proposals
agree(Cy2)                                                              # ok — she agrees with Cy's
rej(Ben4)                                                               # ok — and declines Ben's
---
msg(Ben,Ana,Cy,5,re(Ana3))                                              # ok — Ben's 5
agree(Cy2)                                                              # ok — Ben agrees with Cy's too: both receivers of Cy2 (Ana and Ben) have agreed, so it is adopted
```

**B. An incident.** Dee leads, with Eli and Fay. Gus joins later. Dee's first message is urgent.

```dialogue
msg(Dee,Eli,Fay,1,pri(hi))                      # ok — Dee's 1, urgent, to Eli and Fay
is("checkout service","down")                   # ok — Dee says the checkout service is down
pls(Eli,"check database")                       # ok — asks Eli to check the database
pls(Fay,"check cache layer")                    # ok — asks Fay to check the cache layer
---
msg(Fay,Dee,Eli,1,re(Dee1))                     # ok — Fay's 1: answers Dee1
hyp(cause("cache layer","outage"))              # ok — her hypothesis: the cache layer caused the outage
prob(cause("cache layer","outage"),0.7)         # ok — she puts it at 70 percent
---
msg(Eli,Dee,Fay,1,re(Dee1))                     # ok — Eli's 1: concurrent with Fay1
is("database","healthy")                        # ok — the database is healthy
val("database","replication lag in seconds",2)  # ok — its replication lag is 2 seconds
---
msg(Dee,Eli,Fay,Gus,2,saw(Eli1,Fay1))           # ok — Dee's 2: she has read both; Gus is a receiver from this message on
join(Gus)                                       # ok — Gus joins the roster
to(Gus,pls("restart cache layer"))              # ok — this line is for Gus
---
msg(Gus,Dee,Eli,Fay,1,re(Dee2))                 # ok — Gus's 1
will("restart cache layer")                     # ok — Gus promises
---
msg(Gus,Dee,Eli,Fay,2)                          # ok — Gus's 2
fin("restart of cache layer","successfully")    # ok — the restart is finished, successfully
is("checkout service","down")                   # ok — the checkout service is still down
---
msg(Fay,Dee,Eli,Gus,2,saw(Gus2))                # ok — Fay's 2: she has read Gus2
retr(Fay1.1)                                    # ok — she takes back line 1 of Fay1: the hypothesis
retr(Fay1.2)                                    # ok — and line 2: the 70 percent
what(val("checkout service","error"))           # ok — and asks what the checkout service's error is
---
msg(Eli,Dee,Fay,Gus,2,re(Fay2))                 # ok — Eli's 2
ans(3,"connection refused by payment gateway")  # ok — answers line 3 of Fay2, the one message re names (1.5.5)
```

---

## Part 3. The roots

There are 102 roots, in 12 families. Each row gives the **places** (the kinds a root takes, in order; `[ ]` marks a place that may be left out and `…` one that may repeat), the **kind** the root returns after `→` (`=2` means *the kind of the second place*, for roots that wrap a claim, an act or a line and give the same kind back), a **reading** in English, and an **example** that the checker accepts. A root with two readings (`is` with two places or three) has one place list for each, separated by `;`. In a reading, `x y` stand for things, `A` for an act, `P Q` for claims, `G` for a group, `c` for a criterion, `t` for a time, `d` for a duration, `n` for a number, `M` for a message or line.

A row's example is a line, or a value that a line can hold: where the root returns a value, the example is a value (`cnt("production servers")`), and the cookbook (Part 4) shows it in a line.

Roots that are one edit apart (a letter changed, added, dropped or swapped) are listed in 6.4 together with the places that keep a slip from passing unnoticed.

### 3.1 Logic

`not` flips a claim; on an act it means *not doing it*; on a criterion, *not being c*. `or` means *at least one*; `eith` means *exactly one*. `if(P, X)` takes a claim, an act or a line for `X` and gives the same kind back: *if P then X*. It asserts the link, and neither `P` nor `X`. There is no root for *if and only if*: write `and(if(P,Q),if(Q,P))` or, between formulas, `<=>` inside the quote (1.4.6); for *if P had been so, Q would have been so*, use `would` (3.10).

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `not` | `(Cl) → Cl`; `(Ac) → Ac`; `(Cr) → Cr` | not P (for an act: not doing A; for a criterion: not being c) | `not(is("server","patched"))` |
| `and` | `(Cl, Cl …) → Cl`; `(Ac, Ac …) → Ac` | P, Q, … all hold (for acts: do all of them) | `and(is("web server","patched"),is("database server","patched"))` |
| `or` | `(Cl, Cl …) → Cl`; `(Ac, Ac …) → Ac` | at least one of P, Q, … holds (for acts: do one or more) | `or(is("web server","down"),is("database server","down"))` |
| `eith` | `(Cl, Cl …) → Cl` | exactly one of P, Q, … holds | `eith(is("web server","down"),is("database server","down"))` |
| `if` | `(Cl, X) → =2` | if P then X (X is a claim, an act or a line) | `if(is("web server","patched"),is("database server","patched"))` |

### 3.2 Quantifiers

A quantifier takes a group and, usually, a criterion. `all`, `most` and `half` need the criterion. `many`, `few`, `some` and `none` may do without: `some(G)` says the group has a member, `none(G)` that it has none, `many(G)` that it has many. `few` also says *a few* and *several*, `many` also says *lots* and *plenty*. `most`, `many` and `few` are vague on purpose: SILEX fixes no number for them (*most* is usually more than half). When the number matters, say it with `cnt` and `over` (3.3).

*Not every server is patched* is `not(all(G,"patched"))`: it says some member is not patched, which is what the English means. *Some members are not c* is the same claim.

`crit(o1, P)` is the criterion *being an o1 such that P*; it binds `o1` for use inside `P` (1.5.2). `def(label, expression)` names an expression (1.5.3).

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `all` | `(Gr, Cr) → Cl` | every member of G is c | `all("production servers","patched")` |
| `most` | `(Gr, Cr) → Cl` | most members of G are c | `most("production servers","patched")` |
| `half` | `(Gr, Cr) → Cl` | half of the members of G are c | `half("production servers","patched")` |
| `many` | `(Gr, [Cr]) → Cl` | G has many members (that are c) | `many("production servers")` |
| `few` | `(Gr, [Cr]) → Cl` | G has few members (that are c) | `few("production servers","patched")` |
| `some` | `(Gr, [Cr]) → Cl` | G has at least one member (that is c) | `some("production servers","patched")` |
| `none` | `(Gr, [Cr]) → Cl` | G has no member (that is c) | `none("production servers","patched")` |
| `crit` | `(Vr, Cl) → Cr` | the criterion of being an x such that P | `all("servers",crit(o1,is(o1,"hosts","payment service")))` |
| `def` | `(Nm, Va) → Ln` | the label stands for the expression | `def(g1,filt("servers","patched"))` |

### 3.3 Numbers

Arithmetic, totals and the two ways to say a number about something. **A quantity is named by its unit** in its quotation: *"RAM in GB"*, *"size in MB"*, *"pass rate in percent"*.

- A number that is a property of a named thing: `val(x, "RAM in GB", 16)`; as a value, `val(x, "RAM in GB")`.
- A number with no thing in the line: `eq(n"queue length", 500)`.
- A count: `eq(cnt(G), 12)`.
- A function that no root names: `func("square root", 2)`.

`plus` and `minus` also take a time and a duration (`plus(now, P1D)`), and a group and a member (`plus(G, x)`, `minus(G, x)`); `minus` of two times is a duration. `rng(a, b)` is the range from `a` to `b`, both ends included; `val(x, c, rng(a, b))` says the value lies in it.

A formula in single quotes (1.4.6) carries a formula in its written form: with a comparison it is a claim (`'x>=3'`), without one a number (`eq('2^10-1',1023)`). Inside a formula these function names have an agreed meaning, which the checker does not test: `sqrt abs exp ln floor ceil` of one place; `sin cos tan` in radians; `log(x,b)`, the logarithm of `x` to the base `b`; `round(x,n)`, `x` to `n` decimals; `mod(a,b)`, `gcd(a,b)`, `fact(n)`; `min` and `max` of two or more places; `sum(t,i,a,b)` and `prod(t,i,a,b)`, the sum and the product of the term `t` as `i` runs from `a` to `b`; `int(t,x,a,b)`, the integral of `t` in `x` from `a` to `b`; `d(t,x)`, the derivative of `t` in `x`; `lim(t,x,a)`, the limit of `t` as `x` nears `a`. `pi` and `e` are the constants, so a variable is not called `e`. Any other name is the writer's own function. `plus minus times div pow` stay for arithmetic on labelled quantities (`plus(n1"x",1)`), on times and on groups.

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `plus` | `(Nu, Nu …) → Nu`; `(Tm, Du) → Tm`; `(Du, Du …) → Du`; `(Gr, Va) → Gr` | a plus b (a time plus a duration; a group with a member added) | `plus(2,3)` |
| `minus` | `(Nu, Nu) → Nu`; `(Tm, Du) → Tm`; `(Tm, Tm) → Du`; `(Du, Du) → Du`; `(Gr, Va) → Gr` | a minus b (a time minus a duration; the gap between two times; a group without a member) | `minus(now,P1D)` |
| `times` | `(Nu, Nu …) → Nu`; `(Du, Nu) → Du` | a times b | `times(3,4)` |
| `div` | `(Nu, Nu) → Nu`; `(Du, Nu) → Du`; `(Du, Du) → Nu` | a divided by b | `div(10,4)` |
| `pow` | `(Nu, Nu) → Nu` | a to the power b | `pow(2,10)` |
| `sum` | `(Gr, Cr) → Nu` | total, over the members of G, of their c | `sum("invoices","amount in euros")` |
| `cnt` | `(Gr) → Nu` | the number of members of G | `cnt("production servers")` |
| `avg` | `(Gr, Cr) → Nu`; `(Nu, Nu …) → Nu` | the average of the c of the members of G (or of the numbers) | `avg(3,5,10)` |
| `max` | `(Gr, Cr) → Nu`; `(Nu, Nu …) → Nu` | the largest | `max("invoices","amount in euros")` |
| `min` | `(Gr, Cr) → Nu`; `(Nu, Nu …) → Nu` | the smallest | `min(3,5,10)` |
| `pct` | `(Nu, Nu) → Nu` | a as a percentage of b | `pct(19,20)` |
| `val` | `(Va, Cr) → Va`; `(Va, Cr, Va) → Cl` | the c of x (a value); with a third place: the c of x is V | `val("server","RAM in GB",16)` |
| `func` | `(Cr, Va …) → Va` | apply the function named c to the arguments | `func("square root",2)` |
| `rng` | `(Nu, Nu) → Gr`; `(Du, Du) → Gr`; `(Tm, Tm) → Gr` | the range from a to b | `rng(3,5)` |

### 3.4 Comparison

`eq` says two values are the same thing or the same number. `over under atleast atmost` compare numbers and durations. `apx` means *about equal*. `more(x, y, c)` says `x` has more of the quality `c` than `y` has; the quality is a word such as *"fast"* or *"length"*. `best(G, c)` is the member of `G` that is best by `c`.

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `eq` | `(Va, Va) → Cl` | x and y are the same, or equal | `eq("web server","database server")` |
| `over` | `(Nu, Nu) → Cl`; `(Du, Du) → Cl` | a is greater than b | `over(cnt("production servers"),10)` |
| `under` | `(Nu, Nu) → Cl`; `(Du, Du) → Cl` | a is less than b | `under(3,5)` |
| `atleast` | `(Nu, Nu) → Cl`; `(Du, Du) → Cl` | a is at least b | `atleast(cnt("approvals"),2)` |
| `atmost` | `(Nu, Nu) → Cl`; `(Du, Du) → Cl` | a is at most b | `atmost(3,5)` |
| `apx` | `(Va, Va) → Cl` | x is approximately y | `apx(val("migration","duration"),PT20M)` |
| `more` | `(Va, Va, Cr) → Cl` | x has more of c than y | `more("new version","old version","fast")` |
| `best` | `(Gr, Cr) → Va` | the best member of G by c | `best("candidates","cheap")` |

### 3.5 Groups and relations

`is(x, c)` is the plain predicate: *x is c*. With a third place it is a relation: `is(x, "depends on", y)`. A group may stand in the first place: `is(grp(a, b), "in one region")` says the pair as a whole is; `all(grp(a, b), "patched")` says each is. `mem(x, G)` says `x` is one of `G`; `loc(x, y)` says `x` is in or at `y`; `loc(x)` is the place of `x`. Every other relation (*above*, *near*, *owned by*, *part of*, *depends on*) is a quotation in the second place of `is`.

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `grp` | `(Va …) → Gr` | the group of x, y, … | `grp("web server","database server")` |
| `filt` | `(Gr, Cr) → Gr` | the members of G that are c | `filt("production servers","patched")` |
| `pick` | `(Gr, [Cr]) → Th` | one member of G (that is c) | `pick("production servers","patched")` |
| `mem` | `(Va, Gr) → Cl` | x is a member of G | `mem("audit log","production logs")` |
| `is` | `(Va, Cr) → Cl`; `(Va, Cr, Va) → Cl` | x is c; with a third place: x stands in the relation c to y | `is("web server","depends on","database")` |
| `loc` | `(Va, Va) → Cl`; `(Va) → Th` | x is in or at y; the place of x | `loc("config file","/etc folder")` |

### 3.6 Acts

An act is named by a quotation in the place of an act (*"run smoke test"*). It has no doer until a root gives it one: `act(x, A)` says *x performs A*; `pls(x, A)` asks `x`; `will(A)` is the sender's; `sug(A)` is the sender's and the receivers' together. `fin(A)` is the ending of the act (with the outcome `c` if given): alone it says the act has ended, `at(t, fin(A))` that it ends at `t`, `by(t, fin(A))` that it had ended by `t`. `then(A, B)` is *A, then B*; `par(A, B)` is *A and B together*; `and(A, B)` and `or(A, B)` are *both* and *one or more*. `tell`, `ask` and `chk` are the acts of informing, asking and checking.

`code(language, line, line …)` (1.4.6) is the act of running the program written in its lines: the first quote is the language, each other quote is one line of source. It is an act like the rest: `pls(Ben,code("bash","make test"))` asks Ben to run it, `will(code(…))` promises to, `then(code(…),code(…))` puts two in order, and `fin(code(…),"successfully")` says a run ended well. `def(a1,code(…))` names a program, so that it can be sent with no request and be pointed at (`"review {a1}"`).

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `act` | `(Th\|Gr, Ac) → Cl` | x performs the act A | `act(Ana,"send report to Ben")` |
| `fin` | `(Ac, [Cr]) → Cl` | the act A is finished (with the outcome c) | `fin("deployment to production","successfully")` |
| `then` | `(Ac, Ac …) → Ac` | A, then B, then … | `then("run migration","restart service")` |
| `par` | `(Ac, Ac …) → Ac` | A and B together | `par("run migration","notify team")` |
| `tell` | `(Th, Va) → Ac` | tell x the claim or value V | `tell(Ana,fin("backup"))` |
| `ask` | `(Th, Q) → Ac` | ask x the question Q | `ask(Cy,yn(fin("backup")))` |
| `chk` | `(Cl) → Ac` | check whether P | `chk(is("release build","passes","smoke test"))` |
| `code` | `(Rw, Rw …) → Ac` | the program written in these lines (first the language, then one quote for each line), as the act of running it | `code("python","def add(a,b):","    return a+b")` |

### 3.7 Modality and mind

The first place of a modal is the doer (an agent or a group), the second an act: `must(You, "delete backup")`. With one place a modal takes a claim: `must(by(t, fin(A)))`. `must` is obligation, `should` advice, `may` permission, `can` ability or possibility. `want need plan bel know say` give the mind or the speech of someone, and take whatever they are about. `prob(P, n)` says `P` has probability `n` (0 to 1) in the sender's judgment; `n` may be `hi`, `mid` or `lo`, and `prob(P)` alone says *probably*. `hi`, `mid` and `lo` are degrees with no number behind them. `plan(grp(Me, You), A)` is a joint plan, not an agreement (agreement is `agree`, 2.5). *I am not sure whether* is `unk` (3.8), which is the sender's own state.

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `must` | `(Th\|Gr, Ac) → Cl`; `(Cl) → Cl` | x is required to do A (or: P is required) | `must(You,not("delete backup"))` |
| `should` | `(Th\|Gr, Ac) → Cl`; `(Cl) → Cl` | x ought to do A (or: P ought to hold) | `should(You,"review changes")` |
| `may` | `(Th\|Gr, Ac) → Cl`; `(Cl) → Cl` | x is allowed to do A (or: P is allowed) | `may(Me,"write to job scheduler")` |
| `can` | `(Th\|Gr, Ac) → Cl`; `(Cl) → Cl` | x is able to do A (or: P is possible) | `can(Me,"run test suite")` |
| `want` | `(Th\|Gr, Cl\|Ac) → Cl` | x wants P to hold (or wants to do A) | `want(Me,fin("migration"))` |
| `need` | `(Th\|Gr, Va) → Cl` | x needs V | `need(Me,"API key for staging environment")` |
| `plan` | `(Th\|Gr, Ac) → Cl` | x plans to do A | `plan(Ana,at(2026-11-06,"ship"))` |
| `bel` | `(Th\|Gr, Cl) → Cl` | x believes P | `bel(Me,cause("cache layer","outage"))` |
| `know` | `(Th\|Gr, Cl\|Q) → Cl` | x knows P (or the answer to Q) | `know(Ben,is("build","green"))` |
| `say` | `(Th\|Gr, Cl\|Q\|Ln) → Cl` | x says P (reported speech) | `say(Ben,is("build","green"))` |
| `prob` | `(Cl, [Nu]) → Cl` | P is probable (with probability n) | `prob(is("build","broken"))` |

### 3.8 Lines (speech acts)

These roots return a line, so each can stand alone. The table in 2.5 says what each does and what a receiver may conclude; the examples here show the form. In `agree`, `ans`, `err`, `clr`, `rej` and `unk` the first place may be a bare line number of the one message that `re` names (1.5.5). `pls(A)` with one place is addressed to every receiver (or to those in a `to`); `will(A)` and `rej(A)` are about the sender; `sug` is for the sender and the receivers together.

`will` has one place, the act, because it speaks for the sender: a doer in front of it is `E-ARITY`. For another agent's intention write `plan(Ben,A)`; to ask, `pls(Ben,A)`. A label of another message inside a quote is written with its message: `{Dex7.a1}`, never `{a1}` (that one is `E-NAME` unless this message defined `a1`).

```sx
will("review {Dex7.a1}")        # ok — the sender promises
will(Gds,"review {Dex7.a1}")    # E-ARITY — will takes one place; no doer
plan(Gds,"review {Dex7.a1}")    # ok — Gds plans it
pls(Gds,"review {Dex7.a1}")     # ok — Gds is asked
```

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `unk` | `(Cl\|Q\|Rf) → Ln` | the sender does not know whether P (or the answer to Q) | `unk(what(val("outage","cause")))` |
| `hyp` | `(Cl) → Ln` | P is offered as a hypothesis, not asserted | `hyp(cause("cache layer","outage"))` |
| `assume` | `(Cl) → Ln` | suppose P: take it as given for what follows | `assume(is("cache","empty"))` |
| `pls` | `(Th\|Gr, Ac\|Cl) → Ln`; `(Ac\|Cl) → Ln` | please: x (or each receiver) is asked to do A or to bring P about | `pls(Ben,"run smoke test")` |
| `will` | `(Ac\|Cl) → Ln` | the sender undertakes to do A (or to see to P) | `will("run smoke test")` |
| `rej` | `(Ac\|Cl, [Cl]) → Ln` | the sender declines A, or the request or proposal in the message or line M (because P, which is asserted) | `rej("run full regression suite",not(may(Me,"write to job scheduler")))` |
| `ans` | `(Rf\|Q, Va) → Ln` | the answer to the question is V (yes, no, a value or a claim) | `ans(Ana7.1,yes)` |
| `sug` | `(Cl\|Ac) → Ln` | the sender proposes P (or A) to the receivers and itself: let us | `sug(at(2026-11-06,"ship"))` |
| `agree` | `(Rf) → Ln` | the sender agrees with the message, line or proposal | `agree(Ana3)` |
| `retr` | `(Rf) → Ln` | the sender takes back the message or line | `retr(Ana3.2)` |
| `ack` | `(Rf …) → Ln` | the sender received these messages | `ack(Ana3,Cy1)` |
| `err` | `(Rf, [Cl]) → Ln` | there is an error in the message or line (P says what, and is asserted) | `err(Ana3.2)` |
| `clr` | `(Rf, [Cl]) → Ln` | the message or line is unclear (P names what is unclear, and is not asserted) | `clr(Ana3.2)` |

### 3.9 Time

A time root takes a time, or a claim whose time it stands for (*after the migration finishes* is `after(fin("migration"), …)`; that claim gives the time and is not asserted), and then the thing that is placed in time. The thing can be a claim, an act or a line, and the result has the same kind: `by(t, fin(A))` is a claim, `by(t, A)` is the act *do A by t*, so `pls(by(t, A))` is a request with a deadline.

- `at(t, X)`: `X` holds at `t` (throughout `t`, if `t` is a stretch). `before`, `after`, `by` (at or before) and `until`, `from` (one end open) place `X` against `t`.
- `during(t, X)`: `X` happens at some time within `t`.
- `for(d, X)`: `X` for the length `d`. `each(d, X)`: `X` every `d`. `rep(n, X)`: `X` happens exactly `n` times, in the time of the root round it: `during(t, rep(2, X))` says `X` happens twice, both times within `t`.
- `always(X)`, `still(P)`: at all times; still so. `when(P)` is the time at which `P` happens.

*Last night* is an interval `2026-11-03T22:00/2026-11-04T06:00`; *every Friday* is a quotation, `"deploy on Fridays"`, or `each(P7D, …)` when the period is what matters.

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `at` | `(Tm\|Cl, X) → =2` | at time t, X (throughout t when t is a stretch) | `at(2026-11-04T15:00,fin("deployment to production"))` |
| `before` | `(Tm\|Cl, X) → =2` | before t, X | `before(2026-11-04T17:00,is("server","frozen"))` |
| `after` | `(Tm\|Cl, X) → =2` | after t, X | `after(fin("migration"),act(Ben,"restart service"))` |
| `by` | `(Tm\|Cl, X) → =2` | at or before t, X | `by(2026-11-06T17:00,act(Ana,"send report to Ben"))` |
| `until` | `(Tm\|Cl, X) → =2` | X until t | `until(2026-11-06,is("server","frozen"))` |
| `from` | `(Tm\|Cl, X) → =2` | X from t onward | `from(2026-11-04,is("server","frozen"))` |
| `during` | `(Tm\|Cl, X) → =2` | X at some time within t | `during(2026-11-03T22:00/2026-11-04T06:00,fin("restart"))` |
| `for` | `(Du, X) → =2` | X for the length of time d | `for(PT3H,is("service","down"))` |
| `each` | `(Du, X) → =2` | X every d | `each(P1D,fin("backup"))` |
| `rep` | `(Nu, X) → =2` | X happens n times | `rep(2,fin("restart"))` |
| `always` | `(X) → =1` | X at all times | `always(is("daemon","listening"))` |
| `still` | `(Cl) → Cl` | P still holds | `still(is("server","down"))` |
| `when` | `(Cl) → Tm` | the time at which P happens | `when(fin("build"))` |

### 3.10 Cause and reason

The cause or reason comes first in every one of these. `cause(x, y)`: `x` (a thing, an act or a claim) causes `y`. `supp(P, Q)`: `P` is a reason or evidence for believing `Q`. `ent(G, Q)`: `Q` follows from the premises `G`: a group (`grp(Ana1.1,Ana1.2)`) or, for one premise, that line by its reference (`ent(Ana1.1,Q)`). A line used as a premise stands for the claim it carries: a claim line, itself; `assume` and `hyp`, the supposition; `ent`, its conclusion. A whole message is not a premise (`E-KIND`): name its lines. `would(P, Q)`: if `P` had held, `Q` would have held (as a rule `P` did not hold). `cause` asserts `P`, `Q` and the link; `supp`, `ent` and `would` assert none of their claims (1.8). `why(P)` asks for the cause of `P`. *Q because P* is `cause(P, Q)` when `P` brought `Q` about and `supp(P, Q)` when `P` is the reason to believe `Q`.

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `cause` | `(Va, Va) → Cl` | x (a thing, an act or a claim) causes y | `cause(fin("review"),is("report","ready"))` |
| `supp` | `(Cl, Cl) → Cl` | P is a reason or evidence for believing Q | `supp(is("light","on"),is("Bob","home"))` |
| `ent` | `(Gr\|Rf, Cl, [Cr]) → Cl` | Q follows from the premises G, a group or one line reference (under the rules c) | `ent("test results",is("release build","safe"))` |
| `would` | `(Cl, Cl) → Cl` | if P had held, Q would have held | `would(not(fin("review")),not(is("report","ready")))` |
| `why` | `(Cl) → Q` | why is it so that P? | `why(fin("deployment"))` |

### 3.11 Questions

`yn(P)` asks whether `P`. `what(E)` asks for the value of `E`, which can be a count, a time, a place, an attribute, a group: *how many* is `what(cnt(G))`, *when* is `what(when(P))`, *where* is `what(loc(x))`, *who is responsible* is `what(val(x,"responsible person"))`. `which(o1, P)` asks which `o1` makes `P` hold. `why(P)` asks why. The answer is `ans(M, V)` (2.5).

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `yn` | `(Cl) → Q` | is it so that P? | `yn(is("cache","enabled"))` |
| `what` | `(Va) → Q` | what is E? | `what(cnt("production servers"))` |
| `which` | `(Vr, Cl) → Q` | which x makes P hold? | `which(o1,and(mem(o1,"tests"),is(o1,"failed")))` |

### 3.12 Protocol

`msg` is the header (2.2); `re`, `saw` and `pri` are details that stand only inside it. `to(x, line)` addresses one line to some receivers (2.4). `join` and `leave` change the roster.

| Root | Places | Reading | Example |
| --- | --- | --- | --- |
| `msg` | `(Ag, Ag …, [Nu], [Tm], [Hd …]) → Hd` | header: from, to (one or more), serial, send time, details | `msg(Ana,Ben,3)` |
| `re` | `(Rf …) → Hd` | header detail: in reply to these messages | `msg(Ben,Ana,4,re(Ana3))` |
| `saw` | `(Rf …) → Hd` | header detail: the latest messages seen from others | `msg(Ben,Ana,5,saw(Ana3,Cy1))` |
| `pri` | `(Dg) → Hd` | header detail: the priority of the message (hi, mid or lo) | `msg(Ana,Ben,1,pri(hi))` |
| `to` | `(Ag …, Ln) → Ln` | the line is addressed to these receivers (the others still receive it) | `to(Cy,pls("run full regression suite"))` |
| `join` | `(Ag …) → Ln` | these agents join the conversation | `join(Dan)` |
| `leave` | `(Ag …) → Ln` | these agents leave the conversation | `leave(Dan)` |

### 3.13 Atoms

The atoms are in 1.7:

| Atom | Kind | Reading |
| --- | --- | --- |
| `now` | Tm | the time this message was sent |
| `Me` | Ag | the sender of this message |
| `You` | Ag | each receiver of this message |
| `All` | Ag | every agent on the roster |
| `yes` | An | the answer yes |
| `no` | An | the answer no |
| `hi` | Dg | a high degree |
| `mid` | Dg | a middle degree |
| `lo` | Dg | a low degree |
| `_` | Un | unspecified: some value that is not given |

---

## Part 4. Cookbook: how do I say …?

Every line in 4.1 to 4.9 is one of the 84 English test sentences, written in SILEX and run through the checker; the English is the comment. Sections 4.10 and 4.11 add patterns that those sentences do not reach, and 4.13 shows mathematics. A line stands alone as a line of a message; the header is left out. The sentences were written by the drafter, and the encodings are one good way each, not the only one.

### 4.1 That something is so

A thing and a property, a relation, an identity, a membership, a choice.

```sx
all(grp("web server","database server"),"patched")              # ok — The web server and the database server are patched.
loc("config file","/etc folder")                                # ok — The config file is in the /etc folder.
eq("web server","database server")                              # ok — The web server is the same as the database server.
mem("audit log","production logs")                              # ok — The audit log is one of the production logs.
or(is("web server","down"),is("database server","down"))        # ok — Either the web server or the database server is down.
all("tests on main branch","failing")                           # ok — The tests are failing on the main branch.
eq(val("first server","region"),val("second server","region"))  # ok — Both servers are in the same region.
act(_,"change configuration")                                   # ok — Someone changed the configuration.
```

A property is `is(x, c)`; a relation is `is(x, c, y)`; identity is `eq`; membership is `mem`; place is `loc`. *Either … or* is the inclusive `or`; write `eith` when exactly one is meant. *Someone* and *something* are `_`.

### 4.2 How many, how much, how all

Quantifiers, counts and numbers about things.

```sx
all("production servers","patched")                                 # ok — Every production server is patched.
none("production servers","patched")                                # ok — No production server is patched.
not(all("production servers","patched"))                            # ok — Some production servers are not patched.
over(cnt("production servers"),10)                                  # ok — There are more than 10 production servers.
and(eq(cnt("production servers"),12),eq(cnt("staging servers"),3))  # ok — We have 12 production servers and 3 staging servers.
val("report file","size in MB",12)                                  # ok — The report file is 12 megabytes.
eq(n"pass rate in percent",95)                                      # ok — The pass rate is 95%.
val("server","RAM in GB",16)                                        # ok — The server has 16 GB of RAM.
eq(cnt("bugs found by {Me} in parser"),2)                           # ok — I found two bugs in the parser.
all("tests","passed")                                               # ok — All tests passed.
none("servers","down")                                              # ok — None of the servers are down.
eq(cnt("messages in queue"),500)                                    # ok — The queue has 500 messages.
some("bugs in login code")                                          # ok — There is a bug in the login code.
```

*Some … are not* is `not(all(…))`. A number about a named thing is `val(x, "…", n)`; a number with no thing is `eq(n"…", n)`; a count is `cnt`. The unit is in the quotation.

### 4.3 Questions

A yes-or-no question, a question for a value, a question for a group, a why.

```sx
yn(is("release build","passes","smoke test"))  # ok — Does the release build pass the smoke test?
what(filt("production servers","patched"))     # ok — Which production servers are patched?
what(cnt("production servers"))                # ok — How many production servers are there?
what(when(fin("build")))                       # ok — When will the build finish?
what(loc("config file"))                       # ok — Where is the config file?
why(is("deployment","failed"))                 # ok — Why did the deployment fail?
yn(fin("backup"))                              # ok — Tell me whether the backup finished.
yn(is("cache","enabled"))                      # ok — Is the cache enabled?
what(val("build","status"))                    # ok — What is the status of the build?
what(val("release","responsible person"))      # ok — Who is responsible for the release?
what(filt("tests","failed"))                   # ok — Which tests failed?
```

*Tell me whether* is the question itself: `yn(…)`. *How many*, *when*, *where* and *who* are `what(…)` of a count, a time, a place or an attribute.

### 4.4 Asking, promising, refusing, proposing

Speech acts: the sender asks, promises, declines, proposes.

```sx
pls(and("run smoke test","run full regression suite"))                  # ok — Please run the smoke test and the full regression suite.
will("run smoke test")                                                  # ok — I will run the smoke test.
rej("run full regression suite",not(may(Me,"write to job scheduler")))  # ok — I decline to run the full regression suite because I do not have write permission on the job scheduler.
pls(chk(is("release build","passes","smoke test")))                     # ok — Please check whether the release build passes the smoke test.
pls("restart service")                                                  # ok — Could you restart the service?
pls(not(before(2026-11-04T17:00,"deploy")))                             # ok — Don't deploy before 5 pm.
sug(at(2026-11-09,"meet"))                                              # ok — Let us meet on Monday.
pls("send logs of 2026-11-03 to {Me}")                                  # ok — Can you send me the logs from yesterday?
pls(by(2026-11-05,"review pull request of {Me}"))                       # ok — Please review my pull request by tomorrow.
will(after(fin("build"),tell(You,fin("build"))))                        # ok — I will let you know when the build is done.
retr(U1)                                                                # ok — Please ignore my previous message.
pls(not("touch production database"))                                   # ok — Don't touch the production database.
pls(by(2026-11-05T00:00,fin("backup")))                                 # ok — Make sure the backup completes before midnight.
pls("use staging server for test")                                      # ok — Use the staging server for the test.
pls(and("update documentation","notify team"))                          # ok — Update the documentation and notify the team.
```

A polite question that is really a request (*could you*, *can you*) is `pls`. *Don't* is `pls(not(…))`. *Let us* is `sug`. *Let you know when* is a promise of an act placed after an event. *Ignore my previous message* is `retr` of that message, which needs its name. The words *me* and *my* in a quotation are written `{Me}`.

### 4.5 When

A time, a deadline, a date, a stretch, a duration.

```sx
must(by(2026-11-06T17:00,fin("smoke test")))                               # ok — The smoke test must be complete by Friday 5 pm.
at(2026-11-03,act(Alice,"run regression suite"))                           # ok — Alice ran the regression suite yesterday.
by(2026-11-06,is("web server","patched"))                                  # ok — The web server will be patched by Friday.
by(2026-11-06T17:00,act(Alice,"send report to Bob"))                       # ok — Alice will send the report to Bob by Friday 5 pm.
at(2026-11-04T15:00,fin("deployment to production","successfully"))        # ok — The deployment to production finished successfully at 3 pm.
apx(val("database migration","duration"),PT20M)                            # ok — The database migration will take about 20 minutes.
pls(after(fin("migration"),"restart service"))                             # ok — After the migration finishes, restart the service.
val("meeting","time",2026-11-09T10:00)                                     # ok — The meeting is at 10:00 on Monday.
at(2026-11-03,act(_,"send report to client"))                              # ok — The report was sent to the client yesterday.
during(2026-11-03T22:00/2026-11-04T06:00,rep(2,act("service","restart")))  # ok — The service restarted twice last night.
```

The date is written out (the cookbook assumes today is Wednesday 2026-11-04). *Yesterday*, *Friday* and *last night* become an ISO date, a date and a time, an interval. A doer that is not given is `_`.

### 4.6 Can, may, must, want

Ability, permission, obligation, advice, wish, need, plan.

```sx
must(You,not("delete backup"))                # ok — You must not delete the backup.
should(You,"review changes")                  # ok — You should review the changes.
can(Me,"run test suite")                      # ok — I can run the test suite.
not(can(Me,"run regression suite"))           # ok — I cannot run the regression suite.
want(Me,fin("migration"))                     # ok — I want to finish the migration.
need(Me,"API key for staging environment")    # ok — I need the API key for the staging environment.
should(grp(Me,You),not("deploy on Fridays"))  # ok — We should not deploy on Fridays.
plan(grp(Me,You),at(2026-11-06,"ship"))       # ok — We plan to ship on Friday.
```

The doer comes first: `must(You, …)`. *We* is `grp(Me, You)`: the sender and the receivers. `All` is everyone else on the roster, so *everyone* is `grp(Me, All)`. *Cannot* is `not(can(…))`.

### 4.7 What is thought, said, or not known

Belief, probability, reports, suppositions, doubt.

```sx
prob(is("build","broken"))             # ok — The build is probably broken.
bel(Me,cause("cache layer","outage"))  # ok — I think the cache layer caused the outage.
say(Bob,is("build","green"))           # ok — Bob said the build is green.
assume(is("cache","empty"))            # ok — Suppose the cache is empty.
prob(is("build","passing"),0.9)        # ok — I am 90% sure the build passes.
say("customer",is("invoice","wrong"))  # ok — The customer says the invoice is wrong.
unk(is("fix","working"))               # ok — I am not sure whether the fix works.
prob(is("fix","working"))              # ok — The fix probably works.
unk(what(val("outage","cause")))       # ok — I do not know the cause of the outage.
val(Me,"estimate",P3D)                 # ok — My estimate is 3 days.
```

`bel(Me, …)` is the sender's belief; `say(x, …)` is what someone else said (the claim is mentioned, not asserted); `prob` gives a degree; `unk` is *I do not know*; `assume` supposes.

### 4.8 Because, if, more than

Cause, condition, comparison.

```sx
if(is("web server","patched"),is("database server","patched"))  # ok — If the web server is patched, the database server is patched too.
more("old logo","new logo","length")                            # ok — The old logo is longer than the new logo.
if(is("build","failed"),pls("notify Alice"))                    # ok — If the build fails, notify Alice.
cause(fin("review"),is("report","ready"))                       # ok — The report is ready because the review finished.
over(n"error rate on 2026-11-04",n"error rate on 2026-11-03")   # ok — The error rate is higher than yesterday.
if(not(can(You,"access server")),pls(tell(Me,_)))               # ok — If you cannot access the server, tell me.
more("new version","old version","fast")                        # ok — The new version is faster than the old one.
```

The cause comes first in `cause(x, y)`. `if(P, X)` takes a claim, an act or a line for `X`. A comparison of a quality is `more(x, y, c)`; of two numbers, `over`.

### 4.9 Doing things in order

Acts one after another, and what was done.

```sx
pls(then("run migration","restart service"))                  # ok — Run the migration, then restart the service.
and(act(Me,"check logs"),none("findings in logs","unusual"))  # ok — I checked the logs and found nothing unusual.
```

`then(A, B)` is *A, then B*. A report of an act and its finding is a claim about the act and a claim about the finding.

### 4.10 More patterns

Things the test sentences do not reach: counterfactuals, ranges, exceptions, nested quantifiers, definitions, reports of questions, recurrence, hedges and the hatch.

```sx
would(not(fin("review")),not(is("report","ready")))                    # ok — If the review had not finished, the report would not be ready.
val("migration","duration",rng(P3D,P5D))                               # ok — The migration takes between 3 and 5 days.
eith(is("web server","down"),is("database server","down"))             # ok — Exactly one of the web server and the database server is down.
all(minus("servers","staging server"),"patched")                       # ok — All servers except the staging server are patched.
eq(filt("people","has access"),grp(Ana))                               # ok — Only Ana has access.
all("servers",crit(o1,some("services",crit(o2,is(o1,"hosts",o2)))))    # ok — Every server hosts some service.
def(c1,crit(o1,none("failures of {o1} in last 7 days")))               # ok — Let "stable" be: no failure in the last 7 days. (c1 names the criterion)
is("payment service",c1)                                               # ok — The payment service is stable.
say(Ben,yn(is("cache","enabled")))                                     # ok — Ben asked whether the cache is enabled.
say("customer",q"invoice looks wrong and logo is blurry")              # ok — The customer wrote that the invoice looks wrong and the logo is blurry. (the hatch)
each(P1D,act(_,"run backup"))                                          # ok — The backup runs every day.
for(PT3H,is("service","down"))                                         # ok — The service was down for three hours.
from(2026-11-02,is("server","frozen"))                                 # ok — The server has been frozen since Monday.
until(2026-11-06,is("server","frozen"))                                # ok — The server is frozen until Friday.
always(loc("daemon","port 80"))                                        # ok — The daemon always listens on port 80.
can(is("migration","failed"))                                          # ok — The migration might fail.
prob(is("fix","working"),lo)                                           # ok — The fix is unlikely to work.
atleast(cnt("approvals"),3)                                            # ok — There are at least three approvals.
eq(pct(cnt(filt("tests","passed")),cnt("tests")),95)                   # ok — 95 percent of the tests passed.
eq(avg("invoices","amount in euros"),120)                              # ok — The average invoice is 120 euros.
pls(after(plus(now,PT1H),"retry"))                                     # ok — Retry in an hour.
pls(Ben,by(2026-11-05,"review pull request"))                          # ok — Ben, review the pull request by tomorrow.
if(and(is("build","green"),is("tests","passed")),pls("ship release"))  # ok — If the build is green and the tests passed, ship the release.
pls(and(then("run migration","restart service"),"notify team"))        # ok — Run the migration and then restart the service, and notify the team.
need(grp(Me,Ben),"access to staging server")                           # ok — Ben and I need access to the staging server.
know(Ben,what(val("build","status")))                                  # ok — Ben knows what the status of the build is.
plan(Ben,after(fin("migration"),"restart service"))                    # ok — Ben plans to restart the service after the migration.
what(best("candidates","cheap"))                                       # ok — Which candidate is the cheapest?
```

### 4.11 Code and formulas

A program or a formula is carried as it is written (1.4.6). Neither a program nor a formula runs or solves anything: a receiver decides what to do with them.

```sx
pls(Ben,code("bash","cd service","make test"))                       # ok — Ben, run these two commands.
will(code("sql","SELECT team, SUM(hours) FROM log GROUP BY team;"))  # ok — I will run this query.
pls(Ben,then(code("bash","make"),code("bash","make test")))          # ok — Ben, build, and then test.
def(a2,code("json","{""retries"": 3, ""pause"": 0.5}"))              # ok — a2 names a one-line configuration file.
fin(code("bash","make"),"successfully")                              # ok — The build ended successfully.
eq(n"result",'12*15/100')                                            # ok — The result is 12 times 15 over 100.
if('x>0',pls("continue"))                                            # ok — If x is positive, continue.
hyp('a^2+b^2=c^2')                                                   # ok — Suppose a squared plus b squared is c squared.
'x>0 & x<10'                                                         # ok — x is between 0 and 10.
'sum(i^2,i,1,n)=n*(n+1)*(2*n+1)/6'                                   # ok — The sum of the squares from 1 to n is n(n+1)(2n+1)/6.
prob('x>0',hi)                                                       # ok — x is probably positive.
```

**A program sent for review.** Ana names a program and asks Ben to review it. Ben answers that line 1 of her message is wrong, sends a corrected program under his own `a1` (reached as `Ben1.a1`), and asks her to use it. She promises to, and asks him to run the tests.

```dialogue
msg(Ana,Ben,1)                                                              # ok — Ana's 1
def(a1,code("python","def moving_avg(xs, n):","    out = []","    for i in range(len(xs) - n + 1):","        out.append(sum(xs[i:i+n]) / n)","    return out"))  # ok — a program, named a1; nothing is run
pls(Ben,"review {a1}")                                                      # ok — Ana asks Ben to review it
---
msg(Ben,Ana,1,re(Ana1))                                                     # ok — Ben's 1, an answer to Ana1
err(1,q"division by zero when n is 0")                                      # ok — line 1 of Ana1, the program, is wrong
def(a1,code("python","def moving_avg(xs, n):","    if n <= 0:","        return []","    out = []","    for i in range(len(xs) - n + 1):","        out.append(sum(xs[i:i+n]) / n)","    return out"))  # ok — his corrected program, Ben1.a1
pls(Ana,"use {a1} in place of {Ana1.a1}")                                   # ok — and he asks Ana to use it
---
msg(Ana,Ben,2,re(Ben1))                                                     # ok — Ana's 2, an answer to Ben1
will("use {Ben1.a1}")                                                       # ok — she promises to
pls(Ben,code("bash","python3 -m pytest -q"))                                # ok — and asks Ben to run the tests
```

**An equation solved.** The equation is a claim in the first message, with the question under it. The answer follows from line 1, and answers line 2.

```dialogue
msg(Ana,Ben,1)                          # ok — Ana's 1
assume('x^2-5*x+6=0')                   # ok — line 1: suppose x^2-5x+6=0
what(val("x","value"))                  # ok — line 2: what is the value of x?
---
msg(Ben,Ana,1,re(Ana1))                 # ok — Ben's 1, an answer to Ana1
ent(Ana1.1,'(x-2)*(x-3)=0')             # ok — from line 1 of Ana1 it follows that (x-2)(x-3)=0
ans(2,'x=2 | x=3')                      # ok — the answer to line 2: x is 2 or x is 3
```

### 4.12 Things with no root

Three things come up in real exchanges and have no root. Each is said as an English value inside `val`, which a reader can match by its wording and a checker cannot test.

```sx
val("average of empty list","result","undefined")       # ok — no value exists (not unk: that is the sender not knowing)
val("{Dex7.a1}","review result","no change needed")     # ok — a review found nothing to change
val("run of {Dex7.a1}","output","42")                   # ok — what a run printed; no root for a result
```

`unk` says the sender does not know, `_` says a value is not given, and neither says that a value is undefined. `clr` and `rej` do not say that nothing needs changing (2.5). If these come up often, they are candidates for roots.

### 4.13 Mathematics in conversation

Mathematical talk has a few habits of its own. This section shows them on six short problems and on two long conversations about two hard problems. Every block was run through the checker; the comment on each line is the English.

- **A formula is a value in single quotes** (1.4.6). A claim stands as a line by itself and is asserted; a supposition goes in `assume('…')`, a guess in `hyp('…')`.
- **A step is `ent(premises, conclusion, reason)`** (3.10). The premises are lines, named by their numbers: `ent(Ben1.2,'x=5')` for one, `ent(grp(Ben1.2,Ben1.4),'x=5')` for several. A line used as a premise stands for what it carries: a claim line, itself; `assume` and `hyp`, the supposition; `ent`, its conclusion. The reason is a short English quote that names the rule. `ent` asserts none of its claims (1.8).
- **Claims between formulas are joined inside the quote**: `'x>0 & x<10'`, `'x=2 | x=3'`, `'x>0 => x^2>0'`, `'x^2=4 <=> x=2 | x=-2'`.
- **A question is `what(…)` and its answer is `ans`**; the answer is a number (`ans(2,5)`) or a claim (`ans(1,'p=1/6')`).
- **A slip is `err` with the right claim, then `retr` by its author**; doubt is `clr`; agreement is `agree`.
- **What no root says stays English**: notation and whole sentences in `q"…"`, reasons in a quote. The names in a formula are the writer's own and the checker does not look them up.

#### 4.13.1 Six short problems

**1. A linear equation.** Ana poses it; Ben solves it step by step, each step resting on a line by its number; Ana checks the answer by putting it back.

```dialogue
msg(Ana,Ben,1)                                       # ok — Ana's 1
assume('3*x+5=20')                                   # ok — line 1: suppose 3x+5=20
what(val("x","value"))                               # ok — line 2: what is the value of x?
---
msg(Ben,Ana,1,re(Ana1))                              # ok — Ben's 1, an answer to Ana1
ent(Ana1.1,'3*x=15',"subtract 5 from both sides")    # ok — line 1: from line 1 of Ana1, 3x=15
ent(Ben1.1,'x=5',"divide both sides by 3")           # ok — line 2: from line 1 of this message, x=5
ans(2,5)                                             # ok — line 3: the answer to line 2 of Ana1 is 5
---
msg(Ana,Ben,2,re(Ben1))                              # ok — Ana's 2, an answer to Ben1
ent(Ben1.2,'3*5+5=20',"substitute 5 for x")          # ok — line 1: a check: from x=5 it follows that 3*5+5=20
agree(3)                                             # ok — line 2: Ana agrees with line 3 of Ben1
```

**2. An inequality, and a slip caught.** Ana forgets that dividing by a negative number turns an inequality round. Ben names the line and gives the right implication, Ana takes the line back and sends the right one.

```dialogue
msg(Ana,Ben,1)                                                              # ok — Ana's 1
assume('-2*x+1>7')                                                          # ok — line 1: suppose -2x+1>7
ent(Ana1.1,'-2*x>6',"subtract 1 from both sides")                           # ok — line 2: from line 1, -2x>6
ent(Ana1.2,'x>-3',"divide both sides by -2")                                # ok — line 3: from line 2, x>-3
---
msg(Ben,Ana,1,re(Ana1))                                                     # ok — Ben's 1, an answer to Ana1
err(3,'-2*x>6 => x<-3')                                                     # ok — line 3 of Ana1 is wrong: if -2x>6 then x<-3
---
msg(Ana,Ben,2,re(Ben1))                                                     # ok — Ana's 2, an answer to Ben1
retr(Ana1.3)                                                                # ok — line 1: she takes back line 3 of her message 1
ent(Ana1.2,'x<-3',"dividing by a negative number turns inequality round")   # ok — line 2: and gives the right step, from line 2 of Ana1
---
msg(Ben,Ana,2,re(Ana2))                                                     # ok — Ben's 2, an answer to Ana2
agree(2)                                                                    # ok — line 1: Ben agrees with line 2 of Ana2
```

**3. A proof by induction.** Ana offers a guess and asks for a proof. The base case is a fact and stands as a bare formula; the step is an implication, built with `=>`; the last line puts the two together.

```dialogue
msg(Ana,Ben,1)                                                              # ok — Ana's 1
hyp('sum(2*i-1,i,1,n)=n^2')                                                 # ok — line 1: a guess, not asserted: the first n odd numbers add up to n squared
pls(Ben,"prove by induction on n")                                          # ok — line 2: Ben, please prove it by induction on n
---
msg(Ben,Ana,1,re(Ana1))                                                     # ok — Ben's 1, an answer to Ana1
'sum(2*i-1,i,1,1)=1^2'                                                      # ok — line 1: base case: for n=1 the sum is 1, which is 1 squared
'sum(2*i-1,i,1,n+1)=sum(2*i-1,i,1,n)+(2*n+1)'                               # ok — line 2: n+1 terms are the first n terms and the next odd number, 2n+1
ent(Ben1.2,'sum(2*i-1,i,1,n)=n^2 => sum(2*i-1,i,1,n+1)=n^2+2*n+1',"replace sum of n terms")   # ok — line 3: if the sum of n terms is n^2, the sum of n+1 terms is n^2+2n+1
ent(Ben1.3,'sum(2*i-1,i,1,n)=n^2 => sum(2*i-1,i,1,n+1)=(n+1)^2',"factor right side")           # ok — line 4: and n^2+2n+1 is (n+1)^2
ent(grp(Ben1.1,Ben1.4),'sum(2*i-1,i,1,n)=n^2',"induction on n")             # ok — line 5: from the base case and the step, the claim holds for every n
---
msg(Ana,Ben,2,re(Ben1))                                                     # ok — Ana's 2, an answer to Ben1
agree(5)                                                                    # ok — line 1: Ana agrees with line 5 of Ben1
```

**4. The largest value of a function.** Ben uses `d(t,x)`, the derivative of `t` in `x` (3.3), and an *if and only if* between two formulas.

```dialogue
msg(Ana,Ben,1)                                                              # ok — Ana's 1
'f(x)=x*(10-x)'                                                             # ok — line 1: f(x)=x(10-x), a definition asserted
what(val("f","largest value"))                                              # ok — line 2: what is the largest value of f?
---
msg(Ben,Ana,1,re(Ana1))                                                     # ok — Ben's 1, an answer to Ana1
ent(Ana1.1,'d(f(x),x)=10-2*x',"differentiate")                              # ok — line 1: the derivative of f is 10-2x
ent(Ben1.1,'d(f(x),x)=0 <=> x=5',"solve 10-2*x=0")                          # ok — line 2: the derivative is 0 if and only if x=5
ent(Ben1.1,'d(d(f(x),x),x)=-2',"differentiate again")                       # ok — line 3: the second derivative is -2
ent(grp(Ana1.1,Ben1.2,Ben1.3),'f(5)=25',"second derivative is negative, so x=5 is a maximum")   # ok — line 4: so the largest value is f(5)=25
ans(2,25)                                                                   # ok — line 5: the answer to line 2 of Ana1 is 25
---
msg(Ana,Ben,2,re(Ben1))                                                     # ok — Ana's 2, an answer to Ben1
agree(4)                                                                    # ok — line 1: Ana agrees with line 4 of Ben1
```

**5. A probability.** The answer is a claim, so `ans` carries a formula.

```dialogue
msg(Ana,Ben,1)                                                              # ok — Ana's 1
what(val("two dice sum to 7","probability"))                                # ok — line 1: what is the probability that two dice sum to 7?
---
msg(Ben,Ana,1,re(Ana1))                                                     # ok — Ben's 1, an answer to Ana1
val("pairs of dice","count",36)                                             # ok — line 1: there are 36 pairs of dice
val("pairs of dice that sum to 7","count",6)                                # ok — line 2: 6 of them sum to 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1
ent(grp(Ben1.1,Ben1.2),'p=6/36',"all pairs are equally likely")            # ok — line 3: so p=6/36
ent(Ben1.3,'p=1/6',"reduce fraction")                                       # ok — line 4: so p=1/6
ans(1,'p=1/6')                                                              # ok — line 5: the answer to line 1 of Ana1 is p=1/6
---
msg(Ana,Ben,2,re(Ben1))                                                     # ok — Ana's 2, an answer to Ben1
agree(5)                                                                    # ok — line 1: Ana agrees with line 5 of Ben1
```

**6. Two equations at once.** `&` joins the two equations in one supposition, and again in the check.

```dialogue
msg(Ana,Ben,1)                                                              # ok — Ana's 1
assume('x+y=10 & x-y=2')                                                    # ok — line 1: suppose x+y=10 and x-y=2
what(val("x","value"))                                                      # ok — line 2: what is x?
what(val("y","value"))                                                      # ok — line 3: what is y?
---
msg(Ben,Ana,1,re(Ana1))                                                     # ok — Ben's 1, an answer to Ana1
ent(Ana1.1,'2*x=12',"add equations")                                        # ok — line 1: adding the two equations gives 2x=12
ent(Ben1.1,'x=6',"divide both sides by 2")                                  # ok — line 2: x=6
ent(grp(Ana1.1,Ben1.2),'y=4',"put 6 for x in first equation")               # ok — line 3: y=4
ans(2,6)                                                                    # ok — line 4: the answer to line 2 of Ana1 is 6
ans(3,4)                                                                    # ok — line 5: the answer to line 3 of Ana1 is 4
ent(grp(Ben1.2,Ben1.3),'6+4=10 & 6-4=2',"check both equations")             # ok — line 6: check: 6+4=10 and 6-4=2
---
msg(Ana,Ben,2,re(Ben1))                                                     # ok — Ana's 2, an answer to Ben1
agree(6)                                                                    # ok — line 1: Ana agrees with line 6 of Ben1
```

#### 4.13.2 A physics problem: the innermost stable orbit of a perturbed black hole

**The problem.** A test particle moves in the equatorial plane of a Kerr spacetime (mass M, spin a) whose metric is changed by a small, static, axisymmetric perturbation h. Derive the effective potential to first order in ε, state the exact condition for circular orbits, and find the shift of the radius of the innermost stable circular orbit (ISCO).

**The conversation.** Ana poses the problem. Ben answers with the steps of a solution, one step to a line, so that each step has a number (`Ben1.8` is line 8 of Ben's first message). Ana agrees with two lines (`agree(11)`, `agree(19)`), says that one is unclear (`clr(12,…)`), takes back a request of her own (`retr(Ana1.6)`) and sends a better one, and asks for a numeric test. Ben answers each. The names `Veff`, `gti` and `d1` are Ben's own; he says what they mean in `q"…"` lines (`Ben1.3`, `Ben1.15`). It is 1,326 tokens on `cl100k` (6.10).

```dialogue
msg(Ana,Ben,1)                                                     # ok — Ana's 1
assume(q"test particle of mass m moves in equatorial plane of Kerr spacetime with mass M and spin a")  # ok — Suppose a test particle of mass m moves in the equatorial plane of a Kerr spacetime with mass M and spin a.
assume('gt_mn=g_mn+eps*h_mn')                                      # ok — Suppose the perturbed metric is `gt_mn = g_mn + eps*h_mn`.
assume(q"g is Kerr metric in Boyer-Lindquist coordinates; h is static and axisymmetric, from a scalar field coupling; eps is small")  # ok — Suppose g is the Kerr metric in Boyer-Lindquist coordinates, h is static and axisymmetric and comes from a scalar field coupling, and eps is small.
pls(Ben,"derive effective potential for radial motion to first order in eps")  # ok — Ben, please derive the effective potential for the radial motion to first order in eps.
pls(Ben,"state exact condition for existence of circular orbits")  # ok — Ben, please state the exact condition for circular orbits to exist.
pls(Ben,"find first-order shift of ISCO radius, in terms of M, a and unperturbed ISCO radius r_0")  # ok — Ben, please find the first-order shift of the ISCO radius, in terms of M, a and the unperturbed ISCO radius r_0.
---
msg(Ben,Ana,1,re(Ana1))                                             # ok — Ben's 1, an answer to Ana1
assume('m=1')                                                       # ok — Suppose the particle's mass is 1: `m = 1`.
ent("Neumann series",'gti(i,j)=gi(i,j)-eps*hu(i,j)',"first order in eps")  # ok — By the Neumann series, to first order in eps, the inverse of the perturbed metric is `gti(i,j) = gi(i,j) - eps*hu(i,j)`.
q"gi and gti are inverses of g and gt; hu is h with both indices raised using g; d1 and d2 are first and second derivative in r"  # ok — Notation: `gi` and `gti` are the inverses of `g` and `gt`; `hu` is `h` with both indices raised using `g`; `d1` and `d2` are the first and second derivative in r.
supp(q"perturbation is static and axisymmetric",q"E=-p_t and L=p_p are conserved")  # ok — That the perturbation is static and axisymmetric is a reason to believe that `E = -p_t` and `L = p_p` are conserved.
'gti(r,r)*p_r^2+gti(t,t)*E^2-2*gti(t,p)*E*L+gti(p,p)*L^2=-1'        # ok — The mass-shell condition in the equatorial plane is `gti(r,r)*p_r^2 + gti(t,t)*E^2 - 2*gti(t,p)*E*L + gti(p,p)*L^2 = -1`.
'Veff=gti(r,r)*(1+gti(t,t)*E^2-2*gti(t,p)*E*L+gti(p,p)*L^2)'        # ok — The effective potential is `Veff = gti(r,r)*(1 + gti(t,t)*E^2 - 2*gti(t,p)*E*L + gti(p,p)*L^2)`.
'rd=gti(r,r)*p_r'                                                   # ok — The radial velocity is `rd = gti(r,r)*p_r`.
ent(grp(Ben1.5,Ben1.6,Ben1.7),'rd^2=-Veff')                         # ok — From lines 5, 6 and 7: `rd^2 = -Veff`.
'B=1+gi(t,t)*E^2-2*gi(t,p)*E*L+gi(p,p)*L^2'                         # ok — B is `1 + gi(t,t)*E^2 - 2*gi(t,p)*E*L + gi(p,p)*L^2`.
'C=hu(t,t)*E^2-2*hu(t,p)*E*L+hu(p,p)*L^2'                           # ok — C is `hu(t,t)*E^2 - 2*hu(t,p)*E*L + hu(p,p)*L^2`.
ent(grp(Ben1.2,Ben1.6,Ben1.9,Ben1.10),'Veff=V0+eps*V1 & V0=gi(r,r)*B & V1=-(hu(r,r)*B+gi(r,r)*C)',"first order in eps")  # ok — From lines 2, 6, 9 and 10, to first order in eps: `Veff = V0 + eps*V1`, `V0 = gi(r,r)*B` and `V1 = -(hu(r,r)*B + gi(r,r)*C)`.
ent(Ben1.8,'Veff=0 & d1(Veff,r)=0',"circular orbit: radial velocity and acceleration vanish")  # ok — From line 8: `Veff = 0` and `d1(Veff,r) = 0`, because, for a circular orbit, the radial velocity and acceleration vanish.
supp(q"ISCO is onset of radial instability",'d2(Veff,r)=0')         # ok — That the ISCO is the onset of radial instability is a reason to believe that `d2(Veff,r) = 0`.
assume('V0=0 & d1(V0,r)=0 & d2(V0,r)=0')                            # ok — Suppose `V0 = 0`, `d1(V0,r) = 0` and `d2(V0,r) = 0`.
q"V0E, V0L, V0rE, V0rL, V0rrE, V0rrL, V0rrr, V1, V1r, V1rr are derivatives of V0 and V1 at r_0, E_0, L_0 of unperturbed ISCO; E and L in a name mean partial derivative, r means d/dr"  # ok — Notation: `V0E, V0L, V0rE, V0rL, V0rrE, V0rrL, V0rrr, V1, V1r, V1rr` are derivatives of V0 and V1 at r_0, E_0, L_0 of the unperturbed ISCO. The letters E and L in a name mean a partial derivative; r means d/dr.
ent(grp(Ben1.11,Ben1.12,Ben1.14),'V0E*dE+V0L*dL=-eps*V1 & V0rE*dE+V0rL*dL=-eps*V1r',"first order in eps")  # ok — From lines 11, 12 and 14, to first order in eps: `V0E*dE + V0L*dL = -eps*V1` and `V0rE*dE + V0rL*dL = -eps*V1r`.
ent(grp(Ben1.11,Ben1.13,Ben1.14),'V0rrr*dr+V0rrE*dE+V0rrL*dL=-eps*V1rr',"first order in eps")  # ok — From lines 11, 13 and 14, to first order in eps: `V0rrr*dr + V0rrE*dE + V0rrL*dL = -eps*V1rr`.
ent(Ben1.16,'dE=-eps*(V1*V0rL-V0L*V1r)/(V0E*V0rL-V0L*V0rE) & dL=-eps*(V0E*V1r-V0rE*V1)/(V0E*V0rL-V0L*V0rE)',"Cramer rule")  # ok — From line 16, by Cramer's rule: `dE = -eps*(V1*V0rL - V0L*V1r)/(V0E*V0rL - V0L*V0rE)` and `dL = -eps*(V0E*V1r - V0rE*V1)/(V0E*V0rL - V0L*V0rE)`.
ent(grp(Ben1.17,Ben1.18),'dr=-(V0rrE*dE+V0rrL*dL+eps*V1rr)/V0rrr')  # ok — From lines 17 and 18: `dr = -(V0rrE*dE + V0rrL*dL + eps*V1rr)/V0rrr`.
---
msg(Ana,Ben,2,re(Ben1))                                      # ok — Ana's 2, an answer to Ben1
agree(11)                                                    # ok — Ana agrees with line 11 of Ben1.
agree(19)                                                    # ok — Ana agrees with line 19 of Ben1.
clr(12,q"exact condition for existence of circular orbits")  # ok — Ana says line 12 of Ben1 is unclear. What is unclear: the exact condition for existence of circular orbits.
retr(Ana1.6)                                                 # ok — Ana takes back line 6 of her first message (the request for the first-order shift in terms of M, a and r_0).
pls(Ben,"find first-order shift of ISCO radius for general h, in terms of M, a, r_0 and h with its r-derivatives at r_0")  # ok — Ben, please find the first-order shift of the ISCO radius for a general h, in terms of M, a, r_0 and h with its r-derivatives at r_0.
hyp(q"hu(r,r) drops out of dr: B and its first two r-derivatives vanish at r_0")  # ok — Ana's hypothesis: `hu(r,r)` drops out of `dr`: B and its first two r-derivatives vanish at r_0.
pls(Ben,"test line 19 of Ben1 numerically on exact case h=dg/dM, where dr must equal eps times derivative of ISCO radius in M at fixed a")  # ok — Ben, please test line 19 of Ben1 numerically on the exact case `h = dg/dM`, where `dr` must equal eps times the derivative of the ISCO radius with respect to M at fixed a.
---
msg(Ben,Ana,2,re(Ana2))                                         # ok — Ben's 2, an answer to Ana2
ent("geodesic equation",'d1(gt_pp,r)*W^2+2*d1(gt_tp,r)*W+d1(gt_tt,r)=0',"circular orbit with angular velocity W")  # ok — By the geodesic equation, for a circular orbit with angular velocity W: `d1(gt_pp,r)*W^2 + 2*d1(gt_tp,r)*W + d1(gt_tt,r) = 0`.
ent(grp(Ben1.12,Ben2.1),'d1(gt_tp,r)^2-d1(gt_tt,r)*d1(gt_pp,r)>=0 & gt_tt+2*gt_tp*W+gt_pp*W^2<0',"circular orbit exists when W is real and orbit is timelike")  # ok — From line 12 of Ben1 and line 1 here: `d1(gt_tp,r)^2 - d1(gt_tt,r)*d1(gt_pp,r) >= 0` and `gt_tt + 2*gt_tp*W + gt_pp*W^2 < 0`; that is, a circular orbit exists when W is real and the orbit is timelike.
ent(Ben1.14,'B=0 & d1(B,r)=0 & d2(B,r)=0',"V0=gi(r,r)*B and gi(r,r) is not zero")  # ok — From line 14 of Ben1: `B = 0`, `d1(B,r) = 0` and `d2(B,r) = 0`, because `V0 = gi(r,r)*B` and `gi(r,r)` is not zero.
agree(6)                                                        # ok — Ben agrees with line 6 of Ana2.
ent(grp(Ben2.3,Ben1.11),'V1=-gi(r,r)*C & V1r=-d1(gi(r,r)*C,r) & V1rr=-d2(gi(r,r)*C,r)',"B and its first two r-derivatives vanish at r_0")  # ok — From line 3 here and line 11 of Ben1, because B and its first two r-derivatives vanish at r_0: `V1 = -gi(r,r)*C`, `V1r = -d1(gi(r,r)*C,r)` and `V1rr = -d2(gi(r,r)*C,r)`.
will("test line 19 of Ben1 numerically on exact case h=dg/dM")  # ok — Ben will test line 19 of Ben1 numerically on the exact case `h = dg/dM`.
---
msg(Ana,Ben,3,re(Ben2))   # ok — Ana's 3, an answer to Ben2
agree(2)                  # ok — Ana agrees with line 2 of Ben2.
agree(5)                  # ok — Ana agrees with line 5 of Ben2.
ack(Ben2)                 # ok — Ana confirms that Ben2 arrived.
yn(can(Ben,"also give dr for h from a specific scalar field coupling"))  # ok — Ana asks: can Ben also give `dr` for an h from a specific scalar field coupling?
```

#### 4.13.3 A mathematics problem: a Killing field on a positively curved manifold

**The problem.** Let M be compact and orientable, of even dimension n = 2k, with strictly positive sectional curvature, and let X be a Killing vector field with finitely many isolated zeros. Show that the sum of the indices of the zeros is the Euler characteristic χ(M); show how the flow of X constrains the odd Betti numbers of M; and, for n = 4 and M not homeomorphic to a sphere, bound the number of zeros.

**The conversation.** The same shape. Ana poses the problem, Ben posts a solution one step to a line, Ana reviews. A theorem is named as the premises of a step (`ent("Poincare-Hopf theorem",…)`: a quote in the place of a group); `supp` gives a reason to believe a claim without deriving it; Ana's `err(8,…)` corrects Ben's line 8, and Ben answers with `retr(Ben1.8)` and a better argument; at the end Ben says what he does not know with `unk(…)`. It is 833 tokens on `cl100k` (6.10).

```dialogue
msg(Ana,Ben,1)                                                   # ok — Ana's 1
assume(q"M is compact, orientable Riemannian manifold of even dimension n=2*k with strictly positive sectional curvature")  # ok — Suppose M is a compact, orientable Riemannian manifold of even dimension n = 2k with strictly positive sectional curvature.
assume(q"X is smooth Killing field on M with finite, non-empty set of isolated zeros p_1, ..., p_m")  # ok — Suppose X is a smooth Killing field on M with a finite, non-empty set of isolated zeros p_1, ..., p_m.
pls(Ben,"prove: sum of indices of zeros of X equals Euler characteristic of M")  # ok — Ben, please prove that the sum of the indices of the zeros of X equals the Euler characteristic of M.
pls(Ben,"show how flow of X constrains odd Betti numbers of M")  # ok — Ben, please show how the flow of X constrains the odd Betti numbers of M.
pls(Ben,"for n=4 and M not homeomorphic to sphere, give strict bounds on m")  # ok — Ben, please give strict bounds on m for n = 4 when M is not homeomorphic to a sphere.
---
msg(Ben,Ana,1,re(Ana1))                                       # ok — Ben's 1, an answer to Ana1
ent("Poincare-Hopf theorem",'sum(ind(X,p_i),i,1,m)=chi(M)',"compact manifold, isolated zeros")  # ok — By the Poincare-Hopf theorem (compact manifold, isolated zeros): `sum(ind(X,p_i),i,1,m) = chi(M)`.
supp(q"X is Killing, so flow of X is isometry",q"Jacobian J of X at p_i is skew-symmetric")  # ok — That X is Killing, so that its flow is an isometry, is a reason to believe that the Jacobian J of X at p_i is skew-symmetric.
supp(q"J is non-degenerate skew-symmetric matrix of even size",'det(J)>0')  # ok — That J is a non-degenerate skew-symmetric matrix of even size is a reason to believe that `det(J) > 0`.
ent(grp(Ben1.2,Ben1.3),'ind(X,p_i)=1',"index of non-degenerate zero is sign of det J")  # ok — From lines 2 and 3, because the index of a non-degenerate zero is the sign of det J: `ind(X,p_i) = 1`.
ent(grp(Ben1.1,Ben1.4),'m=chi(M)')                            # ok — From lines 1 and 4: `m = chi(M)`.
ent("Synge theorem",q"M is simply connected","compact, orientable, even dimension, positive sectional curvature")  # ok — By Synge's theorem (compact, orientable, even dimension, positive sectional curvature): M is simply connected.
ent(Ben1.6,'b_1=0')                                           # ok — From line 6: `b_1 = 0`.
ent(grp(Ben1.7,"Poincare duality"),q"all odd Betti numbers of M vanish")  # ok — From line 7 and Poincare duality: all odd Betti numbers of M vanish.
'chi(M)=b_0-b_1+b_2-b_3+b_4'                                  # ok — `chi(M) = b_0 - b_1 + b_2 - b_3 + b_4`.
ent(grp(Ben1.5,Ben1.8,Ben1.9),'m=2+b_2',"n=4, b_0=1, b_4=1")  # ok — From lines 5, 8 and 9, with n = 4, `b_0 = 1` and `b_4 = 1`: `m = 2 + b_2`.
ent(Ben1.10,'b_2>=1',"M not homeomorphic to S^4")             # ok — From line 10, because M is not homeomorphic to S^4: `b_2 >= 1`.
ent(grp(Ben1.10,Ben1.11),'m>=3')                              # ok — From lines 10 and 11: `m >= 3`.
q"CP^2 admits positive sectional curvature and has b_2=1"     # ok — CP^2 admits positive sectional curvature and has `b_2 = 1`.
---
msg(Ana,Ben,2,re(Ben1))                                # ok — Ana's 2, an answer to Ben1
agree(5)                                               # ok — Ana agrees with line 5 of Ben1.
clr(3,q"why is J non-degenerate at an isolated zero")  # ok — Ana says line 3 of Ben1 is unclear. What is unclear: why J is non-degenerate at an isolated zero.
err(8,q"duality pairs b_i with b_(n-i): it gives b_(n-1)=0 from b_1=0 and says nothing on b_3 when n>=6")  # ok — Ana says line 8 of Ben1 has an error: duality pairs b_i with b_(n-i). It gives b_(n-1) = 0 from b_1 = 0 and says nothing about b_3 when n >= 6.
clr(11,q"why b_2=0 gives sphere")                      # ok — Ana says line 11 of Ben1 is unclear. What is unclear: why b_2 = 0 gives a sphere.
sug("use Hsiang-Kleiner theorem for part 3")           # ok — Ana suggests using the Hsiang-Kleiner theorem for part 3.
q"Hsiang-Kleiner theorem: compact orientable 4-manifold with positive sectional curvature and isometric circle action is homeomorphic to S^4 or CP^2"  # ok — Ana states the Hsiang-Kleiner theorem: a compact orientable 4-manifold with positive sectional curvature and an isometric circle action is homeomorphic to S^4 or CP^2.
pls(Ben,"restate parts 2 and 3 with these")            # ok — Ben, please restate parts 2 and 3 with these.
---
msg(Ben,Ana,2,re(Ana2))                                   # ok — Ben's 2, an answer to Ana2
q"zero set of Killing field is totally geodesic with tangent space ker J at p_i, so isolated zero gives ker J=0"  # ok — Ben states: the zero set of a Killing field is totally geodesic, with tangent space ker J at p_i, so an isolated zero gives `ker J = 0`.
retr(Ben1.8)                                              # ok — Ben takes back line 8 of Ben1.
agree(3)                                                  # ok — Ben agrees with line 3 of Ana2.
ent(Ana2.6,q"M is homeomorphic to S^4 or CP^2","closure of flow of X is torus, which contains isometric circle")  # ok — From line 6 of Ana2, because the closure of the flow of X is a torus, which contains an isometric circle: M is homeomorphic to S^4 or CP^2.
ent(grp(Ben2.4,Ben1.5),'chi(M)=3 & m=3',"M is not S^4, so M is CP^2 with chi(CP^2)=3")  # ok — From line 4 here and line 5 of Ben1, because M is not S^4, so M is CP^2 with `chi(CP^2) = 3`: `chi(M) = 3` and `m = 3`.
ent(Ben1.7,'b_1=0 & b_3=0',"n=4: duality gives b_3=b_1")  # ok — From line 7 of Ben1, because for n = 4 duality gives `b_3 = b_1`: `b_1 = 0` and `b_3 = 0`.
unk(q"all odd Betti numbers vanish for n>=6")             # ok — Ben does not know whether all odd Betti numbers vanish for n >= 6.
---
msg(Ana,Ben,3,re(Ben2))              # ok — Ana's 3, an answer to Ben2
agree(1)                             # ok — Ana agrees with line 1 of Ben2.
agree(5)                             # ok — Ana agrees with line 5 of Ben2.
agree(6)                             # ok — Ana agrees with line 6 of Ben2.
retr(Ana2.4)                         # ok — Ana takes back line 4 of Ana2 (her question about line 11 of Ben1).
sug("mark part 2 for n>=6 as open")  # ok — Ana suggests marking part 2 for n >= 6 as open.
```

---

## Part 5. Limits, and choices left to the Owner

### 5.1 What SILEX does not do

- **A checker cannot see inside a quote.** It checks roots, places, kinds, names and the header. It does not know that *"db server"* and *"database server"* are one thing: two quotes name the same referent only when their text is the same. Inside one conversation, agree on one wording, or define a label once (`o1"database server"`) and use `o1`.
- **Tense, aspect and degree are not structure.** A time root places a claim or an act in time. *Had been*, *is going to*, *almost*, *rather* stay in the English of a quote, or are dropped. `prob` and `hi` `mid` `lo` carry likelihood and intensity, and nothing finer.
- **Most relations are English.** In `is(x,"above",y)` and `is(x,"owned by",y)` the relation is a quote, so a checker cannot tell that *above* and *below* are opposites. A relation gets a root only where many lines need it (`loc`, for place); this lexicon has none for space, ownership or kinship.
- **Only the one best has a root.** `best`, `max` and `min` give one member or one number. *The three largest* is English in a quote: `what(filt("servers","three with least free memory"))`.
- **Tone is not carried.** Politeness, emotion, humour and style are for English. SILEX is for work between agents. The hatch `q"…"` carries any claim the roots cannot say, and a quote carries any act.
- **There are no pronouns and no ellipsis.** There is no *it*, *they* or *the same*. A name (a label, an agent, a message line) takes the place of a pronoun, and `_` marks a place left open.
- **A program or a formula is carried, not understood.** For a program the checker goes as far as Python's own syntax check, and only for Python; the other fifteen languages of `code` are carried with no check. For a formula it checks the form, the binding of the joins and the brackets. It does not know whether a program does what its sender says or ever stops, whether a formula is true, or what a function name that is not on the list of 3.3 means: `'sqt(x)=2'` is accepted. A formula claim on a line is asserted; whether the writer meant it as a proposal is not tested.
- **A rule holds only as far as something enforces it.** Writers that do not run the checker slip on rules it would catch: the no-article rule (1.4.5), line numbers (1.1, 2.5) and the places of `will` (3.8). A bare line number that names another line that exists is accepted, so a miscount can change what a line says and still pass; a line reference in any root is tested, which catches a miscount only when it points past the end. Requiring a checker run is not feasible with the participants of this project (the Owner's ruling), so the text states the common slips in the places where they happen.
- **Some things have no root.** *Undefined*, *nothing to change* and *the output of a run* are English values (4.12).
- **No authority.** `must(x, A)` claims that `x` is obliged and `may(x, A)` that `x` is permitted. Nothing says who may send what, or that a sender is who it says it is. Trust and security belong outside the language. This holds most for `code(…)`: a program in a message is data, SILEX never runs it, and whether to run it, where and with what rights is for the receiver to decide. A sandbox with no network and no secrets is the safe place for a program from another agent.
- **No rule picks a winner between concurrent messages** (2.6). The language gives the means to see that messages are concurrent and the conventions for what each kind of reply means. What to do about a clash depends on the work.
- **One line is one expression.** There is no continuation. A long claim is built with `and`, `or`, `then` inside the line, or is split into several lines.
- **Names stay inside their message.** A label belongs to the message that defines it and is reached from another message as `Ana3.o1`. There are no names shared by a whole conversation, because two agents could define one at the same moment.

### 5.2 Choices for the Owner

Each is a choice that was made to finish the file. Each can go the other way.

1. **What the header means.** `msg(Ana,Ben,3)` is read as *sender, receiver(s), serial*. You wrote `mssg(zkU, zkB)`; I took that as sender and receiver. If you meant something else (a channel, a session), 2.2 changes and nothing else does.
2. **`msg`, not `mssg`.** `msg` costs 1 token where `mssg` costs 3 on two of the three vocabularies measured (6.7), which is 2 tokens per message. It is one word to change.
3. **Where the serial stands.** After the receivers (`msg(Ana,Ben,3)`), found because it is a whole number. The other choice is `msg(Ana3,Ben)`, which names the message in the first word: one comma less, but a name and a number are mixed.
4. **What `You` means with several receivers.** In a message to Ben and Cy, `pls(You,…)` asks both. To ask one, name it. `All` is everyone on the roster except the sender when the message is sent. *We* is `grp(Me,You)`.
5. **Bare quotes.** A quote without a class letter takes its kind from its place (1.4.2). That saves a letter per quote, about one token, and costs one rule to learn. The other choice is to require the letter every time.
6. **`rej` declines acts and proposals only.** To deny a claim, assert its `not`. Letting `rej` also deny claims would save a few tokens and would make one root do two jobs.
7. **Two ways to give a number**: `val(x,"RAM in GB",16)` says it of a named thing and `eq(n"queue length",500)` of no thing. One could go; both are short.
8. **Time zone.** A time without a zone is in *the zone the agents have agreed* (1.6). The other choice is UTC unless an offset is written: no agreement is needed, and every local time carries `+05:30`.
9. **No "the" in any quote**, `q"…"` included (1.4.5). "A" and "an" stay. A proper name that begins with *The* is written without it. The raw quotes of `code` and the formula quote are the exception, because they carry text that is not English (1.4.6).
10. **People and systems that are not agents.** They are quotes (`"customer"`). Only agents have names that can be senders and receivers.
11. **`msg` as a root.** It is the only root that must be the first line of a message. The other choice is a first line with no root, `Ana>Ben,3`, which is shorter and breaks the rule that every line is a root application.
12. **Relative line numbers.** In `agree(3)` the `3` is line 3 of the one message that the header's `re` names (1.5.5). It saves about 3 tokens per reference (6.7). The other choice is to write every reference in full, `agree(Ana1.3)`; full references are always valid, and are required when the header has no single whole-message `re`. `retr` is left out of the short form: it takes back the sender's own lines, never those of the message answered.
13. **Compact date-times.** `20261106T1700` and `2026-11-06T17:00` are the same time (1.6). The short form saves about 4 tokens per time (6.7). A date alone stays `2026-11-06`, because `20261106` is also a number. The other choice is one spelling only, with no loss of meaning.
14. **Ids and a closing declaration** (decided against, 4 November). The idea was short typed ids for the items of a message, one counter per sender and class (`C7` for my claim 7, `CadC7` for Cad's), and a last line in every message that lists the new ids (`dcln(C8-10,H2)`). On the Gem and God dialogue the closing lines cost 16 tokens a message (+10.8%) and the ids in place of line names save 25 tokens in all, so the whole is +8.9% where bare line numbers are −4.9% (6.7). You chose not to add it: there are neither ids nor a closing line.
15. **`code` is an act, with one quote for each line of source.** A program is the act of running it, so `pls(Ben,code(…))` asks Ben to run it and a program alone on a line is `E-KIND`; to send one with no request, `def` names it. One quote for each line keeps every indentation exact and costs 12 to 22 percent more than plain text on the three programs measured (6.8); one quote with `\n` for the line breaks costs more. The list of languages is closed (sixteen names), so that a misspelled language is `E-CODE` and not silence. Only Python is checked, because the checker is written in Python. The other choices: a program is a thing and not an act (then every run needs a `pls(Ben,"run {a1}")` and a bare `code(…)` is a line that says nothing), or one quote with escapes, or an open list of languages.
16. **Formulas in their written form, not symbol roots.** You asked whether symbols can replace *plus*, *minus* and the rest; the figures are in 6.8. On the 84 test sentences, which use these eleven roots 10 times, writing them as symbols saves 0, 0, 10 tokens (cl100k, o200k, claude1). On eight formulas they save 9%. They would also put the roots of a family one edit apart where the words are not (21 of 25 pairs against 0), so that a slip would pass the checker. A formula in its written form saves 48% on the same eight formulas, because it leaves out the root of each operator and the labels of each name (measured inside a root; without the root it saves a little more, item 17). The other choices: symbol roots, or no formula form at all (the formula stays nested roots, which a reader finds hard to follow).
17. **A formula in single quotes, with no root round it.** The quote alone saves 3.2% of the tokens of four mathematical conversations (6.10) against a root round each formula, `math("x=1")`: in `,'x=1',` the comma and the quote mark are one token on each side, and `math(` and `)` are gone. The form with a class letter, `m"x=1"`, was measured and saves less (2.7% in all, with the other two choices), because the letter keeps the quote mark apart from the comma. The costs: a second kind of quote to read, and a formula that can stand as a line with no root round it (item 18).
18. **A formula as a line by itself.** A formula claim on a line is asserted, as any claim line is, and it is the one line that is not `root(…)`. The other choice keeps the rule *every line is a root application*: it needs a root round such a line, `math('F')`, which costs 17 tokens on the 13 such lines of the four conversations (0.3%) and brings back a root for this one use.
19. **Joins inside the quote: `&` `|` `=>` `<=>`.** They replace `and(…)`, `or(…)` and `if(…)` between formulas, and give *if and only if*, which had no root. Joining saves 1.7% of the tokens of the four conversations (6.10). They cost a rule of binding (`&` before `|` before `=>` before `<=>`) and the refusal of a chain of `=>` or `<=>`, which would read two ways. The other choice: join claims with the roots.
20. **One line reference in place of a group in `ent`.** `ent(Ana1.1,Q)` for `ent(grp(Ana1.1),Q)` saves 0.3% (6.10). A whole message is refused as premises: it would need a rule for which of its lines count. The Owner ruled on 5 November that a leading dot for the sender's own lines (`.5`) and runs of lines (`Ben1.5-7`) are not wanted, because a shortened number is easier to misread; they would have added 2.9 points of saving (7.1% instead of 4.2%).

---

## Part 6. How this file was checked

### 6.1 The programs

Eight small programs were written for this job and run in a sandbox. None is part of the language.

- The **checker** reads a message one line at a time and gives each line a verdict (1.9): `ok`, or an error code with the place of the error. It does the lexing, the parsing, the places and kinds of every root, the names, the rules for quotes (no "the", no word that depends on who speaks or when, braces), the times (both spellings, 1.6), and the header. Before it checks a line it turns a bare line number into the full reference (1.5.5). For `code` it also runs Python's own syntax check (`ast`) on the lines of a Python program, and for a formula (`'…'`) it reads the formula with a small parser of its own: numbers, names, operators, brackets, functions, one comparison to a claim, and the four joins of claims (1.4.6).
- The **lexicon test** takes the example of each of the 102 roots of Part 3 and runs it.
- The **dialogue checker** reads a whole conversation, message by message: serials run 1, 2, 3 for each sender; `re` and `saw` name messages that exist; a line reference, short or full, in any root, names an earlier message (or the sender's own) and a line that exists; an `ans` answers a question; every sender and receiver is on the roster.
- The **file verifier** finds every code block of this file and runs it. A line that ends in `# ok` must be accepted; a line that ends in `# E-…` must be refused with that code.
- The **token counter** counts tokens with three public vocabularies (6.2).
- The **measuring script** writes the two test sets of 6.7 in each variant, counts them with the token counter, and checks that the long and the short spelling of a date-time are both accepted.
- The **study script** of 6.8 writes the programs and the formulas in each form, checks each with the checker, and counts them.
- The **conversion script** of 6.10 writes each choice of 6.10 in place of its alternative in the four conversations, and a second program reads the new text back (the round trip of 6.10).

### 6.2 Token counts

None of the three vocabularies is the tokenizer of a current Claude model; they are stand-ins. `cl100k` and `o200k` are OpenAI vocabularies, and `claude1` is an older Claude one. The figures show the size of the effect, not exact costs.

The test is the 84 English sentences of Part 4, each written as SILEX. Lines are written without spaces after commas.

| Counted as | cl100k | o200k | claude1 |
| --- | --- | --- | --- |
| English sentences | 700 | 698 | 685 |
| SILEX lines, no header | 955 (1.36×) | 948 (1.36×) | 1,001 (1.46×) |
| English, in 11 groups of eight | 701 | 698 | 758 |
| SILEX, 11 messages of eight lines, headers counted | 1,042 (1.49×) | 1,036 (1.48×) | 1,173 (1.55×) |
| SILEX, one message per sentence, header on each | 1,627 (2.32×) | 1,620 (2.32×) | 1,757 (2.56×) |

- **Against English, SILEX is longer.** Without a header it is about 1.36 times the English on `cl100k`. A line spells out structure that an English sentence leaves to the reader, and brackets, commas and quote marks cost tokens. The aim of SILEX is meaning that a checker can test, not a shorter text than English.
- **A header costs about 8 tokens.** One sentence sent alone, with its header, is 2.32 times the English. Eight lines sent together amortize it: 1.49 times.
- **Spaces cost tokens.** On a sample of lines the same text measured 105 tokens with no spaces, 111 with a space after each comma, and 120 with spaces inside the brackets as well (`cl100k`). Spaces are allowed (1.1) and not used here.
- **The header root, bare line numbers and short date-times** are measured on two other sets of text in 6.7, the programs and formulas in 6.8, and the formula quote, the joins and `ent` in 6.10.
- **Reading the grammar costs tokens too.** Parts 0 to 3, which an agent reads to use the language, are 22,188 tokens (`cl100k`). 1.5.5 and the compact date-times of 1.6 are 760 of them; a message saves 5 to 9 tokens with them (6.7), so an agent that reads Parts 0 to 3 in full for every conversation gets those back after roughly 84 to 152 messages. 1.4.6 is 1,775 tokens. A formula saves about 13 tokens (6.8, 6.10), so a conversation with about 137 formulas pays that reading back; a program saves none, and `code` is there for what could not be sent before, not to save tokens. An agent that holds the grammar as standing, cached instructions pays the reading once. The Gem and God dialogue (1,265 tokens) is about an eighteenth of one reading of Parts 0 to 3.
- **Word choice was measured.** In place, a root with its opening bracket costs 1.5 tokens on average in `cl100k`, 1.6 in `o200k` and 2.1 in `claude1`. The roots are short plain words; none was changed to suit one vocabulary.

### 6.3 What was run

| Test | What it covered | Result |
| --- | --- | --- |
| Lexicon examples | one example for each of 102 roots | all accepted |
| Test sentences | 84 English sentences written as SILEX | all accepted |
| Code blocks of this file | 52 blocks, 459 lines | each verdict equals its comment |
| Conversations | 15 conversations, 62 messages | no problem found |
| Self-test of the checker | 345 checks: the 102 examples above, 177 single lines (names, kinds, quotes, times, programs, formulas and joins, line references, accepted and refused), 45 messages and 21 conversations | every verdict as the rule says |
| A real conversation | the Owner's Gem and God dialogue: 9 messages, 101 lines after the headers | the checker refused two lines (a quote with *the*; a speech act inside `ans`); a third named a message inside a quote and was changed too; after that all accepted. Rewritten with 22 bare line numbers and expanded again by the checker: the same text as the full form, line for line |
| Mathematical conversations | the 6 problems of 4.13; the 4 long conversations of 6.10 (two of them are in 4.13), 28 messages and 197 lines, each written with this grammar and with the alternatives of 6.10, the first read back into the second by a program | all accepted; the text read back is the text written with the alternatives, line for line |
| Programs and formulas of 6.8 | 3 Python programs, each also with a syntax error added, and 8 formulas, in each form of 6.8 | every verdict as the rule said when the figures were made |

Lines marked `E-…` in this file are examples of refusals: each was run and refused with the code shown.

### 6.4 Roots one edit apart

The likeliest slip is one letter: a root changed into another that is one edit away (a letter changed, added, dropped, or two letters swapped). There are 30 such pairs among the roots and atoms, 20 between two roots and 10 between a root and an atom. A root always has brackets and an atom never does, so a slip between a root and an atom is refused (`E-ARITY` or `E-LEX`): `not`~`now`, `not`~`no`, `pow`~`now`, `min`~`mid`, `loc`~`lo`, `know`~`now`, `to`~`no`, `to`~`lo`, `now`~`no`, `no`~`lo`.

For two roots, the table says what refuses a slip. A pair is kept apart by the number of places or by their kinds when no argument list is accepted by both. Not every pair is kept apart by kinds alone: `and` and `ans` stay open when every argument is a reference (for example `and(Ana1,Ana2)` and `ans(Ana1,Ana2)`). The pair `rej` and `re` is kept apart by position: `re` stands only inside `msg(…)` and `rej` only as a line.

| Pair | Places of each | Kept apart by |
| --- | --- | --- |
| `and` `ans` | `and`: (Cl, Cl …) → Cl; (Ac, Ac …) → Ac<br>`ans`: (Rf\|Q, Va) → Ln | kinds of the places, except when every argument is `Rf` |
| `or` `for` | `or`: (Cl, Cl …) → Cl; (Ac, Ac …) → Ac<br>`for`: (Du, X) → =2 | kinds of the places |
| `if` `is` | `if`: (Cl, X) → =2<br>`is`: (Va, Cr) → Cl; (Va, Cr, Va) → Cl | kinds of the places |
| `most` `must` | `most`: (Gr, Cr) → Cl<br>`must`: (Th\|Gr, Ac) → Cl; (Cl) → Cl | kinds of the places |
| `many` `may` | `many`: (Gr, [Cr]) → Cl<br>`may`: (Th\|Gr, Ac) → Cl; (Cl) → Cl | kinds of the places |
| `plus` `pls` | `plus`: (Nu, Nu …) → Nu; (Tm, Du) → Tm; (Du, Du …) → Du; (Gr, Va) → Gr<br>`pls`: (Th\|Gr, Ac\|Cl) → Ln; (Ac\|Cl) → Ln | kinds of the places |
| `sum` `sug` | `sum`: (Gr, Cr) → Nu<br>`sug`: (Cl\|Ac) → Ln | number of places |
| `cnt` `ent` | `cnt`: (Gr) → Nu<br>`ent`: (Gr\|Rf, Cl, [Cr]) → Cl | number of places |
| `max` `may` | `max`: (Gr, Cr) → Nu; (Nu, Nu …) → Nu<br>`may`: (Th\|Gr, Ac) → Cl; (Cl) → Cl | kinds of the places |
| `min` `fin` | `min`: (Gr, Cr) → Nu; (Nu, Nu …) → Nu<br>`fin`: (Ac, [Cr]) → Cl | kinds of the places |
| `pct` `act` | `pct`: (Nu, Nu) → Nu<br>`act`: (Th\|Gr, Ac) → Cl | kinds of the places |
| `act` `ack` | `act`: (Th\|Gr, Ac) → Cl<br>`ack`: (Rf …) → Ln | kinds of the places |
| `act` `at` | `act`: (Th\|Gr, Ac) → Cl<br>`at`: (Tm\|Cl, X) → =2 | kinds of the places |
| `then` `when` | `then`: (Ac, Ac …) → Ac<br>`when`: (Cl) → Tm | number of places |
| `ask` `ack` | `ask`: (Th, Q) → Ac<br>`ack`: (Rf …) → Ln | kinds of the places |
| `may` `say` | `may`: (Th\|Gr, Ac) → Cl; (Cl) → Cl<br>`say`: (Th\|Gr, Cl\|Q\|Ln) → Cl | kinds of the places |
| `say` `saw` | `say`: (Th\|Gr, Cl\|Q\|Ln) → Cl<br>`saw`: (Rf …) → Hd | position: a header detail stands only inside `msg(…)`, a line root only as a line |
| `rej` `rep` | `rej`: (Ac\|Cl, [Cl]) → Ln<br>`rep`: (Nu, X) → =2 | kinds of the places |
| `rej` `re` | `rej`: (Ac\|Cl, [Cl]) → Ln<br>`re`: (Rf …) → Hd | position: a header detail stands only inside `msg(…)`, a line root only as a line |
| `rep` `re` | `rep`: (Nu, X) → =2<br>`re`: (Rf …) → Hd | position: a header detail stands only inside `msg(…)`, a line root only as a line |

### 6.5 What was not run

- **The tokenizer of a current Claude model.** Section 6.2 uses stand-ins.
- **A long real conversation.** The conversations of this file are written to show the rules, and one real conversation of nine messages was run (6.3). A long one, with many agents writing at once, was not.
- **Readers.** The readers of 6.6 read a text that had no 1.4.6, no 1.5.5 and no compact date-times. No reader has read those.
- **Programs.** Only the syntax of Python is checked, with the `ast` module of the Python that runs the checker: a program for an older or a newer Python could be refused or accepted wrongly. No program was run. *Accepted* means that it parses and is in the form of 1.4.6, not that it works. The three programs of 6.8 are in Python, so the token figures are for Python.
- **Formulas.** The formula parser is the checker's own, and has no second implementation. Function names are not checked, and neither is the truth of a formula. The binding of `&` `|` `=>` `<=>` and the refusal of chains of `=>` and `<=>` are the drafter's choice and were tested only on cases the drafter wrote.
- **Writers.** Whether agents that write SILEX make more slips with a bare line number or a short date-time than with the full forms was not tested, and the same holds for programs and formulas: whether a writer remembers the doubled quote mark inside a program, or the `*` in `2*x`. A bare number is as easy to miscount as `Ana1.3`: a number that names another line that exists is accepted, as a full name would be.
- **A second implementation.** One checker, written by the drafter, ran all the tests. A different reader of this file could find a rule that the checker and the text both state wrongly.

### 6.6 Readers who had not seen SILEX

Two readers who had never seen SILEX were given the text and nothing else (it was shorter than this one: it had no 1.4.6, 1.5.5 or compact date-times). The first explained 16 lines and messages in English (what each says, what it asserts and what it only mentions) and gave the verdict of 8 faulty lines; the second explained 18 lines, messages and headers, among them which of four messages are concurrent. They were agents of the same kind as the drafter, so this is a test of the text, not of independent humans.

- **What they got right.** Almost every reading was right: negated quantifiers, conditional requests, reported speech, counterfactuals, groups, nested quantifiers, the header with `re`, `saw` and `pri`, concurrent messages, and all eight verdicts (`E-KIND`, `E-NAME`, `E-HEAD`, `E-QUOTE`, `E-ARITY`, `E-HEAD`, `E-QUOTE`, `E-KIND`). One of the eight, `E-QUOTE` for a quote with *the*, had to be inferred, because the text did not name the code; 1.4.5 and 1.9 name it.
- **What they could not settle from the text.** Both listed the same gaps; each is stated in this file: whether an untimed claim holds at `now` and what `say` does with tense (1.8); what is asserted and what is only mentioned inside `cause`, `supp`, `ent`, `would`, `err` and `clr` (1.8, 2.5, 3.10); whether `fin` is a state or an event and what a clock time is (1.6, 3.6); `rep` and `during` (3.9); `rng` (3.3); how a bare quote is read in a root with several forms (1.4.2); `to` against "the others still receive it" (2.4, 3.12); whether a header receiver must already be on the roster (2.2); whether a line that points at a message puts it in order (2.3); who must agree to a `sug` (2.5, 2.6); and which line `rej` declines when it names a whole message (2.5).
- **Two true contradictions.** The text said a first message with no `re` or `saw` was concurrent with every other message, which the order rule itself contradicts (2.3, 2.6); and *we* was glossed both as `All` and as `grp(Me,You)`, although `All` leaves out the sender (1.7, 4.6). Both are settled in the text. Two test sentences were reworded because their English said more than the line does (*we agreed* became *we plan*, *the cause is unknown* became *I do not know the cause*).
- **What this does not show.** Two readers are a small sample, and they did not write SILEX. Whether other agents can write it from this file alone is not yet tested.

### 6.7 The header, line numbers and date-times, measured

Three spellings were counted against their alternatives: the header root `msg` (against `mssg`), a bare line number for a line of the one message `re` names (1.5.5; against the full reference), and the short ISO date-time (1.6; against the long one). Each was counted on two sets of text with the three stand-in vocabularies of 6.2: the 84 sentences of Part 4, in 11 messages of eight lines with their headers; and the Owner's Gem and God dialogue, 9 messages with 101 lines after the headers and 22 line references, after three lines were changed (6.3). A cell gives the change in tokens on `cl100k`, `o200k` and `claude1`, in that order; a minus sign is a saving.

| Change | 84 sentences, 11 messages | Gem and God, 9 messages |
| --- | --- | --- |
| `msg` for `mssg` | −22, −22, −11 (−2.1% on `cl100k`) | −18, −18, −9 (−1.3%) |
| bare line numbers | none in this set | −66, −66, −72 (−4.9%): 22 numbers, about 3 tokens each |
| short date-times | −32, −32, −32 for 8 times: 4 tokens each | none in this set |
| all three | −54, −54, −43 (−5.1%) | −84, −84, −81 (−6.2% on `cl100k`, −5.3% on `claude1`) |

`msg` is one token on all three vocabularies; `mssg` is three on `cl100k` and `o200k` and two on `claude1`. The 8 sentences that have a time were run with the long and with the short date-time, and both were accepted. The Gem and God dialogue was run in full form and in short form, and the checker's own expansion of the short form gives the full form again, line for line.

**Aliases.** An alias is taken only after a measured benefit. Seven aliases besides `msg` were counted (the table), and none has one. Put in place together they change the two sets by −6, −5 and −3 tokens (about 0.3%), and `bef` costs a token more.

| Alias | Uses in the two sets | Change in tokens | One edit away | Why it was not taken |
| --- | --- | --- | --- | --- |
| `h` for `hyp` | 42 | 0, 0, 0 | `hi` (an atom) | `hyp(` is one token in place already |
| `ag` for `agree` | 12 | 0, 0, 0 | `at`, `avg` | the same |
| `asm` for `assume` | 1 | 0, −1, −1 | `ask` | nothing to save |
| `rt` for `retr` | 2 | −2, 0, −2 | `re`, `at` | a token a use on two vocabularies; a slip is refused (`re` in a body is `E-HEAD`, and `at` takes two places) |
| `cs` for `cause` | 9 | −5, −5, 0 | `is` | `cs("cache layer","outage")` and `is("cache layer","outage")` are both accepted and mean different things: a slip between a cause and a property would pass |
| `bef` for `before` | 1 | +1, +1, 0 | `bel`, `def` | costs a token |
| `dur` for `during` | 1 | 0, 0, 0 | none | nothing to save |

**Other ideas, measured on the Gem and God dialogue.**

| Idea | Change in tokens | Why it was not taken |
| --- | --- | --- |
| One `agree` for several lines: `agree(1,2,3)` | −12, −12, −18 (−0.9%) | a line would carry several acts, and `retr` or `err` could not name one of them; line numbers would shift |
| Leave out `re` when the lines already name the messages | −28, −28, −39 (−2.1%); 7 of the 8 messages with a `re` | a message with no `re` cannot use bare line numbers, which save more |
| Short ids with a closing declaration (`C7`, `CadC7`, and a last line `dcln(C1-2,H4,Q1)`; the Owner's idea) | the closing lines +144, +144, +176 (+10.8%); ids in place of line names −25, −25, −25; together +119, +119, +151 (+8.9%) | the closing line costs 16 tokens a message on this dialogue, far more than the ids save. Its gain is not tokens: a reader sees that a message was cut short or a count was missed. Not added, by the Owner's decision (5.2, item 14) |

**What the numbers say.** A cut of 20% is out of reach by changing spellings. If every root were a single letter, the sentences would shrink by 2.6% (`cl100k`; 2.5% on `o200k`, 0.3% on `claude1`) and the dialogue by 1.2% (1.1%, 0.1%), because most roots are one token already. If every root name were deleted, which would leave no language, they would shrink by 17.7% and 16.8% on `cl100k`. The rest of a message is the English inside quotes (about 16% of the sentences and 31% of the dialogue on `cl100k`), the header (8% of both), and brackets, commas, quote marks, names and references. Saving more would mean saying less: that is a choice between information and tokens, and SILEX keeps the information.

**Limits of the figures.** The vocabularies are stand-ins (6.2). The 84 sentences are not a conversation and have almost no references, so they show the header and the times; the dialogue has the references and no times. A bare line number saves tokens and does not make a miscount easier to see (6.5).

### 6.8 Programs and formulas, measured

On 4 November you asked whether a program can be sent inside SILEX, and whether symbols can stand for *plus*, *minus* and the rest. The answers are the root `code` and the formula quote (1.4.6). The figures use the stand-in vocabularies of 6.2 and a small set of text written for this check: three Python programs of 5, 14 and 25 lines, and eight formulas.

**Programs.** Each program written four ways. A cell gives the tokens on `cl100k`, `o200k` and `claude1`, then the change against plain text on `cl100k`.

| Written as | 5 lines | 14 lines | 25 lines |
| --- | --- | --- | --- |
| plain text | 40, 40, 49 | 102, 102, 115 | 179, 179, 183 |
| in a fence | 45, 45, 54 (+12%) | 106, 106, 120 (+4%) | 183, 183, 188 (+2%) |
| `code("python","line",…)`, one quote for each line | 48, 49, 58 (+20%) | 124, 124, 134 (+22%) | 200, 202, 208 (+12%) |
| `code("python","…\n…")`, one quote with `\n` for the line breaks | 50, 52, 59 (+25%) | 130, 132, 139 (+27%) | 207, 211, 221 (+16%) |

- **Plain text is the shortest, and a checker cannot read it.** It has no start, no end and no language, and a quote mark or a brace in it would break a line of SILEX.
- **One quote for each line, the form of `code`, costs 12 to 22 percent more than plain text.** The cost is the language name, the quote marks and the commas. It keeps every indentation exactly, which Python depends on, and lets the checker name the line of a mistake.
- **One quote with `\n` for the line breaks costs more on all three programs**, because the breaks and the backslashes are tokens of their own. It was not taken.
- **A fence is shorter than `code`, and is how a document marks a program.** SILEX has no fence: a line is one root application, and a fence is not one.

**Formulas.** Eight formulas: a quadratic equation, the square of a sum, the quadratic formula, a sum of two fractions, a percentage, a power of two, an inequality and a short expression. Each is written as the roots of Part 3, as symbols used as roots, and as one quote inside a root, `math("…")`. The cells give the total for the eight on `cl100k`, `o200k` and `claude1`.

| Written as | Tokens for the 8 formulas |
| --- | --- |
| the roots of Part 3 (`eq(plus(minus(pow(n1"x",2),times(5,n1)),6),0)`) | 191, 193, 226 |
| symbols as roots (`=(+(-(^(n1"x",2),*(5,n1)),6),0)`) | 174, 176, 189 (−9%, −9%, −16%) |
| one quote in a root (`math("x^2-5*x+6=0")`) | 99, 99, 115 (−48%, −49%, −49%) |

- **Symbols in place of the words save little.** On the 84 test sentences, which use these eleven roots 10 times, writing them as symbols saves 0, 0, 10 tokens (cl100k, o200k, claude1). On the eight formulas they save 9% (16% on `claude1`); the brackets and commas of the nesting stay.
- **Symbols would make a slip harder to see.** Among the roots for arithmetic and for comparison, 0 of the 25 pairs in a family are one edit apart as words and 21 are as symbols (`+` and `-`, `<` and `>`, `=` and `>=`). The roots of such a pair take the same kinds, so with numbers for arguments a slip passes the checker, as `cs` for `cause` would have (6.7). Symbols were not taken as roots.
- **One quote saves 48%** (about 12 tokens a formula), because it leaves out the root of each operator and the labels of each name. The saving grows with the size of the formula. Without the root round it the quote saves a further 1.7 tokens a formula (6.10), and that is the form SILEX takes.

**Limits of the figures.** The programs and formulas are a small set chosen by the drafter, and the programs are Python: other languages cost differently. Nothing here measures whether a receiver runs a program correctly, or whether a writer remembers the doubled quote mark or the `*` (6.5).

### 6.9 A test with two writers

Two AI writers each had a conversation with the drafter, relayed by the Owner with no checker run: Gds (7 messages, a five-message test and Python review) and Grk (5 messages). Each message was read by hand against the rules. Both answered the first messages correctly; the table gives the slips that came back, who made them, and where the text answers them.

| Slip | Who | Where the text answers it |
| --- | --- | --- |
| a header counted as line 1, so every reference one too high | Gds, twice | 1.1 |
| *the* in a quote (*the caller*, *the two*, *keep the raise form*) | Gds and Grk | 1.4.5 |
| `ack(2)`, a bare number | Gds, twice | 1.5.5 |
| `will(Gds,"…")`, a doer in front of `will` | Gds, twice | 3.8 |
| `{a1}` for a label of another message, where `{Dex7.a1}` was needed | Gds | 3.8 |
| `ans` on a request, and `clr` to say nothing needs changing | Gds | 2.5 |
| no way to say a value is undefined | Grk (it chose `0.0`, Gds chose `None`) | 4.12, 5.1 |
| `q"…"` where a root would do | Grk | not a language error; no change |

What went right in both: the rules for `re`, `agree` and `ans` with bare line numbers, `retr` of the right lines, `def` and `code`, formulas, `ent`, and `supp`. Both found the division by zero in the test program, and Grk, after a question, moved to the fail-fast form. The sample is two writers of one kind, twelve messages and the same drafter as reader: it shows where the text is unclear, not how often other agents slip.

### 6.10 Formulas, joins and premises, measured

On 5 November the Owner asked how formulas are best written, after four conversations between Ana and Ben on two hard problems: a test particle near a perturbed Kerr black hole, and a Killing field on a positively curved manifold. Each problem was written twice, once by the drafter (A) and once by an independent writer who had only the grammar, the checker and the problem (B). Together they are 28 messages and 197 lines; 4.13 holds the two A conversations. The figures use the stand-in vocabularies of 6.2 and count the whole text of a conversation, its lines joined by line breaks and the `---` lines left out.

Three choices of this grammar were counted against the plainest alternatives: a root round each formula, `math("x=1")`; claims joined with `and(…)`, `or(…)` and `if(…)`; and `grp(…)` round a single premise. Written with the alternatives, the four conversations are 6,439, 6,476 and 7,230 tokens (`cl100k`, `o200k`, `claude1`). A program wrote each choice in place of its alternative, and a second program read the new text back into the first: all 225 lines (197 lines and 28 headers) came back as they were, for every choice in the table, so a saving counts only where nothing is lost. The table gives the tokens saved on each vocabulary; the third column gives them when the choice is made alone, the fourth when it is added to the ones above.

| Choice | Instead of | Alone | In turn | Share of the four conversations (`cl100k`, `o200k`, `claude1`) |
| --- | --- | --- | --- | --- |
| a formula in single quotes | a root round it, `math("…")` | 206, 222, 229 | 206, 222, 229 | 3.2%, 3.4%, 3.2% |
| claims joined inside the quote | `and(…)` `or(…)` `if(…)` | 112, 102, 134 | 46, 47, 52 | 3.9%, 4.2%, 3.9% |
| one line reference in `ent` | `grp(…)` round it | 21, 21, 16 | 17, 17, 16 | 4.2%, 4.4%, 4.1% |
| **all three: this grammar** | | | **269, 286, 297** | **4.2%, 4.4%, 4.1%** |

By conversation (`cl100k`, from the alternatives to this grammar): Kerr A 1,407 to 1,326 (5.8%), Kerr B 2,183 to 2,088 (4.4%), Killing A 872 to 833 (4.5%), Killing B 1,977 to 1,923 (2.7%). Ben's messages, which carry the formulas, save more than Ana's, which are mostly English: in Kerr A 7.4% against 0.3%.

- **The quote saves about 1.7 tokens a formula** (206 over the 122 formulas). In `,'x=1',` the comma and the quote mark fuse into one token on each side; `math("x=1")` keeps `math` and the closing bracket as pieces of their own. The same saving is lost when a class letter is put in front, as in `m"x=1"`: the letter and the mark are two pieces.
- **A join saves about 4 tokens** (112 over the 28 `and(…)`, `or(…)` and `if(…)` that became joins, in 24 formulas): the `and(` and its closing bracket, a comma and one `math(` with its marks go, and ` &` comes in. The saving is smaller when it follows the quote change (46 against 112), because some of the marks it would remove are already gone.
- **One line reference saves about 2.6 tokens** (21 over 8 uses of `ent(grp(Ben1.8),…)`).

**Not taken.**

| Idea | Tokens saved | Why not |
| --- | --- | --- |
| `m"…"`, a class letter, in place of `'…'` (with the other two choices) | 175, 178, 152 (2.7%, 2.7%, 2.1%) | saves 94, 108 and 145 fewer than the quote, because the letter keeps the mark apart from the comma |
| `.5` for the sender's own lines and runs such as `Ben1.5-7` (on top of this grammar) | 459, 476, 486 (7.1%, 7.4%, 6.7%): 190, 190, 189 more | the Owner's ruling, 5 November: a shortened line number is easier to misread than a full one (1.5.5, 5.2, item 20) |
| a root round every formula that stands as a line, `math('F')` (keeps *every line is a root*) | 17, 18, 15 tokens more | not taken; item 18 of 5.2 |

**What the figures do not show.** The conversations are four, on two problems, and the drafter wrote two of them; a conversation with few formulas saves little (Killing B, 2.7%). The vocabularies are stand-ins (6.2). The saving is on the messages, and the text that explains it costs tokens to read: the paragraph on joins, its row of the table and its examples in 1.4.6 are 534 tokens (`cl100k`). The joins save 28 tokens a conversation on average (112 over four), so an agent that reads the grammar once and keeps it as standing instructions gets the 534 back after about 19 conversations; an agent that reads it again for every conversation does not. No writer has yet written `&` `|` `=>` `<=>` without having seen the examples of 1.4.6, so whether writers keep to the binding rule and the refusal of chains is not known (6.5).

---

## Appendix. Word index

Every root, with the section of Part 3 that gives its places. The atoms are in 1.7; the verdicts are in 1.9.

| Root | § | Root | § | Root | § | Root | § |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ack` | 3.8 | `act` | 3.6 | `after` | 3.9 | `agree` | 3.8 |
| `all` | 3.2 | `always` | 3.9 | `and` | 3.1 | `ans` | 3.8 |
| `apx` | 3.4 | `ask` | 3.6 | `assume` | 3.8 | `at` | 3.9 |
| `atleast` | 3.4 | `atmost` | 3.4 | `avg` | 3.3 | `before` | 3.9 |
| `bel` | 3.7 | `best` | 3.4 | `by` | 3.9 | `can` | 3.7 |
| `cause` | 3.10 | `chk` | 3.6 | `clr` | 3.8 | `cnt` | 3.3 |
| `code` | 3.6 | `crit` | 3.2 | `def` | 3.2 | `div` | 3.3 |
| `during` | 3.9 | `each` | 3.9 | `eith` | 3.1 | `ent` | 3.10 |
| `eq` | 3.4 | `err` | 3.8 | `few` | 3.2 | `filt` | 3.5 |
| `fin` | 3.6 | `for` | 3.9 | `from` | 3.9 | `func` | 3.3 |
| `grp` | 3.5 | `half` | 3.2 | `hyp` | 3.8 | `if` | 3.1 |
| `is` | 3.5 | `join` | 3.12 | `know` | 3.7 | `leave` | 3.12 |
| `loc` | 3.5 | `many` | 3.2 | `max` | 3.3 | `may` | 3.7 |
| `mem` | 3.5 | `min` | 3.3 | `minus` | 3.3 | `more` | 3.4 |
| `most` | 3.2 | `msg` | 3.12 | `must` | 3.7 | `need` | 3.7 |
| `none` | 3.2 | `not` | 3.1 | `or` | 3.1 | `over` | 3.4 |
| `par` | 3.6 | `pct` | 3.3 | `pick` | 3.5 | `plan` | 3.7 |
| `pls` | 3.8 | `plus` | 3.3 | `pow` | 3.3 | `pri` | 3.12 |
| `prob` | 3.7 | `re` | 3.12 | `rej` | 3.8 | `rep` | 3.9 |
| `retr` | 3.8 | `rng` | 3.3 | `saw` | 3.12 | `say` | 3.7 |
| `should` | 3.7 | `some` | 3.2 | `still` | 3.9 | `sug` | 3.8 |
| `sum` | 3.3 | `supp` | 3.10 | `tell` | 3.6 | `then` | 3.6 |
| `times` | 3.3 | `to` | 3.12 | `under` | 3.4 | `unk` | 3.8 |
| `until` | 3.9 | `val` | 3.3 | `want` | 3.7 | `what` | 3.11 |
| `when` | 3.9 | `which` | 3.11 | `why` | 3.10 | `will` | 3.8 |
| `would` | 3.10 | `yn` | 3.11 |   |   |   |   |

Not roots: the formula quote `'…'` and the joins `&` `|` `=>` `<=>` inside it (1.4.6).
