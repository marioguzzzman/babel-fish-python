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


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.color = color
        self.has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.has_bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of" +
              f" {self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1


if __name__ == "__main__":

    f1 = Flower(name="Rose",
                height=25.0,
                age_days=30,
                growth_rate=0.8,
                color="red")

    print("=== Garden Plant Types ===")

    print("=== Flower")
    f1.show()
    print("[asking the rose to bloom]")
    f1.bloom()
    f1.show()

    print("=== Tree")
    t1 = Tree("Oak", 200.0, 365, 0.1, trunk_diameter=5.0)
    t1.show()
    print("[asking the oak to produce shade]")
    t1.produce_shade()

    print("=== Vegetable")
    v1 = Vegetable("Tomato", 5.0, 10, 2.1,
                   harvest_season="April",
                   nutritional_value=0)
    v1.show()
    growing_days = 20
    print(f"[make tomato grow and age for {growing_days} days]")
    for days in range(1, growing_days + 1):
        v1.age()
        v1.grow()
    v1.show()
