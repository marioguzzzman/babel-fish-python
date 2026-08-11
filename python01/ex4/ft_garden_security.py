#!/usr/bin/env python 3


class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 age_days: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height += self.growth_rate

if __name__ == "__main__":

    p1 = Plant("Rose", 25.0, 30, 0.8)
    p2 = Plant("Sunflower", 80.0, 54, 0.9)
    p3 = Plant("Cactus", 15.0, 120, 0.1)
    p4 = Plant("Flower", 5.0, 1, 0.3)
    p5 = Plant("Palm", 10.0, 12, 0.6)

    garden = [p1, p2, p3, p4, p5]

    print("=== Plant Factory Output ===")
    for plant in garden:
        print("Created: ", end="")
        plant.show()