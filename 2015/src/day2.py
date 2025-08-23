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
    paper = 0
    for line in input:
        [l,w,h] = aoc.ints(line)
        paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    return paper

def part2(input):
    ribbon = 0
    for line in input:
        [s1,s2,s3] = sorted(aoc.ints(line))
        ribbon += 2*s1 + 2*s2 + s1*s2*s3
    return ribbon


if __name__ == "__main__":
    sys.exit(main())
