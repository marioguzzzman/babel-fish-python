# babel-fish-python

42 Berlin Python track. Five modules; the garden metaphor runs through the first three, then the
setting changes while the skills keep stacking.

| Module | Subject title | What it teaches |
|---|---|---|
| [python00/](python00/) | *Growing Code — Python Fundamentals Through Garden Data* | Functions: input → transform → output |
| [python01/](python01/) | *Code Cultivation — Object-Oriented Garden Systems* | Objects: things that hold state and behave |
| [python02/](python02/) | *Garden Guardian — Data Engineering for Smart Agriculture* | Exceptions: the path your code takes when something fails |
| [python03/](python03/) | *Data Quest — Mastering Python Collections* | Containers: choosing the right shape to hold many things |
| [python04/](python04/) | *Data Archivist — Digital Preservation in the Cyber Archives* | Files and streams: talking to the world outside the process |

**How to use this file.** The module tables below show *when* each idea appears, module by
module. The deep explanations, code snippets, and the "when something breaks" lookup tables live
in [CONCEPTS.md](CONCEPTS.md) — start there when something breaks or you need the full
explanation of a term.

> **Note:** [CONCEPTS.md](CONCEPTS.md) currently covers python00–02 in depth, plus python04
> (finished). python03 concepts will be added as those exercises actually get built. Each
> module's own subject lives in its own `.md` — e.g. [python03.md](python03/python03.md),
> [python04.md](python04/python04.md).

---

## The through-line

The single most useful thing to understand about the first two modules is that they teach
**two different units of organisation**.

**python00's unit is the function.** A function is a transformation. Data goes in, something
comes out (or gets printed), and nothing is remembered afterwards. Each exercise is an
independent problem; nothing carries over. Signal in, signal out, no memory.

**python01's unit is the class.** `Plant`. You write it in ex1 and you are still writing the
*same* `Plant` in ex6. An object is a module in a rack: it has knobs whose positions persist
between touches (**attributes**) and jacks you can trigger (**methods**), and triggering a jack
can change where a knob is sitting.

That shift — from *stateless transformation* to *stateful thing* — is the whole learning curve.

```
python00                        python01
────────                        ────────
function                        class
arguments                       attributes
"what does it return?"          "what does it remember?"
independent exercises           one object, grown seven times
```

The next three modules each add a dimension to code you already know how to write. None of them
introduces a new unit of organisation — they change what your functions and objects have to
survive contact with.

```
python02        the failure path      what happens when the input is wrong
python03        the container         what shape holds many things at once
python04        the outside world     what happens when data leaves the process
```

Put another way: python00–01 assume everything goes right and everything is in memory.
python02 removes the first assumption, python04 removes the second, and python03 gives you the
tools to handle more than one thing at a time in between.

---

## python00 — Growing Code

Constraint: **write only the requested function.** No `main`, no `if __name__`, no code outside
the function. A `main.py` harness is provided to import and test your work.

| Ex | File | Concept introduced | Vocabulary |
|---|---|---|---|
| 0 | `ft_hello_garden.py` | Defining and calling a function; output as a side effect | function, definition, call, side effect |
| 1 | `ft_garden_name.py` | Reading input; storing it in a variable | `input()`, variable, assignment, string literal |
| 2 | `ft_plot_area.py` | Converting text to numbers; arithmetic | type conversion / casting, `int()`, expression |
| 3 | `ft_harvest_total.py` | Accumulating a running total across several inputs | accumulator, running total |
| 4 | `ft_plant_age.py` | Branching on a condition | `if`/`else`, boolean, comparison operator, branch |
| 5 | `ft_water_reminder.py` | Threshold logic; second pass at conditionals | condition, threshold, guard |
| 6 | `ft_count_harvest_iterative.py`<br>`ft_count_harvest_recursive.py` | The same problem two ways: a loop, and a function that calls itself | iteration, `range()`, recursion, base case, helper function |
| 7 | `ft_seed_inventory.py` | Parameters instead of `input()`; multi-way branching; **type hints** | parameter vs. argument, signature, `elif` chain, type annotation, `mypy`, string method |

**Arc:** output → input → conversion → accumulation → decision → repetition → typed interface.

Exercise 7 is the hinge: the first function that receives its data as **parameters** rather than
prompting for it, and the first that must declare **types**. Both carry straight into python01.

---

## python01 — Code Cultivation

Constraint: **each exercise in its own directory, standing alone.** You cannot import across
exercises, so `Plant` is physically copied forward into each file and grows one capability per
step. That duplication would be wrong in real code; here it is the grading format.

| Ex | File | Concept introduced | Vocabulary |
|---|---|---|---|
| 0 | `ft_garden_intro.py` | How a Python file starts; what changes when it's imported instead of run | module, entry point, `__name__`, `"__main__"`, guard, shebang, executable bit, `PATH` |
| 1 | `ft_garden_data.py` | Class as a template; instances as the things that hold values; `self` | class, instance, instantiation, attribute, method, `self`, object, list of objects |
| 2 | `ft_plant_growth.py` | Methods that **change** the object rather than just reading it | state, mutation, augmented assignment (`+=`), floating-point error, `round()` |
| 3 | `ft_plant_factory.py` | Building a fully-formed object in one step | constructor, `__init__`, initialization, required argument, fail-fast |
| 4 | `ft_garden_security.py` | Controlling access to data; validating before storing | encapsulation, protected (`_x`), name mangling (`__x`), getter, setter, validation, invariant |
| 5 | `ft_plant_types.py` | Specialised classes built on a shared one | inheritance, parent/base class, child/subclass, `super()`, override, state flag |
| 6 | `ft_garden_analytics.py` | Methods not tied to an instance; classes inside classes | static method, class method, `cls`, alternative constructor, nested class, decorator, inheritance chain, polymorphism |

**Arc:** program structure → objects exist → objects change → objects are born complete →
objects protect themselves → objects specialise → objects observe themselves.

Each step is motivated by a problem the previous step created. ex1's four separate assignment
lines are tedious and error-prone → ex3's constructor fixes it. ex3's constructor accepts any
value including nonsense → ex4's validation fixes it. ex4's single `Plant` can't express a tree
and a tomato → ex5's inheritance fixes it.

---

## python02 — Garden Guardian

Constraint: **your programs must never crash.** Every exercise is a `try`/`except` exercise; the
keywords `try`, `except`, `finally` and `raise` are language features, so they never appear in the
authorized-functions list.

| Ex | File | Concept introduced | Vocabulary |
|---|---|---|---|
| 0 | `ft_first_exception.py` | Catching a failure instead of dying from it | exception, `try`/`except`, catching, traceback, exception object |
| 1 | `ft_raise_exception.py` | Signalling a failure yourself when the value is *valid but wrong* | `raise`, validation vs. conversion, domain range, error message |
| 2 | `ft_different_errors.py` | Different failure kinds are different types; catching several at once | `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `TypeError`, exception tuple, multiple handlers |
| 3 | `ft_custom_errors.py` | Your own exception types, arranged in a hierarchy | custom exception, subclassing `Exception`, default message, catching a base class |
| 4 | `ft_finally_block.py` | Cleanup that runs whether or not it went wrong | `finally`, resource cleanup, acquire/release, early `return` inside `try` |

**Arc:** catch → raise → distinguish → classify → clean up.

Two ideas worth naming. First, ex3's inheritance is **the same mechanism as python01 ex5** —
`PlantError(GardenError)` is `Tree(Plant)` — but used for classification rather than behaviour:
catching `GardenError` catches every child, which is the *entire point* of putting them in a tree.

Second, **`raise` is the mirror image of `return`.** Both end the function and hand something back
to the caller. `return` hands back an answer up the normal path; `raise` hands back a problem up a
separate path that keeps travelling until someone catches it. Exercise 1 is where this lands: the
string `"100"` converts perfectly well — `int()` has no complaint — but 100 °C is not a temperature
a plant survives, so *your* code is the only thing that can object.

---

## python03 — Data Quest

Constraint: **no file I/O.** Everything in memory or from `sys.argv`. This is also the first module
that uses `import`.

**Status: in progress.** ex0 done, ex1 in progress, ex2–ex6 not started. The table below is the
curriculum map (what each exercise will teach), not a claim that it's built yet.

| Ex | File | Concept introduced | Vocabulary | Status |
|---|---|---|---|---|
| 0 | `ft_command_quest.py` | Arguments from outside the program; the list you didn't build | `import`, module, `sys.argv`, list, index, `len()` | ✅ done |
| 1 | `ft_score_analytics.py` | Building a list by filtering; aggregating over it | append, filtering, `sum()`/`max()`/`min()`, aggregate, partial validity | 🚧 in progress |
| 2 | `ft_coordinate_system.py` | A fixed-size group of values that must not change | tuple, immutability, unpacking, retry loop, `math.sqrt()` | ⬜ not started |
| 3 | `ft_achievement_tracker.py` | Membership and uniqueness as the whole point | set, uniqueness, union, intersection, difference, `random` | ⬜ not started |
| 4 | `ft_inventory_system.py` | Lookup by name instead of by position | dict, key/value, parsing `k:v`, duplicate key, percentage of total | ⬜ not started |
| 5 | `ft_data_stream.py` | Producing values on demand instead of all at once | generator, `yield`, `next()`, lazy evaluation, infinite sequence, consuming a generator | ⬜ not started |
| 6 | `ft_data_alchemist.py` | Writing a whole transformation on one line | list comprehension, dict comprehension, filtering clause, condensed form | ⬜ not started |

**Planned arc:** ordered → aggregated → immutable → unique → keyed → lazy → condensed.

The four containers are not four syntaxes to memorise — they are four different answers to
*"what do I need to do with this data?"*:

```
list      order matters, duplicates fine        scores in the order given
tuple     fixed shape, must not change          (x, y, z)
set       only membership matters               which achievements do you have
dict      look it up by name                    sword → 3
```

Choose by the question you'll ask, not by which one you typed last time. That's the Twitter story
in the subject's foreword: correct code, wrong container, linear time in production.

Exercise 5 is the conceptual jump. Every container before it *holds* its values; a generator holds
only the **instruction for producing the next one**. `gen_event()` is infinite yet costs nothing,
because nothing exists until `next()` asks. This is the first time you write something that is a
process rather than a thing.

---

## python04 — Data Archivist

Constraint: **no `with` before ex3.** You open and close by hand first, so that the context manager
in ex3 arrives as a solution to a problem you have already felt.

**Status: done.** All four exercises finished, flake8- and mypy-clean.

| Ex | File | Concept introduced | Vocabulary |
|---|---|---|---|
| 0 | `ft_ancient_text.py` | Reading a file; failure modes that come from outside your program | `open()`, file object, `read()`, `close()`, `typing.IO`, `FileNotFoundError`, `PermissionError` |
| 1 | `ft_archive_creation.py` | Writing; a mode that destroys what was there | write mode, truncation, transform-then-save, optional save |
| 2 | `ft_stream_management.py` | The three standard channels a process is born with | stream, `sys.stdin`/`stdout`/`stderr`, `readline()`, `flush()`, redirection |
| 3 | `ft_vault_security.py` | Cleanup that can't be forgotten; returning success alongside the result | `with`, context manager, `(bool, str)` return, default parameters |

**Arc:** read → write → streams → guaranteed cleanup.

This module is where python02 stops being an exercise topic and becomes unavoidable. Everything
here fails for reasons that have nothing to do with your logic: the file isn't there, you don't
have permission, the disk is full. A pure function can be proven correct; a file operation can only
be *handled*.

Two things to hold onto:

- **`with` is `finally`, packaged.** python02 ex4 made you write the cleanup by hand. `with` is the
  language noticing that "always close it, even on the error path" is the same four lines every
  time, and making them disappear. It is the same idea, not a new one.
- **`stderr` exists so that errors survive a pipe.** `print()` goes to stdout, which is what gets
  redirected into the next program or a file. Sending errors there mixes complaints into the data.
  That's what ex2's `[STDERR]` prefix is demonstrating.

---

# Concepts, errors, and checking your work

Moved to [CONCEPTS.md](CONCEPTS.md) — the deep explanations, code snippets, the runtime-error
lookup table, flake8 codes, and the recurring-error-patterns list all live there now, so this file
stays a map instead of a textbook. Start here for *when* an idea appears; go there for *what it
means* or *why something broke*.
