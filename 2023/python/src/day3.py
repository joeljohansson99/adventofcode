import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)
    
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))
    
def part1(input):
    nums = []
    num = ""
    index = []
    for r in range (0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c].isdigit():
                num += input[r][c]
                index.append([r,c])
            else:
                if num != "":
                    nums.append((num, index))
                    num = ""
                    index = []
        if num != "":
            nums.append((num, index))
            num = ""
            index = []
                    
    sum = 0
    for (num, idx) in nums:
        found = False
        for [r,c] in idx:
            for dr in range(-1, 2):
                for dc in range(-1,2):
                    indr = max(min(r+dr, len(input)-1), 0)
                    indc = max(min(c+dc, len(input[0])-1), 0)
                    if input[indr][indc] != '.' and not input[indr][indc].isdigit():
                        sum = sum + int(num)
                        found = True
                        break
                if found:
                    break
            if found:
                break
    return sum

def part2(input):
    nums = []
    num = ""
    index = []
    gears = dict()
    for r in range (0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c].isdigit():
                num += input[r][c]
                index.append([r,c])
            else:
                if num != "":
                    nums.append((num, index))
                    num = ""
                    index = []
                if input[r][c] == '*':
                    gears[(r,c)] = []
        if num != "":
            nums.append((num, index))
            num = ""
            index = []
                    
    for (num, idx) in nums:
        done = []
        for [r,c] in idx:
            for dr in range(-1, 2):
                for dc in range(-1,2):
                    indr = max(min(r+dr, len(input)-1), 0)
                    indc = max(min(c+dc, len(input[0])-1), 0)
                    if input[indr][indc] == '*' and not [indr, indc] in done:
                        gears[(indr,indc)].append(int(num))
                        done.append([indr, indc])
                        break
    
    sum = 0
    for _, nums in gears.items():
        if len(nums) == 2:
            sum += nums[0] * nums[1]
    return sum



if __name__ == "__main__":
    sys.exit(main())