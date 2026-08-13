#!/usr/bin/env python3


class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self._height = height
        self._age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age_days} days old")

    def age(self) -> None:
        self._age_days += 1

    def grow(self) -> None:
        self._height += self.growth_rate

    def validate_data(self, data: float) -> bool:
        if data < 0:
            return False
        return True

    def set_height(self, new_height: float) -> bool:
        if self.validate_data(new_height):
            self._height = new_height
            print(f"Height updated: {self._height}cm")
            return True
        else:
            print(f"{self.name}: Error, height can't be negative")
            return False

    def set_age(self, new_age: int) -> bool:
        if self.validate_data(new_age):
            self._age_days = new_age
            print(f"Age updated: {self._age_days} days")
            return True
        else:
            print(f"{self.name}: Error, age can't be negative")
            return False

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days


if __name__ == "__main__":

    p1 = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    p1.show()
    p1.set_height(26.0)
    p1.set_age(31)
    if not p1.set_height(-0.6):
        print("Height update rejected")
    if not p1.set_age(-30):
        print("Age update rejected")
    print("Current state: ", end="")
    p1.show()
