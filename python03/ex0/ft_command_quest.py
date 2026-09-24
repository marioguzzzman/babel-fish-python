#! /usr/bin/env python3

import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) == 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {len(sys.argv) - 1}")
for num in range(1, len(sys.argv)):
    print(f"Argument {num}: {sys.argv[num]}")
print(f"Total arguments: {len(sys.argv)}")
