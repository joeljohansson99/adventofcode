from collections import defaultdict
import copy
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    bits = [defaultdict(int) for _ in input[0]]
    for num in input:
        for i in range(len(num)):
            bits[i][num[i]] += 1
    mc = ""
    lc = ""
    for bit in bits:
        mc += max(bit, key=bit.get)
        lc += min(bit, key=bit.get)

    return int(mc,2)*int(lc,2)

def part2(input):
    ox_nums = copy.copy(input)
    co_nums = copy.copy(input)
    for i in range(len(input[0])):
        ox_bits = defaultdict(int)
        for num in ox_nums:
            ox_bits[num[i]] += 1
        co_bits = defaultdict(int)
        for num in co_nums:
            co_bits[num[i]] += 1

        ox_keep = '1' if ox_bits['1'] >= ox_bits['0'] else '0'
        co_keep = '0' if co_bits['1'] >= co_bits['0'] else '1'

        ox_nums = [n for n in ox_nums if n[i] == ox_keep]
        if len(co_nums) != 1:
            co_nums = [n for n in co_nums if n[i] == co_keep]

    return int(ox_nums[0],2)*int(co_nums[0],2)

if __name__ == "__main__":
    sys.exit(main())