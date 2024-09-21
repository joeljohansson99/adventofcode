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
    freq = 0
    for line in input:
        freq += int(line)
    return freq

def part2(input):
    freqs = set()
    freq = 0
    while True:
        for line in input:
            freq += int(line)
            if freq in freqs:
                return freq
            freqs.add(freq)


if __name__ == "__main__":
    sys.exit(main())