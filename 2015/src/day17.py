from functools import reduce
from operator import mul
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day17.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    cups = aoc.ints(" ".join(input))
    return len(getCombinations([], cups, 150, set()))

def part2(input):
    cups = aoc.ints(" ".join(input))
    combs = getCombinations([], cups, 150, set())
    min_len = min([len(comb) for comb in combs])
    return sum([1 if len(comb) == min_len else 0 for comb in combs])

def getCombinations(comb, cups, L, seen):
    key = tuple(sorted(comb))
    if key in seen:
        return []
    seen.add(key)
    filled = sum([cups[i] for i in comb])
    if filled == L:
        return [comb]
    elif filled > L:
        return []

    combs = []
    for i in range(len(cups)):
        if i not in comb:
            combs = combs + getCombinations(comb + [i], cups, L, seen)
    return combs

if __name__ == "__main__":
    sys.exit(main())
