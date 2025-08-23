import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day1.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    line = input[0]
    return line.count("(") - line.count(")")

def part2(input):
    line = input[0]
    floor = 0
    for i in range(len(line)):
        if line[i] == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i+1

if __name__ == "__main__":
    sys.exit(main())
