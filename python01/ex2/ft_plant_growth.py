#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age_days: int
    growth_rate: float

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height += self.growth_rate


if __name__ == "__main__":
    p1 = Plant()
    p1.name = "Rose"
    p1.height = 25.0
    p1.age_days = 30
    p1.growth_rate = 0.8

    print("=== Garden Plant Growth ===")
    h_start = p1.height
    p1.show()
    for simulation_days in range(1, 8):
        print(f"=== Day {simulation_days} ===")
        p1.age()
        p1.grow()
        p1.show()
    print(f"Growth this week: {round(p1.height - h_start, 1)}cm")
