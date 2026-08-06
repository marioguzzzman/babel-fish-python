def user_input() -> int:
    target = int(input("Days until harvest: "))
    return target


def counter(target: int, day: int) -> None:
    if day == target:
        print("Harvest time!")
    else:
        print(f"Day {day + 1}")
        counter(target, day + 1)


def ft_count_harvest_recursive() -> None:
    day = 0
    target = user_input()
    counter(target, day)
