#! /usr/bin/env python3

from sys import argv


def show_argv() -> None:
    """ Print the program name, each command-line argument,
    and the total argument count.
    """
    # total number of arguments
    n = len(argv)
    # the name of the program
    pname = argv[0]

    print("=== Command Quest ===")
    print(f"Program name: {pname}")
    # No arg entered
    if n == 1:
        print("No arguments provided!")
    # 1 or more arg entered
    else:
        print(f"Arguments received: {len(argv) - 1}")
        for num in range(1, len(argv)):
            print(f"Argument {num}: {argv[num]}")
    print(f"Total arguments: {n}")


if __name__ == "__main__":
    show_argv()
