import os
import sys
import re
import time

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    for line in input:
        [res, nums] = line.split(":")
        nums = nums.split(" ")[1:]
        val = int(res)

        res = set()
        res.add(int(nums[0]))
        for i in range(1, len(nums)):
            new_res = set()
            for r in res:
                new_res.add(r + int(nums[i]))
                new_res.add(r * int(nums[i]))
            res = new_res
            
        for r in res:
            if r == val:
                sum += val
                break
    
    return sum

def part2(input):
    sum = 0
    for line in input:
        [res, nums] = line.split(":")
        nums = nums.split(" ")[1:]
        val = int(res)

        res = set()
        res.add(int(nums[0]))
        for i in range(1, len(nums)):
            new_res = set()
            for r in res:
                new_res.add(r + int(nums[i]))
                new_res.add(r * int(nums[i]))
                new_res.add(int(str(r)+nums[i]))
            res = new_res
            
        for r in res:
            if r == val:
                sum += val
                break
    
    return sum

if __name__ == "__main__":
    sys.exit(main())