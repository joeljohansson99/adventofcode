import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for line in input:
        sides = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', line)))
        (a,b,c) = sorted(sides)
        if a + b > c:
            count += 1
    return count


def part2(input):
    count = 0
    for r in range(0, len(input), 3):
        for c in range(3):
            a = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[r])))[c]
            b = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[r+1])))[c]
            c = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[r+2])))[c]
            (a,b,c) = sorted([a,b,c])
            if a + b > c:
                count += 1
    return count

if __name__ == "__main__":
    sys.exit(main())
