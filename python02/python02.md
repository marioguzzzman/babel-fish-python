# Garden Guardian — Data Engineering for Smart Agriculture (Python 02)

**Version:** 3.0
**Summary:** Build resilient data pipelines for your smart garden! Learn to handle sensor
failures, process agricultural data streams, and create robust monitoring systems that keep your
digital greenhouse thriving.

---

## Contents

| Chapter | Title | Directory | File |
|---|---|---|---|
| I | Foreword | — | — |
| II | AI Instructions | — | — |
| III | Introduction | — | — |
| IV | General Instructions | — | — |
| V | Exercise 0: Agricultural Data Validation | `ex0/` | `ft_first_exception.py` |
| VI | Exercise 1: Agricultural Data Validation Pipeline | `ex1/` | `ft_raise_exception.py` |
| VII | Exercise 2: Different Types of Problems | `ex2/` | `ft_different_errors.py` |
| VIII | Exercise 3: Making Your Own Error Types | `ex3/` | `ft_custom_errors.py` |
| IX | Exercise 4: Finally Block — Always Clean Up | `ex4/` | `ft_finally_block.py` |
| X | Turn in and Submission | — | — |

---

## Chapter I — Foreword

Python's exception handling system is your toolkit for building bulletproof agricultural data
pipelines. You'll learn to catch sensor anomalies, create custom agricultural alerts, and ensure
data integrity even when Mother Nature (or Murphy's Law) strikes.

## Chapter III — Introduction

- How to validate and clean agricultural data streams in real-time
- Which different failure modes exist in IoT sensor networks
- How to create custom agricultural alerts for crop-specific monitoring
- Essential techniques for data pipeline fault tolerance and recovery
- How to ensure data integrity in distributed farming systems

Each exercise builds a component of your smart agriculture data platform, progressing from basic
sensor validation to comprehensive agricultural monitoring systems.

## Chapter IV — General Instructions

- Your programs must be written in **Python 3.10+**
- Your code must respect the **flake8** linter standards
- All functions and methods must include **type hints**: use **mypy** to check your code
- Each exercise must be in its own file
- Focus on demonstrating basic error handling concepts clearly
- Show both normal operations and error scenarios
- Use built-in exceptions appropriately
- Keep solutions simple and focused on learning
- **Your programs must never crash**

> **Data Engineering Note:** This project teaches resilient data pipeline design for agricultural
> systems. Your code should demonstrate how to build fault-tolerant monitoring systems that
> maintain data integrity under real-world conditions.

> **Exception Handling:** All exercises in this module require the use of `try`/`except` blocks
> for error handling. Python keywords such as `try`, `except`, `finally`, and `raise` are
> fundamental language features and do not need to be listed in authorized functions.

> You may use any built-in exception types necessary to complete the exercises, including but not
> limited to `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`,
> `IndexError`, `AttributeError`, and the base `Exception` class. Each exercise description may
> include which exception types are most appropriate for that specific task.

---

## Chapter V — Exercise 0: Agricultural Data Validation

| | |
|---|---|
| **Exercise** | 0 — `ft_first_exception` |
| **Directory** | `ex0/` |
| **Files to Submit** | `ft_first_exception.py` |
| **Authorized** | `int()`, `print()` |

Your smart agriculture data pipeline receives temperature readings from field sensors. Sometimes
sensors transmit corrupted data or farmers input invalid values through mobile apps. Your data
validation layer must filter out bad data before it corrupts your agricultural analytics.

### Requirements

Write a simple function `input_temperature(temp_str)` that:

- Takes an input string as a parameter
- Converts it to a number
- Returns the temperature as an integer

Then, write a function `test_temperature()` that will perform the following tests on
`input_temperature()`:

- Use a valid input (`"25"`)
- Use an invalid input (`"abc"`)
- Handle the case when `input_temperature()` fails; print an error message
- Show that your program keeps running despite the error

### Example

```
$> python3 ft_first_exception.py
=== Garden Temperature ===

Input data is '25'
Temperature is now 25°C

Input data is 'abc'
Caught input_temperature error: invalid literal for int() with base 10: 'abc'

All tests completed - program didn't crash!
```

> You can use the base `Exception` class, or find out which exceptions can be raised by
> `input_temperature()`.

> It's up to you to properly adjust the type hints for these two functions. Consider this
> information valid for all the exercises and upcoming projects.

---

## Chapter VI — Exercise 1: Agricultural Data Validation Pipeline

| | |
|---|---|
| **Exercise** | 1 — `ft_raise_exception` |
| **Directory** | `ex1/` |
| **Files to Submit** | `ft_raise_exception.py` |
| **Authorized** | `int()`, `print()` |

You actually need extra control over your data. Even if the temperature is a valid number, your
plants cannot grow if it's too cold or too hot.

### Requirements

Use your code from Exercise 0 and improve `input_temperature()` and `test_temperature()` as
follows:

- In `input_temperature`:
  - Check if the temperature is reasonable for plants (**0 to 40 degrees Celsius**, limits
    included)
  - Return the temperature if it's valid; otherwise, **raise an exception**
- In `test_temperature`:
  - Add new tests with extreme values (`"100"`, `"-50"`)

The main part of your file will call `test_temperature()`.

### Example

```
$> python3 ft_raise_exception.py
=== Garden Temperature Checker ===

Input data is '25'
Temperature is now 25°C

Input data is 'abc'
Caught input_temperature error: invalid literal for int() with base 10: 'abc'

Input data is '100'
Caught input_temperature error: 100°C is too hot for plants (max 40°C)

Input data is '-50'
Caught input_temperature error: -50°C is too cold for plants (min 0°C)

All tests completed - program didn't crash!
```

---

## Chapter VII — Exercise 2: Different Types of Problems

| | |
|---|---|
| **Exercise** | 2 — `ft_different_errors` |
| **Directory** | `ex2/` |
| **Files to Submit** | `ft_different_errors.py` |
| **Authorized** | `print()`, `open()`, `int()` |

Your garden program might encounter different types of problems. Python has different types of
errors for different situations, and you can catch them separately or together.

### Requirements

Write a function `garden_operations(operation_number)` that contains faulty code. For each value
of `operation_number` between 0 and 3, a different piece of faulty code will raise one of the
following exceptions:

- **`ValueError`** — when bad data is provided (like `"abc"` instead of a number to `int()`)
- **`ZeroDivisionError`** — when you try to divide by zero
- **`FileNotFoundError`** — when you try to open a file that does not exist (and if it's not
  open, no need to `close()` it)
- **`TypeError`** — when you try to mix different types that cannot be mixed (did you try to add
  a string and a number?)

Other values of `operation_number` will not contain faulty code and simply return.

Create a `test_error_types()` function that:

- Shows each type of error happening
- Catches each error and explains what went wrong
- Demonstrates that your program continues running after each error
- Shows how to catch **multiple error types with one `try:` block**

### Example

```
$> python3 ft_different_errors.py
=== Garden Error Types Demo ===
Testing operation 0...
Caught ValueError: invalid literal for int() with base 10: 'abc'
Testing operation 1...
Caught ZeroDivisionError: division by zero
Testing operation 2...
Caught FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'
Testing operation 3...
Caught TypeError: can only concatenate str (not "int") to str
Testing operation 4...
Operation completed successfully

All error types tested successfully!
```

> Why does Python have different types of errors? How can you catch multiple types of errors with
> a single `try:` only? Note that you **can't use `type()`**.

> `mypy` will display an error for the faulty code that raises the `TypeError`. That's its job! So,
> to test this exception, we need to keep this error on purpose.

> You have already encountered `open()` in C. Using it in Python is pretty straightforward.

---

## Chapter VIII — Exercise 3: Making Your Own Error Types

| | |
|---|---|
| **Exercise** | 3 — `ft_custom_errors` |
| **Directory** | `ex3/` |
| **Files to Submit** | `ft_custom_errors.py` |
| **Authorized** | `print()` |

Sometimes the built-in Python errors are not specific enough for your garden program. You can
create your own error types to make your code clearer and more helpful.

### Requirements

Create these simple custom exception classes:

- **`GardenError`** — A basic error for garden problems
- **`PlantError`** — For problems with plants (inherits from `GardenError`)
- **`WaterError`** — For problems with watering (inherits from `GardenError`)

Each custom exception should:

- Be a simple class that inherits from `Exception` (or `GardenError`)
- Have a specific **default error message** (e.g. `"Unknown plant error"`) if none is provided

Create functions that:

- Raise your custom errors in different situations
- Show how to catch your specific error types
- Demonstrate that catching `GardenError` catches **all** garden-related errors

### Example

```
$> python3 ft_custom_errors.py
=== Custom Garden Errors Demo ===

Testing PlantError...
Caught PlantError: The tomato plant is wilting!

Testing WaterError...
Caught WaterError: Not enough water in the tank!

Testing catching all garden errors...
Caught GardenError: The tomato plant is wilting!
Caught GardenError: Not enough water in the tank!

All custom error types work correctly!
```

> When should you create your own error types instead of using Python's built-in ones? How does
> inheritance help organize different types of errors?

---

## Chapter IX — Exercise 4: Finally Block — Always Clean Up

| | |
|---|---|
| **Exercise** | 4 — `ft_finally_block` |
| **Directory** | `ex4/` |
| **Files to Submit** | `ft_finally_block.py` |
| **Authorized** | `print()`, `str.capitalize()` |

Your garden program needs to clean up resources, even if an error has occurred. The `finally`
block is perfect for this — it always runs, whether there was an error or not.

### Requirements

Write a function `water_plant(plant_name)` that:

- Tries to water the plant
- **Succeeds if the plant name is capitalized**
- Raises an error if the plant name is not capitalized (use your `PlantError` exception from the
  previous exercise)
- Prints a message on success

Create a `test_watering_system()` function that:

- Opens the watering system (just print a message)
- Waters several plants using `water_plant()`
- Uses `try`/`except`/`finally` structure
- Handles errors if a plant name is invalid and can't be watered. In that case, **stop the test
  and immediately return to main**
- Always closes the watering system in a `finally` block
- Shows that cleanup always happens, even when there's an error

### Example

```
$> python3 ft_finally_block.py
=== Garden Watering System ===

Testing valid plants...
Opening watering system
Watering Tomato: [OK]
Watering Lettuce: [OK]
Watering Carrots: [OK]
Closing watering system

Testing invalid plants...
Opening watering system
Watering Tomato: [OK]
Caught PlantError: Invalid plant name to water: 'lettuce'
.. ending tests and returning to main
Closing watering system

Cleanup always happens, even with errors!
```

> Why is it important to clean up resources even when errors happen? How does the `finally` block
> help ensure cleanup always occurs?

---

## Chapter X — Turn in and Submission

Turn in your assignment to your Git repository as usual. Only the work inside your repository will
be evaluated during the defense. Do not hesitate to double-check the names of your files to ensure
they are correct.

> During evaluation, you may be asked to explain error handling concepts, demonstrate how
> exceptions work in your garden programs, or show how your system handles different types of
> problems. Make sure you understand the principles behind your code.

> You need to submit only the files requested by the subject of this project. Focus on clean,
> readable code that clearly demonstrates error handling and defensive programming concepts.
