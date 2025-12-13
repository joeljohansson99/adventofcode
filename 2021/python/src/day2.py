import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day2.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    hor = 0
    ver = 0
    for line in input:
        if "forward" in line:
            hor += aoc.ints(line)[0]
        elif "down" in line:
            ver += aoc.ints(line)[0]
        elif "up" in line:
            ver -= aoc.ints(line)[0]
    return hor*ver

def part2(input):
    hor = 0
    ver = 0
    aim = 0
    for line in input:
        if "forward" in line:
            hor += aoc.ints(line)[0]
            ver += aoc.ints(line)[0]*aim
        elif "down" in line:
            aim += aoc.ints(line)[0]
        elif "up" in line:
            aim -= aoc.ints(line)[0]
    return hor*ver

if __name__ == "__main__":
    sys.exit(main())