#! /usr/bin/env python3

import sys
import typing


def recover_file() -> str | None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return None
    elif len(sys.argv) == 2:
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO = open(sys.argv[1])
            print("---")
            print()
            content = f.read()
            print(content)
            print("---")
            f.close()
            print(f"File '{sys.argv[1]}' closed.")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
            return None
        return content
    return None


def preserve_file(f) -> None:
    print("Transform data:")
    f = f.replace("\n", "#\n")
    print(f)
    print("Enter new file name (or empty):")
    filename_user = input()
    if filename_user == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{filename_user}'")
        new_file = open(filename_user, "w")
        new_file.write(f)
        new_file.close()
        print(f"Data saved in file '{filename_user}'")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    ancient_text = recover_file()
    if ancient_text is not None:
        preserve_file(ancient_text)
