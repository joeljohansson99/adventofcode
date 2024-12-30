import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day9.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    stream = input[0]

    skip = False
    level = 0
    groups = 0
    garbage = False
    for c in stream:
        if skip:
            skip = False
        elif c == "!":
            skip = True
        elif c == "<":
            garbage = True
        elif c == ">":
            garbage = False
        elif c == "{" and not garbage:
            level += 1
        elif c == "}" and level != 0 and not garbage:
            groups += level
            level -= 1
    
    return groups

def part2(input):
    stream = input[0]

    skip = False
    garbage = False
    count = 0
    for c in stream:
        if skip:
            skip = False
        elif c == "!":
            skip = True
        elif c == "<" and not garbage:
            garbage = True
        elif c == ">":
            garbage = False
        elif garbage:
            count += 1

    return count

if __name__ == "__main__":
    sys.exit(main())