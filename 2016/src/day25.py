from collections import defaultdict
import math
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day25.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    over = 2534
    num = 1
    while num < over or num % 2 != 0:
        if num % 2 == 0:
            num = num * 2 + 1
        else:
            num = num * 2
    
    return num - over

def part2(input):
    pass

def get_num(x, regs):
    return int(x) if is_num(x) else regs[x]

def is_num(x):
    if x[0] in ('-', '+'):
        return x[1:].isdigit()
    return x.isdigit()

if __name__ == "__main__":
    sys.exit(main())
