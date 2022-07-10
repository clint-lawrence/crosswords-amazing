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


parser = argparse.ArgumentParser()
parser.add_argument("in_file")
parser.add_argument("title")
parser.add_argument("by")

args = parser.parse_args()

d = {
    "title": args.title,
    "by": args.by,
    "clues": []
}

with open(args.in_file, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for i, row in enumerate(csv_reader):
        x, y, direction, word, clue = row
        d["clues"].append(
            {
                "d": direction,
                "n": i+1,
                "x": int(x),
                "y": int(y),
                "a": word,
                "c": clue
            }
        )
        
print(json.dumps(d, indent=4))