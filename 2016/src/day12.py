from collections import defaultdict
import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    pc = 0
    regs = defaultdict(int)
    while pc < len(input):
        [op, *par] = input[pc].split()
        if op == "cpy":
            [x,y] = par
            regs[y] = get_num(x, regs)
        if op == "inc":
            [x] = par
            regs[x] += 1
        if op == "dec":
            [x] = par
            regs[x] -= 1
        if op == "jnz":
            [x,y] = par
            if get_num(x, regs) != 0:
                pc += get_num(y, regs)
                continue
        pc+=1
    
    return regs['a']

def part2(input):
    pc = 0
    regs = defaultdict(int)
    regs['c'] = 1
    while pc < len(input):
        [op, *par] = input[pc].split()
        if op == "cpy":
            [x,y] = par
            regs[y] = get_num(x, regs)
        if op == "inc":
            [x] = par
            regs[x] += 1
        if op == "dec":
            [x] = par
            regs[x] -= 1
        if op == "jnz":
            [x,y] = par
            if get_num(x, regs) != 0:
                pc += get_num(y, regs)
                continue
        pc+=1
    
    return regs['a']

def get_num(x, regs):
    return int(x) if is_num(x) else regs[x]

def is_num(x):
    if x[0] in ('-', '+'):
        return x[1:].isdigit()
    return x.isdigit()

if __name__ == "__main__":
    sys.exit(main())
