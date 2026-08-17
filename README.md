# babel-fish-python

42 Berlin Python track. Two modules, one continuous garden metaphor.

| Module | Subject title | What it teaches |
|---|---|---|
| [python00/](python00/) | *Growing Code — Python Fundamentals Through Garden Data* | Functions: input → transform → output |
| [python01/](python01/) | *Code Cultivation — Object-Oriented Garden Systems* | Objects: things that hold state and behave |

---

## The through-line

The single most useful thing to understand about these two modules is that they teach
**two different units of organisation**.

**python00's unit is the function.** A function is a transformation. Data goes in, something
comes out (or gets printed), and nothing is remembered afterwards. Each exercise is an
independent problem; nothing carries over. Signal in, signal out, no memory.

**python01's unit is the class**
`Plant`. You write it in ex1 and you are still writing the *same* `Plant` in ex6. An object is a
module in a rack: it has knobs whose positions persist between touches (**attributes**) and jacks
you can trigger (**methods**), and triggering a jack can change where a knob is sitting.

That shift — from *stateless transformation* to *stateful thing* — is the whole learning curve.

```
python00                        python01
────────                        ────────
function                        class
arguments                       attributes
"what does it return?"          "what does it remember?"
independent exercises           one object, grown seven times
```

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

Exercise 7 is the hinge: it's the first function that receives its data as **parameters** rather
than prompting for it, and the first that must declare **types**. Both carry straight into
python01.

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
| 6 | `ft_garden_analytics.py` | Methods not tied to an instance; classes inside classes | static method, class method, `cls`, alternative constructor, nested class, decorator, inheritance chain |

**Arc:** program structure → objects exist → objects change → objects are born complete →
objects protect themselves → objects specialise → objects observe themselves.

Each step is motivated by a problem the previous step created. ex1's four separate assignment
lines are tedious and error-prone → ex3's constructor fixes it. ex3's constructor accepts any
value including nonsense → ex4's validation fixes it. ex4's single `Plant` can't express a tree
and a tomato → ex5's inheritance fixes it.

---

## Vocabulary

**Class vs. instance.** The class is the blueprint; instances are the buildings. The blueprint
holds no values — `Plant` has no height. `p1` does.

**Attribute vs. method.** An attribute is data stored on an object (`self.name`). A method is a
behaviour attached to an object (`self.show()`).

**`self`.** The first parameter of *every* method, filled in automatically by the call syntax.
Writing `p2.show()` means "run `show`, passing `p2` into the first parameter slot." It does **not**
come from `__init__`, and works fine in a class that has no `__init__`.

**`__init__`.** The method Python calls automatically at construction. It sets up data and never
prints. A value belongs in its signature **only if the caller needs to choose it** — things that
are the same for every instance (a bloom flag starting `False`, a counter starting `0`) are
hardcoded in the body instead.

**Doer vs. returner.** Some functions hand back a value (`round()`, `get_height()`); you use the
result. Others do something and return `None` (`show()`, `grow()`); calling them *is* the output.
Wrapping a doer in `print()` prints `None`.

**Encapsulation.** `_height` is a *convention*, not a lock — anyone can still write to it. What it
buys is a **chokepoint**: the validation rule lives in exactly one place, and bypassing it becomes
visible in the code.

**`_x` vs. `__x`.** One underscore does nothing mechanically — it's a sign saying "internal."
Two underscores trigger **name mangling**, rewriting `__x` to `_ClassName__x`. Mangling exists to
avoid subclass collisions, not for security, and it actively fights inheritance — which is why
python01 requires the single underscore.

**Inheritance and `super()`.** A subclass gets the parent's methods for free. Defining a method
with the same name **overrides** (shadows) the parent's. `super()` reaches past your own version
to the parent's — so `super().show()` prints the standard line and you add to it, instead of
retyping it.

**Static method vs. class method vs. instance method.** An instance method receives `self`. A
class method receives the class (`cls`) and can therefore build new instances — useful as an
alternative constructor. A static method receives neither: it's a plain function that happens to
live inside a class because it belongs there conceptually.

**`if __name__ == "__main__":`.** Python sets `__name__` before your first line runs: to
`"__main__"` when the file is executed directly, to the module's own name when it's imported. The
`if` only **compares** — it's a sensor, not an actuator. Everything at module level runs on import;
only the fenced block is skipped.

**Shebang.** `#!/usr/bin/env python3` tells the OS which interpreter to use — but *only* when the
file is launched directly (`./file.py`), never when you type `python3 file.py` and name it
yourself. Routing through `env` finds whichever `python3` is on `PATH`, instead of hardcoding a
path that varies per machine. Requires the executable bit (`chmod +x`).

---

## Checking your work

Both modules require flake8; python01 (and python00 ex7) require type hints.

```bash
python3 ft_whatever.py                  # does it run and produce the right output?
python3 -m flake8 ft_whatever.py        # style: silent output means clean
python3 -m mypy ft_whatever.py          # types
```
