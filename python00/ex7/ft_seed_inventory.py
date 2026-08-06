def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    s = seed_type.capitalize() + " " + "seeds:"
    if unit == "packets":
        print(f"{s} {quantity} {unit} available")
    elif unit == "grams":
        print(f"{s} {quantity} {unit} total")
    elif unit == "area":
        print(f"{s} covers {quantity} square meters")
    else:
        print("Unknown unit type")
