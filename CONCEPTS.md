# Concepts

Grouped by the problem each one solves, not alphabetically — a glossary is a lookup tool, and
these are meant to be read in order the first time. Linked from [README.md](README.md); start
there for the module map, come here when something breaks or you need the full explanation.

Currently covers python00–02 in depth, plus python04 (finished). python03 concepts will be added
as those exercises actually get built — see the README's python03 table for real status.

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

## 9 · When things go wrong (python02)

**Transmitter and receiver.** `raise` *sends* an error; `except` *receives* it. They live in
different functions. The function that detects the problem raises; the caller decides what the
problem means.

```
input_temperature                 test_temperature
┌──────────────────┐             ┌──────────────────────────┐
│ 100 > 40 ?       │             │ try:                     │
│   raise ValueError ─────────────▶ except ValueError as e:  │
└──────────────────┘             │     print(... e)         │
     TRANSMITTER                 └──────────────────────────┘
                                        RECEIVER
```

**Why the callee must not catch its own error.** `-> int` is a promise. For `"abc"` there is no
correct integer to return — `0` or `-1` would be a *false reading*, silently corrupting the data.
A function that cannot keep its promise raises instead of pretending.

```python
def input_temperature(temp_str: str) -> int:
    return int(temp_str)           # no try here — failure leaves on its own
```

**`raise` stops the function.** Nothing after it runs, nothing is returned. An uncaught raise
travels all the way up and becomes a traceback — that *is* the crash.

**A `try` only protects code that runs inside it.** A fuse box protects the sockets wired through
it. A call to the same function outside the `try` is on the mains.

**The exception object.** An error is a package: a **type** and a **message**. The last line of a
traceback shows both — `ValueError: invalid literal for int() with base 10: 'abc'`. `as e` gives
the package a name; `{e}` prints the message. Never hand-type a message Python already wrote — it
will be wrong for the next input.

```python
except ValueError as e:
    print(f"Caught input_temperature error: {e}")
```

`e` exists only inside its `except` block. Reading it anywhere else is a `NameError`.

**Type vs. value.** Type is *what kind of thing*; value is *which one*. Wrong plug in the socket →
`TypeError`. Right plug, wrong voltage → `ValueError`.

| Code | Type OK? | Value OK? | Raises |
|---|---|---|---|
| `int("abc")` | ✅ `int()` accepts strings | ❌ not a number | `ValueError` |
| `100` °C for a plant | ✅ it's an int | ❌ out of range | `ValueError` (yours) |
| `int(None)`, `int([...])`, `"abc" + 50` | ❌ | — | `TypeError` |

**The exception tree.** `except X` catches `X` **and every child of `X`**. `except Exception`
catches almost everything — including your own bugs, which it then hides. Catch the narrowest
type you expect.

```
Exception
├── ValueError
├── TypeError
├── ZeroDivisionError
└── GardenError            ← yours
    ├── PlantError
    └── WaterError
```

**Several types, one `try`.** Two forms, for two needs:

```python
try:                                   # separate handlers — each knows its own name
    garden_operations(n)
except ValueError as e:
    print(f"Caught ValueError: {e}")
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")
```

```python
try:                                   # grouped — one shared reaction,
    garden_operations(n)               # but it can't say which one it caught
except (ValueError, TypeError) as e:
    print(f"Caught a data error: {e}")
```

No `type()` allowed means the *handler* supplies the name, which is why separate handlers are
needed when the output must name the error.

**`try` / `except` / `else` / `finally`.** Four branches of one junction:

```
try:       the risky call
except:    runs only if it failed
else:      runs only if it did NOT fail    ← the "success" message goes here
finally:   runs ALWAYS — even after a return inside except
```

**Custom exceptions and the relay baton.** A custom exception is a label template: the class
defines the *kind*, the raiser writes the *message*, and the default is only the fallback. The
message must be passed up the chain with `super()` to `Exception`, which is what stores it for
`{e}`. One class that drops the baton breaks the default message for every child below it.

```python
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)          # hand it up — don't just store it on self


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

raise PlantError(f"Invalid plant name to water: '{name}'")   # specific text: at the raise
```

Classes define; they never `print`. A `print` in a class body runs once when the file is read,
before `main` — the first line of your output, uninvited.

**`finally` survives `return`.** The function is already on its way out, and Python still stops
to run the cleanup. That is the whole point: whoever leaves last switches the desk off.

```python
print("Opening watering system")
try:
    for plant in plants:           # loop INSIDE the try: one failure stops the run
        water_plant(plant)
except PlantError as e:
    print(f"Caught PlantError: {e}")
    return                         # leave immediately...
finally:
    print("Closing watering system")   # ...but this still runs
```

Put the `try` *inside* the loop instead and the system opens once and closes after every plant.

**Code after the junction runs on both paths.** Anything placed after the whole `try`/`except`
(at the same indent as `try`) runs whether it succeeded or failed — the right place for a blank
line between tests.

---

## 10 · Talking to the outside world (python04)

**Shebang vs. interpreter invocation.** `#!/usr/bin/env python3` only matters when a file is
launched directly (`./file.py`). Run it as `python3 file.py` instead and the shebang is never even
read — you already named the interpreter yourself.

**`sys.argv[0]` always exists.** It's the script's own name, not an argument. `len(sys.argv) == 1`
means *no extra arguments were given*; the first real argument sits at index `1`, never `0`.

**A path and the data it points to are both `str`, and that's exactly the trap.** `open()` always
wants the **address** — a filename — never the content living at that address, even though both
happen to be the same type. Passing a file's already-read content back into `open()` (or into
another file's `.write()`) is the same mistake wearing a different variable name each time.

```python
content = f.read()        # content: the DATA
open(content, "w")        # WRONG — content isn't a path, it's text
open(filename, "w")       # right — filename is the address
```

**A file handle and its content are different values — don't reuse one name for both.**
`f = open(path)` then later `f = f.read()` throws away the handle you still need to `.close()`.
Give the handle and the content two different names.

**`print()` always returns `None`.** It's built to *display*, not to hand back a usable value.
`x = print(y)` sets `x` to `None` — never to `y`. If you need the value itself, call whatever
actually returns it (`f.read()`) and skip wrapping it in `print()`.

**String methods never mutate — they return a new string.** `.replace()`, `.strip()` leave the
original untouched; the result has to be captured and reassigned, same pattern as any other
transformation: `s = s.strip()`, not `s.strip()` alone.

**An unset variable across `try`/`except` is the same shape as across `if`/`else`.** A variable
assigned only inside `try` doesn't exist on the `except` path. Reading it afterward — unconditionally,
at the same indent as the whole block — crashes with `UnboundLocalError` the instant the error path
actually runs, not before.

```python
try:
    content = f.read()
except OSError as e:
    print(e)
return content              # crashes here if the except path ran — content was never set
```

**Every declared return type needs every path covered — no silent fallthrough.** mypy accepts
"falls off the end with no `return`" only when the annotation is bare `-> None`. Any other
annotation (`-> str`, `-> str | None`, `-> tuple[bool, str]`) requires an explicit `return` on
*every* branch, including the one you're sure can't happen.

**`with` is the cleanup you'd otherwise write by hand, guaranteed.** `with open(path) as f: ...`
closes `f` automatically at the end of the block, even if an exception fires partway through.
Same job as a `finally` — scoped specifically to things that need releasing.

**Streams are separate channels, not separate destinations, by default.** `stdout` and `stderr`
both land on the same terminal unless redirected — but they *can* be redirected independently
(`program > out.txt 2> err.txt`), which is the entire reason to keep errors on `stderr`: so
redirecting normal output doesn't also swallow the error messages. Unlike `print()`,
`sys.stderr.write()` adds no trailing newline — append `\n` yourself.

**`sys.stdin.readline()` keeps the newline; `input()` strips it.** Same job, different contract.
Swapping one for the other means re-adding the `.strip()` step `input()` used to do for free.

**A tuple is just `(value, value, ...)` — printing one shows exactly that.** `(True, 'content')`
printed is literally Python's own `repr()` of a 2-element tuple. No manual string formatting is
needed to match that shape — build the tuple, `return` it, let `print()` show it.

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
| `ValueError: invalid literal for int() with base 10` | right type, bad value — and you caught `TypeError` instead |
| `UnboundLocalError` / `NameError` after an `except` | the variable was assigned in the `try` only; the `except` path never set it — or you read `e` outside its `except` |
| `TypeError: int() argument must be ... not 'list'` | passed the whole container instead of the loop variable |
| `RecursionError: maximum recursion depth exceeded` | a function calls itself by accident — feedback loop (e.g. `test_x()` inside `test_x`'s own print) |
| traceback despite a `try` | the failing call sits outside the `try`, or the `except` names a different type than the one raised |
| `{e}` prints an empty string | a custom exception stored the message on `self` but never passed it to `super().__init__()` |
| output line appears before your header | a `print` in a class body — runs when the class is defined |
| `IndexError: list index out of range` reading `sys.argv[N]` | assumed an argument exists that wasn't passed — check `len(sys.argv)` first |
| `OSError: [Errno 22] Invalid argument` from `open()` | passed content (or a `{set}`-wrapped value) where a plain filename string was expected |
| `IndentationError: expected an indented block after 'with'` | `with` opens a block exactly like `if`/`try`/`for` — its body needs to be indented a level deeper |

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
| `E711` | `== None` — use `is None` instead (identity, not equality) |
| `E265` | block comment must start with `# ` |
| `W291` / `W293` / `W391` / `W292` | trailing whitespace, whitespace on a blank line, blank lines at EOF, no newline at EOF |
| `F821` | undefined name — catches read-before-assignment before you run anything |
| `F541` | f-string with no placeholders |
| `F841` | variable assigned but never used — e.g. `except X as e:` whose body never mentions `e` |
| `E111` | indentation not a multiple of 4 |
| `E225` | missing whitespace around an operator (`x =y`) |

## Checking your work

```bash
python3 ft_whatever.py                  # does it run and produce the right output?
python3 -m flake8 ft_whatever.py        # style: silent output means clean
python3 -m mypy --strict ft_whatever.py # types
```

Run mypy **before** running the program — it catches missing `self`, wrong return types and
undefined names without executing anything.

Use `--strict`: plain `mypy` silently skips functions whose parameters have no hints, so a missing
`temp_str: str` passes unnoticed. Always name the file — `mypy` alone prints
`Missing target module, package, files, or command`.

python02 ex2 is the one exception: the `TypeError` operation *must* fail mypy (`Unsupported
operand types for +`). That error is the exercise working, not a bug.

---

## Recurring error patterns

Personal to this repo, tracked in [CLAUDE.md](CLAUDE.md). Worth checking for by reflex:

1. **Loop body ignores the loop variable** — after writing a `for` loop, immediately confirm the
   variable it hands you appears in the body.
2. **Read before assignment** — a name used on a path where nothing assigned it. Often appears
   after deleting a line and leaving its readers behind, or after splitting one assignment into a
   `try`/`except` or `if`/`else` where only one branch sets it. `F821` catches the module-level
   case instantly; the `try`/`except` case only shows up at runtime as `UnboundLocalError`.
3. **Inverted condition / wrong operator** — the action lands in the guard branch instead of the
   `else`; or `==` where `=` was meant. `==` asks, `=` commands.
4. **Name collisions** — an attribute and a method sharing a name (`age`, `bloom`); or one variable
   reused for two different meanings in the same function (a filename string, then overwritten to
   become the file handle that was opened from it).
5. **Indentation decides membership** — a `def` is inside a class only because of its indentation;
   same rule makes a `with`/`try`/`for` body belong to that block only when indented under it.
6. **Class instead of instance** — `Plant.show()`, `garden.show()`, `Plant.Stats.add_show()`. When
   you type a capital letter before a dot, ask whether you meant an object.
7. **Declared but ignored parameters** — a value in the signature that the body hardcodes anyway.
   python02 version: an exception's `__init__` receives `message`, then passes a fixed string to
   `super()` instead.
8. **Catching in the wrong place** — the try/except inside the function that fails, instead of in
   its caller. If the function then has to `return` a made-up value (`return 1`), that's the sign.
9. **Hand-typed error messages** — typing the text Python already put in `e`. Use `{e}`.
10. **Treating a doer's return value as real** — `x = print(y)` or `x = some_mutating_call()`
    assumes the call hands back something useful; many don't. Check what a function actually
    `return`s before assigning its result anywhere.
