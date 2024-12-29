import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day2.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    for line in input:
        nums = list(map(int, re.findall(r'\d+', line)))
        sum += max(nums)-min(nums)
    return sum
                

def part2(input):
    sum = 0
    for line in input:
        nums = list(map(int, re.findall(r'\d+', line)))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if max(nums[i], nums[j]) % min(nums[i], nums[j]) == 0:
                    sum += max(nums[i], nums[j]) / min(nums[i], nums[j])
            
    return int(sum)

if __name__ == "__main__":
    sys.exit(main())