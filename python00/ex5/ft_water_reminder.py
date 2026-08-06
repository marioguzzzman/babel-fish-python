def ft_water_reminder() -> None:
    dry_day = int(input("Days since last watering: "))
    if dry_day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

