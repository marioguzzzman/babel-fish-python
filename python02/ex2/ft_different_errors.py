#! /usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        30/0
    elif operation_number == 2:
        f = open("/non/existent/file")
        print(f.read())
    elif operation_number == 3:
        "abc" + 50
    else:
        return


def test_error_types() -> None:
    operation_numbers = [0, 1, 2, 3, 4]
    for operation in operation_numbers:
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
