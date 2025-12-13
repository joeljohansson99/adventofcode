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
    nums = [int(line) for line in input]
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
    return count


def part2(input):
    nums = [int(line) for line in input]
    count = 0
    for i in range(1, len(nums)-2):
        if sum(nums[i:i+3]) > sum(nums[i-1:i+2]):
            count += 1
    return count

if __name__ == "__main__":
    sys.exit(main())