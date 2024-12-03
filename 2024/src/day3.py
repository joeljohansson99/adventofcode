import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    input = "\n".join(line for line in input)
    res = 0
    pattern = re.compile(r"mul\(\d+(?:,\d+)?\)")
    for case in pattern.findall(input):
        nums = list(map(int, re.findall(r'\d+', case)))
        if len(nums) == 2:
            [l,r] = nums
            if l < 1000 and r < 1000:
                res += l*r

    return res


def part2(input):
    input = "\n".join(line for line in input)
    res = 0
    do = True
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    for case in pattern.findall(input):
        if "don't" in case:
            do = False
        elif "do" in case:
            do = True
        elif "mul" in case and do:
            nums = list(map(int, re.findall(r'\d+', case)))
            if len(nums) == 2:
                [l,r] = nums
                if l < 1000 and r < 1000:
                    res += l*r    

    return res

if __name__ == "__main__":
    sys.exit(main())