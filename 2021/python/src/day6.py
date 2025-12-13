from collections import defaultdict
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    fishes = defaultdict(int)
    for fish in aoc.ints(input[0]):
        fishes[fish] += 1
    
    for _ in range(80):
        next = defaultdict(int)
        for (i, count) in fishes.items():
            if i == 0:
                next[8] = count
                next[6] += count
            else:
                next[(i-1)] += count
        fishes = next
    return sum(fishes.values())

def part2(input):
    fishes = defaultdict(int)
    for fish in aoc.ints(input[0]):
        fishes[fish] += 1

    for _ in range(256):
        next = defaultdict(int)
        for (i, count) in fishes.items():
            if i == 0:
                next[8] = count
                next[6] += count
            else:
                next[(i-1)] += count
        fishes = next
    return sum(fishes.values())

if __name__ == "__main__":
    sys.exit(main())