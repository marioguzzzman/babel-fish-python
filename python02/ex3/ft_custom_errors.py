#! /usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self.message = message
        super().__init__(message)


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_all_plant_errors() -> None:
    try:
        print("Testing PlantError...")
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    try:
        print("Testing WaterError...")
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    try:
        print("Testing catching all garden errors...")
        test_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        print("Testing catching all garden errors...")
        test_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_all_plant_errors()
    print()
    print("All custom error types work correctly!")
