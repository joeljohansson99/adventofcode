import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day1.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    dial = 50
    count = 0
    for line in input:
        t = aoc.ints(line)[0]
        if "L" in line:
            dial = (dial-t) % 100
        else:
            dial = (dial+t) % 100
        if dial == 0:
            count += 1
    return count

def part2(input):
    dial = 50
    count = 0
    for line in input:
        t = aoc.ints(line)[0]
        if "L" in line:
            for _ in range(t):
                dial = (dial + 1) % 100
                if dial == 0:
                    count += 1
        if "R" in line:
            for _ in range(t):
                dial = (dial + 1) % 100
                if dial == 0:
                    count += 1
    return count

if __name__ == "__main__":
    sys.exit(main())