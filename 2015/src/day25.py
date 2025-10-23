from collections import defaultdict
from email.policy import default
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day25.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    [row, col] = aoc.ints(input[0])
    code = 20151125
    r = c = 1
    while r != row or c != col:
        code *= 252533
        code %= 33554393
        r -= 1
        if r == 0:
            r = c + 1
            c = 1
        else:
            c += 1
    return code

def part2(input):
    pass

if __name__ == "__main__":
    sys.exit(main())
