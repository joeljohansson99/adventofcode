import os
import sys
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day1.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    for line in input:
        mass = int(line)
        fuel = math.floor(mass/3) - 2
        sum += fuel
    return sum

def part2(input):
    sum = 0
    stack = []
    for line in input:
        stack.append(int(line))

    while stack:
        mass = stack.pop(0)
        fuel = math.floor(mass/3) - 2
        if fuel > 0:
            sum += fuel
            stack.append(fuel)
    return sum

if __name__ == "__main__":
    sys.exit(main())