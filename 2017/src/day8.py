from collections import defaultdict
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day8.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    regs = defaultdict(int)
    
    for line in input:
        [ops, case] = line.split(" if ")
        ops = ops.split(" ")
        case = case.split(" ")
        if check(case, regs):
            do(ops, regs)
    
    return max(regs.values())

def part2(input):
    regs = defaultdict(int)
    highest = 0
    for line in input:
        [ops, case] = line.split(" if ")
        ops = ops.split(" ")
        case = case.split(" ")
        if check(case, regs):
            do(ops, regs)
        highest = max(highest, max(regs.values()))
    
    return highest

def check(case, regs):
    [reg, comp, val] = case
    vreg = regs[reg]
    if comp == "==" and vreg == int(val):
        return True
    if comp == "!=" and vreg != int(val):
        return True
    if comp == "<=" and vreg <= int(val):
        return True
    if comp == "<" and vreg < int(val):
        return True
    if comp == ">=" and vreg >= int(val):
        return True
    if comp == ">" and vreg > int(val):
        return True

def do(ops, regs):
    [reg, op, val] = ops
    if op == "inc":
        regs[reg] += int(val)
    if op == "dec":
        regs[reg] -= int(val)

if __name__ == "__main__":
    sys.exit(main())