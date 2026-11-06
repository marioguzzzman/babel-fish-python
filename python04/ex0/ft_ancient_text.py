#! /usr/bin/env python3

import sys
import typing


def recover_file() -> None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
    elif len(sys.argv) == 2:
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO = open(sys.argv[1])
            print("---")
            print()
            print(f.read())
            print("---")
            f.close()
            print(f"File '{sys.argv[1]}' closed.")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    recover_file()
