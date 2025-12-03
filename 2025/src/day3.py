import os
import sys
import utils.aoc as aoc
import itertools as it

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    output = 0
    for line in input:
        nums = [int(n) for n in line]
        best = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                val = int(str(nums[i]) + str(nums[j]))
                if val > best:
                    best = val
        output += best
    return output

def part2(input):
    output = 0
    for line in input:
        nums = [int(n) for n in line]
        i = 0
        val = ""
        while len(val) < 12:
            span = nums[i:len(nums)-(11-len(val))]
            best = max(span)
            val += str(best)
            i = i + span.index(best)+1
        output += int(val)
    return output

if __name__ == "__main__":
    sys.exit(main())