import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day17.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    spin = int(input[0])
    buffer = [0]
    loc = 0
    for val in range(1, 2018):
        loc = (loc + spin) % len(buffer)
        buffer.insert(loc+1, val)
        loc += 1

    return buffer[loc+1]

def part2(input):
    spin = int(input[0])
    size = 1
    loc = 0
    for val in range(1, 50000000):
        loc = (loc + spin) % size
        if loc == 0:
            after = val
        size += 1
        loc += 1

    return after

if __name__ == "__main__":
    sys.exit(main())