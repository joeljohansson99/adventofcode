from collections import defaultdict
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day19.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    elfs = int(input[0])
    low = 1
    high = elfs
    round = 0

    while low != high:
        if elfs % 2 != 0:
            low += pow(2, round+1)
        else:
            high -= pow(2, round)
        elfs = elfs // 2
        round += 1
    
    return low


def part2(input):
    elfs = list(range(int(input[0])))
    while len(elfs) != 1:
        elfs.pop(len(elfs)//2)
        elfs.append(elfs.pop(0))
    
    return elfs[0]+1

if __name__ == "__main__":
    sys.exit(main())
