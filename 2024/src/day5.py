import os
import sys
import re
import time

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    l = []
    order = dict()
    for r in range(len(input)):
        if "|" in input[r]:
            [n1, n2] = list(map(int, re.findall(r'\d+', input[r])))
            if n1 not in order:
                order[n1] = []
            order[n1].append(n2)
        elif "," in input[r]:
            bad = False
            nums = list(map(int, re.findall(r'\d+', input[r])))
            for i in range(len(nums)):
                if nums[i] in order:
                    for j in range(i-1, -1, -1):
                        if nums[j] in order[nums[i]]:
                            bad = True
            if not bad:
                l.append(nums)
                sum += nums[(len(nums) - 1)//2]
    return sum

def part2(input):
    sum = 0
    l = []
    order = dict()
    for r in range(len(input)):
        if "|" in input[r]:
            [n1, n2] = list(map(int, re.findall(r'\d+', input[r])))
            if n1 not in order:
                order[n1] = []
            order[n1].append(n2)
        elif "," in input[r]:
            bad = False
            nums = list(map(int, re.findall(r'\d+', input[r])))
            for i in range(len(nums)):
                if nums[i] in order:
                    for j in range(i-1, -1, -1):
                        if nums[j] in order[nums[i]]:
                            bad = True
            if bad:
                fixed = []
                max = len(nums)
                while len(fixed) < max:
                    idx = -1
                    for i in range(len(nums)):
                        possible = True

                        idx = i
                        for j in range(len(nums)):
                            if nums[j] in order and nums[i] in order[nums[j]]:
                                possible = False
                                break
                        
                        if possible:
                            break

                    if possible:
                        fixed.append(nums[idx])
                        del nums[idx]

                sum += fixed[(len(fixed) - 1)//2]
    
    return sum  

if __name__ == "__main__":
    sys.exit(main())