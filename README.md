# babel-fish-python

42 Berlin Python track. Two modules, one continuous garden metaphor.

| Module | Subject title | What it teaches |
|---|---|---|
| [python00/](python00/) | *Growing Code — Python Fundamentals Through Garden Data* | Functions: input → transform → output |
| [python01/](python01/) | *Code Cultivation — Object-Oriented Garden Systems* | Objects: things that hold state and behave |

**How to use this file.** The two module tables show *when* each idea appears. The Concepts
section groups them by *what problem they solve*, each with a minimal example. The error table
maps a message you actually saw to the concept behind it — start there when something breaks.

---

## The through-line

The single most useful thing to understand about these two modules is that they teach
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

# Concepts

Grouped by the problem each one solves, not alphabetically — a glossary is a lookup tool, and
these are meant to be read in order the first time.

---

## 1 · How a file runs

**Module.** Any `.py` file. Its name is the filename without `.py`.

**`__name__` and the guard.** Python sets `__name__` *before your first line runs*: to
`"__main__"` if the file was executed directly, to the module's own name if it was imported. The
`if` only **compares** — it's a sensor, not an actuator, and cannot change anything.

```python
if __name__ == "__main__":     # True only when run directly
    main()                     # skipped entirely on import
```

**Import runs the whole file.** Importing does not "reach in and take one function" — it executes
the file top to bottom. That's why unguarded prints fire uninvited. Everything at module level
runs on import; only the fenced block is skipped.

**Shebang.** Tells the OS which interpreter to use — but *only* when the file is launched
directly, never when you type `python3 file.py` and name the interpreter yourself.

```python
#!/usr/bin/env python3         # line 1, no space after #!
```

`env` looks up `python3` on `PATH`, so it finds whichever Python this machine has, instead of
hardcoding a path that varies per machine. Needs the executable bit: `chmod +x file.py`.

**Execution order at module level.** A `def` is a *statement that runs*. Calling a function above
its `def` is a `NameError` — but this rule does **not** apply inside a class body (see §5).

---

## 2 · Making a thing

**Class vs. instance.** The class is the blueprint; instances are the buildings. The blueprint
holds no values — `Plant` has no height, `p1` does.

```python
class Plant:          # blueprint
    ...
p1 = Plant()          # instance — the thing that holds values
```

**Attribute vs. method.** An attribute is data stored on an object; a method is a behaviour
attached to it.

```python
p1.name          # attribute — data
p1.show()        # method — behaviour
```

**`self`.** The first parameter of *every* method, filled in automatically by the call syntax.
`p2.show()` means "run `show`, passing `p2` into the first parameter slot." It does **not** come
from `__init__`, and works fine in a class with no `__init__` at all.

```python
class Plant:
    def show(self) -> None:        # declared: one parameter
        print(self.name)
p2.show()                          # called: zero arguments — the dot supplies p2
```

**`__init__` (constructor).** The method Python calls automatically at construction. It sets up
data and **never prints**.

```python
class Plant:
    def __init__(self, name: str, height: float) -> None:
        self.name = name
        self.height = height
p1 = Plant("Rose", 25.0)           # __init__ runs here, once
```

**Signature as a contract.** Every parameter declared is a demand every caller must satisfy —
even if the body ignores it. **A value belongs in the signature only if the caller needs to
choose it.** Things identical for every instance are hardcoded in the body.

```python
def __init__(self, name: str, color: str) -> None:
    self.color = color             # caller chooses  → parameter
    self.has_bloomed = False       # always False    → hardcoded
```

**Fail-fast.** `Plant("Rose", 25.0)` missing an argument fails *immediately*, naming what's
missing. Setting attributes one by one after construction fails later and elsewhere — and a typo
(`p1.hieght = 25`) silently creates a *new* attribute instead of erroring.

---

## 3 · Making it behave

**Doer vs. returner.** Some functions hand back a value; you use the result. Others do something
and return `None`; calling them *is* the output. **Never wrap a doer in `print()`.**

```python
h = round(x, 1)        # returner — use the result
p1.show()              # doer — calling it IS the output
print(p1.show())       # WRONG → prints the line, then "None"
```

Your own `-> None` annotation tells you which kind you wrote.

**Mutation.** A method that *writes* to `self` rather than only reading. The change persists, so
the next call sees it. This is what separates an object from a function.

```python
def show(self) -> None:            # reads
    print(self._height)
def grow(self) -> None:            # writes — the plant is permanently taller
    self._height += self.growth_rate
```

**Augmented assignment.** `x += 1` is `x = x + 1`. Note `x += x` **doubles**; to count events you
add `1`.

**State flag.** A boolean attribute the object carries between calls: set in `__init__`, flipped
by one method, read by another to choose behaviour. Nothing is "passed" — the object remembers.
A latch, not a pushbutton.

```python
self.has_bloomed = False           # __init__
def bloom(self) -> None:
    self.has_bloomed = True        # single = : command, not comparison
def show(self) -> None:
    if self.has_bloomed: ...       # read
```

Give the flag a name distinct from the method that flips it, or the two collide.

**Single responsibility.** A method should own one job. `show()` prints one plant's line; the
banner and the loop belong to the caller. A plant doesn't know how long your experiment runs.

---

## 4 · Protecting it

**Encapsulation.** `_height` is a *convention*, not a lock — anyone can still write to it. What it
buys is a **chokepoint**: the validation rule lives in exactly one place, and bypassing it becomes
visible in the code (`p1._height = -500` reads as "I am deliberately reaching inside").

**`_x` vs. `__x`.** One underscore does nothing mechanically. Two underscores trigger **name
mangling**, rewriting `__x` to `_ClassName__x`. Mangling avoids subclass collisions; it is not
security, and it actively fights inheritance — which is why python01 requires the single
underscore.

**Getter / setter.** The sanctioned ways out and in. The setter validates and reports success;
the caller decides what to do about failure.

```python
def get_height(self) -> float:
    return self._height

def set_height(self, new_height: float) -> bool:
    if new_height < 0:
        print(f"{self.name}: Error, height can't be negative")
        return False               # the class reports the fact
    self._height = new_height
    return True

if not p1.set_height(-5):          # the caller decides how to react
    print("Height update rejected")
```

**Candidate vs. stored value.** A setter deals with two numbers: the parameter (proposed, from
outside) and the attribute (current). Validate the **candidate**; assign it into storage only
after. `self._height = new_height` — storage left, candidate right.

---

## 5 · Relating types

**Inheritance.** A subclass gets the parent's methods for free.

```python
class Flower(Plant):               # Flower IS A Plant
    ...
```

**`super()`.** Reaches past your own version to the parent's. The standard shape is
`super().thing()` first, then your addition.

```python
class Flower(Plant):
    def __init__(self, name, height, color: str) -> None:
        super().__init__(name, height)    # parent sets up the shared part
        self.color = color                # then your extra

    def show(self) -> None:
        super().show()                    # parent's line
        print(f"Color: {self.color}")     # your extra line
```

In an `__init__` override, `super().__init__(...)` goes **first** — anything you set before it can
be overwritten by the parent.

**Override vs. shadow.** Defining a method with a name the parent already uses replaces it for
that subclass. The parent's version isn't deleted, just hidden — `super()` is how you reach it.
Omit the `super()` call and the parent's work simply never happens.

**Polymorphism.** One piece of code calling one method name; different objects supplying different
implementations, with **no type checks in the calling code**.

```python
def display_statistics(plant: Plant) -> None:
    plant.show_plant_stats()       # a Tree prints 4 lines, a Rose prints 3
```

No `isinstance`, no branching. The object decides its own behaviour. If this function needed
branching, the hierarchy would be wrong.

**Nested class.** A class defined inside another class's body. It is **not** a subclass and
inherits nothing from the enclosing class — the nesting is pure organisation, saying "this type
only makes sense in the context of that one."

```python
class Plant:
    class Stats:                   # nested — sibling of the methods, 4 spaces
        def __init__(self) -> None:
            self._show_calls = 0

    def __init__(self) -> None:
        self._stats = Plant.Stats()    # each plant builds its OWN
```

Create it in `__init__` — the only method that runs exactly once per object. Create it anywhere
else and every plant shares one counter.

**Class-body execution order.** Unlike module level, **order inside a class body does not
matter.** The body executes once at definition time, creating every `def` and nested `class`
before any of them is ever *called*. Nothing can be "too early."

**Indentation decides membership.** A `def` belongs to a class only because of its column.
Pasting code near a class does not put it in the class — and a `class` statement inside a *method
body* is a throwaway local, not a nested class.

---

## 6 · Methods not tied to an instance

**Decorator.** A line beginning with `@`, directly above a `def` at the same indent, that changes
how the function below is treated.

**The three method kinds** differ entirely in *what arrives in the first parameter slot*:

| Kind | First parameter | Receives |
|---|---|---|
| instance method | `self` | the object |
| class method | `cls` | the class |
| static method | *(none)* | nothing |

```python
class Plant:
    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365                    # touches no attribute → needs no object

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0)    # builds one — no arguments from the caller

Plant.is_older_than_year(400)               # callable with no object in existence
```

**`cls` and alternative constructors.** `cls` is *whichever class the method was called on*. A
class method returning `cls(...)` is a **second way to build an object**, correct for every
subclass without being rewritten.

```python
Cactus.create_anonymous()   # cls is Cactus  → a Cactus
# hardcoding Plant(...) instead → silently returns a plain Plant
```

`datetime.now()` in the standard library works exactly this way. Note that in *this* project no
subclass has a compatible constructor, so the benefit is theoretical here — `cls` is the right
default because it costs nothing and fails loudly rather than silently.

---

## 7 · Types and annotations

**Type hints.** Required on all methods in python01, checked with `mypy`. Annotate `float` where
either `int` or `float` is acceptable — Python's numeric tower accepts an `int` wherever a `float`
is expected.

```python
def set_age(self, new_age: int) -> bool:
def show(self) -> None:                     # returns nothing
```

**Forward reference.** A type annotation written as a **string**, because the name it mentions
doesn't exist yet when the annotation is read. A class body runs *in order to build* the class, so
the class's own name isn't bound until the body finishes.

```python
def create_anonymous(cls) -> "Plant":       # quoted — Plant doesn't exist yet
_stats: "Tree.Stats"
```

**Annotation-only declaration.** A name and type with no `=` declares a type and **creates
nothing**. Useful for telling mypy about an attribute without assigning it.

```python
class Plant:
    name: str          # no value — creates no attribute
```

**Not every mypy error is a bug.** Sometimes it means "I can't prove this is safe," and the fix is
to give the checker more information. `_stats: "Tree.Stats"` changes nothing at runtime — delete
it and the program behaves identically; only mypy complains.

**Dunder.** *Double under*score on both sides — `__init__`, `__name__`, `__main__`. Python's
special names. `_init_` with single underscores is an ordinary method Python never calls, and it
fails silently: no error at definition, no error at construction, just a missing attribute much
later.

---

## 8 · Syntax mechanics

**f-strings.** The braces can hold any expression, including a function call.

```python
print(f"{self.name}: {round(self._height, 1)}cm")
print(f"{self.height:.1f}")      # format spec: always one decimal
```

`round(x, 1)` changes the **number**; `:.1f` changes only how it's **shown**. An `f` prefix with
no braces is flagged (`F541`); braces with no `f` print the literal text.

**Floating point.** `0.8` has no exact binary representation, so repeated addition drifts
(`30.600000000000005`). Round at **display** time, never in storage, or the errors compound.

**Keyword arguments and defaults.** Passed by name rather than position; they have defaults, so
omitting them is normal, and order doesn't matter.

```python
print("Created: ", end="")       # override end's default "\n"
print("a", "b", sep="-")         # a-b
```

Style rule that flips: **no** spaces around `=` in a call (`f(x=1)`), but spaces **required** in
ordinary assignment (`x = 1`).

**Lists and iteration over objects.** Python has no way to build a variable name from a number —
`p1`, `p2`, `p3` are unrelated labels. Put the objects in a container and iterate the container;
the loop then hands you the objects themselves.

```python
garden = [p1, p2, p3]            # a list literal — syntax, not a function call
for plant in garden:
    plant.show()                 # NOT Plant.show() — ask the object, not the blueprint
```

Adding a fourth plant changes one line and nothing else.

**Splitting long lines (79-char limit).** Anything inside brackets can break across lines; no
backslash needed. Adjacent string literals are concatenated automatically.

```python
print(f"Stats: {a} grow, "
      f"{b} age, "               # each fragment needs its own f
      f"{c} show")
```

Or name a sub-expression: `answer = Plant.is_older_than_year(age)`, then interpolate `answer`.

---

# When something breaks

## Runtime errors → what they usually mean here

| Message | Usual cause |
|---|---|
| `AttributeError: 'X' object has no attribute 'y'` | a rename that didn't reach every reader; or you're on the wrong object (`self` vs. `self._stats`) |
| `TypeError: 'int' object is not callable` | an attribute and a method share a name; the attribute won |
| `TypeError: f() missing 1 required positional argument: 'self'` | called through the class (`Plant.show()`) instead of an object (`p1.show()`) |
| `TypeError: __init__() missing N required positional arguments` | the signature declares parameters the caller doesn't pass — or that the body ignores |
| `TypeError: unexpected keyword argument 'x'` | the call site still passes something the signature no longer declares |
| `NameError: name 'x' is not defined` | read before assignment, often after deleting a line and leaving its readers |
| `TypeError: 'type' object is not iterable` | you named the type (`list`) instead of building a container (`[a, b, c]`) |
| prints `None` | a doer wrapped in `print()` |
| prints nothing | an empty container — the loop ran zero times, silently |

## flake8 codes

| Code | Meaning |
|---|---|
| `E999` | syntax error — flake8 can't parse the file, so **it reports nothing else until you fix it** |
| `E501` | line longer than 79 characters |
| `E302` / `E305` | two blank lines around top-level `def`/`class` |
| `E303` | too many blank lines — **one** between methods inside a class, two between top-level definitions |
| `E117` | over-indented — a body should be 4 spaces past its `def` |
| `E127` | continuation line doesn't align under the first argument |
| `E251` | no spaces around `=` in keyword arguments |
| `E712` | `== True` is redundant — the value is already a boolean |
| `E265` | block comment must start with `# ` |
| `W291` / `W293` / `W391` / `W292` | trailing whitespace, whitespace on a blank line, blank lines at EOF, no newline at EOF |
| `F821` | undefined name — catches read-before-assignment before you run anything |
| `F541` | f-string with no placeholders |

## Checking your work

```bash
python3 ft_whatever.py                  # does it run and produce the right output?
python3 -m flake8 ft_whatever.py        # style: silent output means clean
python3 -m mypy ft_whatever.py          # types
```

Run mypy **before** running the program — it catches missing `self`, wrong return types and
undefined names without executing anything.

---

## Recurring error patterns

Personal to this repo, tracked in [CLAUDE.md](CLAUDE.md). Worth checking for by reflex:

1. **Loop body ignores the loop variable** — after writing a `for` loop, immediately confirm the
   variable it hands you appears in the body.
2. **Read before assignment** — a name used on a path where nothing assigned it. Often appears
   after deleting a line and leaving its readers behind. `F821` catches it instantly.
3. **Inverted condition / wrong operator** — the action lands in the guard branch instead of the
   `else`; or `==` where `=` was meant. `==` asks, `=` commands.
4. **Name collisions** — an attribute and a method sharing a name (`age`, `bloom`).
5. **Indentation decides membership** — a `def` is inside a class only because of its indentation.
6. **Class instead of instance** — `Plant.show()`, `garden.show()`, `Plant.Stats.add_show()`. When
   you type a capital letter before a dot, ask whether you meant an object.
7. **Declared but ignored parameters** — a value in the signature that the body hardcodes anyway.
