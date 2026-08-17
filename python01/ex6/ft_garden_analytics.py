#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def show_stats(self) -> None:
            print(f"Stats: "
                  f"{self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self,
                 name: str,
                 height: float,
                 age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self._height = height
        self._age_days = age_days
        self.growth_rate = growth_rate
        self._stats = Plant.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age_days} days old")
        self._stats.add_show()

    def age(self) -> None:
        self._age_days += 1
        self._stats.add_age()

    def grow(self) -> None:
        self._height += self.growth_rate
        self._stats.add_grow()

    def show_plant_stats(self) -> None:
        self._stats.show_stats()

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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        if age < 365:
            return False
        else:
            return True

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Unknown plant",
                   height=0.0,
                   age_days=0,
                   growth_rate=0.0)


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


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age_days: int, growth_rate: float,
                 color: str) -> None:
        super().__init__(name, height,
                         age_days, growth_rate,
                         color)
        self.seed_count = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42


class Tree(Plant):

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls += 1

        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self._shade_calls} shade")

    _stats: "Tree.Stats"

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self._stats = Tree.Stats()
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._stats.add_shade()
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


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_plant_stats()


if __name__ == "__main__":

    f1 = Flower(name="Rose",
                height=25.0,
                age_days=30,
                growth_rate=0.8,
                color="red")

    print("=== Garden statistics ===")

    print("=== Check year-old")
    age = 30
    print(f"Is {age} days more than a year? -> "
          f"{Plant.is_older_than_year(age)}")
    age = 400
    print(f"Is {age} days more than a year? -> "
          f"{Plant.is_older_than_year(age)}")

    print("=== Flower")
    f1.show()
    display_statistics(f1)
    print("[asking the rose to grow and bloom]")
    f1.grow()
    f1.bloom()
    f1.show()
    display_statistics(f1)

    print("=== Tree")
    t1 = Tree("Oak", 200.0, 365, 0.1, trunk_diameter=5.0)
    t1.show()
    display_statistics(t1)
    print("[asking the oak to produce shade]")
    t1.produce_shade()
    display_statistics(t1)

    print("=== Seed")
    s1 = Seed(name="Sunflower",
              height=80.0,
              age_days=45,
              growth_rate=0.8,
              color="yellow")

    s1.show()
    print("[make sunflower grow, age and bloom]")
    s1.grow()
    s1.age()
    s1.bloom()
    s1.show()
    display_statistics(s1)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)
