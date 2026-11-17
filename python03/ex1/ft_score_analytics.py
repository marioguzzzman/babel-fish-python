#! /usr/bin/env python3

from sys import argv


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    scores = []
    for arg in argv[1:]:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    players = len(scores)
    if players > 0:
        score_total = sum(scores)
        score_average = score_total / players
        score_max = max(scores)
        score_min = min(scores)
        score_range = score_max - score_min
        print(f"Scores processed: {scores}")
        print(f"Total players: {players}")
        print(f"Total score: {score_total}")
        print(f"Average score: {score_average}")
        print(f"High score: {score_max}")
        print(f"Low score: {score_min}")
        print(f"Score range: {score_range}")
    else:
        print(
            "No scores provided. Usage: python3 "
            f"{argv[0]} <score1> <score2> ...")


if __name__ == "__main__":
    score_analytics()
