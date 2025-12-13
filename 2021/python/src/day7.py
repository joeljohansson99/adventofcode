import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    crabs = aoc.ints(input[0])
    cheapest = float('inf')
    for p in range(min(crabs), max(crabs)):
        cost = sum([abs(crab-p) for crab in crabs])
        if cost < cheapest:
            cheapest = cost
    return cheapest

def part2(input):
    crabs = aoc.ints(input[0])
    cheapest = float('inf')
    for p in range(min(crabs), max(crabs)):
        cost = int(sum([(abs(crab-p)*(abs(crab-p)+1))/2 for crab in crabs]))
        if cost < cheapest:
            cheapest = cost
    return cheapest

if __name__ == "__main__":
    sys.exit(main())