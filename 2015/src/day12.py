import os
import sys
import json
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    return sum(aoc.ints(input[0]))

def part2(input):
    obj = json.loads(input[0])
    return findCount(obj)

def findCount(obj):
    count = 0
    if isinstance(obj, dict):
        for v in obj.values():
            if v == "red":
                return 0
            count += findCount(v)
    elif isinstance(obj, list):
        for v in obj:
            count += findCount(v)
    elif isinstance(obj, int):
        return obj
    return count

if __name__ == "__main__":
    sys.exit(main())
