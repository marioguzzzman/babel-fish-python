#! /usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    temp_str = "25"
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C", end="\n\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    temp_str = "abc"
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")
