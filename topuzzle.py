#!/usr/bin/env python3
"""
Read in csv. Convert to json
Across	Down    Direction	Word	Clue
10	    0	    A/D         RIDES   Alice ____ her bike

{
  "title": "Sample Puzzle",
  "by": "By Line",
  "clues": [
    { "d":"A", "n":1, "x":0, "y":0, "a":"ONEACROSS", "c":"Clue 1" },
    ]
}
"""

import argparse
import csv
import json
from pprint import pp
from typing import Literal
from dataclasses import dataclass


@dataclass(frozen=True)
class Clue:
    x: int
    y: int
    direction: Literal["A", "B"]
    word: str
    clue: str


parser = argparse.ArgumentParser()
parser.add_argument("in_file")
parser.add_argument("title")
parser.add_argument("by")

args = parser.parse_args()



start_cells = set()
clues = []

with open(args.in_file, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        x, y, direction, word, clue = row
        x = int(x)
        y = int(y)
        start_cells.add((y,x))
        clues.append(Clue(x, y, direction, word, clue))

start_cell_to_clue_number = {
    (y, x): number
    for number, (y, x) in enumerate(sorted(start_cells), start=1)
}

clue_to_number = {
    clue: start_cell_to_clue_number[(clue.y, clue.x)]
    for clue in clues
}

clues.sort(key=lambda clue: (clue.direction, clue.y, clue.x))

d = {
    "title": args.title,
    "by": args.by,
    "clues": [
        {
            "d": clue.direction,
            "n": clue_to_number[clue],
            "x": clue.x,
            "y": clue.y,
            "a": clue.word,
            "c": clue.clue,
        }
        for clue in clues
    ],
}


print(json.dumps(d, indent=4))
