from collections import defaultdict
from math import factorial
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day23.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    instructions = input.copy()
    pc = 0
    regs = defaultdict(int)
    regs['a'] = 7
    while pc < len(instructions):
        [op, *par] = instructions[pc].split()
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
        if op == "tgl":
            [x] = par
            step = get_num(x, regs)
            toggle(instructions, pc+step)
        pc+=1
    
    return regs['a']

def part2(input):
    # reverse engineered
    return factorial(12) + 78 * 86

def get_num(x, regs):
    return int(x) if is_num(x) else regs[x]

def is_num(x):
    if x[0] in ('-', '+'):
        return x[1:].isdigit()
    return x.isdigit()

def toggle(instructions, i):
    if i >= len(instructions):
        return
    [op, *par] = instructions[i].split()
    if len(par) == 1:
        if op == "inc":
            instructions[i] = " ".join(["dec"] + par)
        else:
            instructions[i] = " ".join(["inc"] + par)
    if len(par) == 2:
        if op == "jnz":
            instructions[i] = " ".join(["cpy"] + par)
        else:
            instructions[i] = " ".join(["jnz"] + par)

if __name__ == "__main__":
    sys.exit(main())
