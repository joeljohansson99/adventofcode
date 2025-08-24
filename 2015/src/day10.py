import os
import sys
from itertools import groupby

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    seq = input[0]

    for _ in range(40):
        seq = look_and_say(seq)

    return len(seq)

def part2(input):
    seq = input[0]

    for _ in range(50):
        seq = look_and_say(seq)

    return len(seq)


def look_and_say(n):
    return ''.join(str(len(list(g))) + k for k, g in groupby(n))


if __name__ == "__main__":
    sys.exit(main())
