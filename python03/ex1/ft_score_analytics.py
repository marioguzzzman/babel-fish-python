#! /usr/bin/env python3

import sys

def score_analytics() -> None:
    n_players = len(sys.argv)
    scores = []
    for arg in sys.argv:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    print("=== Player Score Analytics ===")

    if n_players == 1:
        print(f"No scores provided: Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        print(f"Scores processed: {n_players - 1}")

    return

if __name__ == "_name_":
    score_analytics()