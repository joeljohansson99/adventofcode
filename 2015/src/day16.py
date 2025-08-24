import os
import re
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day16.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

TICKER_TAPE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1 
}

def part1(input):
    for i in range(len(input)):
        for (obj,val) in re.findall(r"(\w+):\s*(\d+)", input[i]):
            if TICKER_TAPE[obj] != int(val):
                break
        else:
            return i+1


def part2(input):
    for i in range(len(input)):
        for (obj,val) in re.findall(r"(\w+):\s*(\d+)", input[i]):
            if obj == "cats" or obj == "trees":
                if TICKER_TAPE[obj] >= int(val):
                    break
            elif obj == "pomeranians" or obj == "goldfish":
                if TICKER_TAPE[obj] <= int(val):
                    break
            elif TICKER_TAPE[obj] != int(val):
                break
        else:
            return i+1


if __name__ == "__main__":
    sys.exit(main())
