from collections import defaultdict
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
    regs = defaultdict(int)
    pc = 0
    while pc < len(input):
        info = input[pc].split(" ")
        if "hlf" == info[0]:
            regs[info[1]] /= 2
        if "tpl" == info[0]:
            regs[info[1]] *= 3
        if "inc" == info[0]:
            regs[info[1]] += 1
        if "jmp" == info[0]:
            off = getVal(info[1])
            pc+=off
            continue
        if "jie" == info[0]:
            r = info[1][0]
            off = getVal(info[2])
            if regs[r] % 2 == 0:
                pc += off 
                continue
        if "jio" == info[0]:
            r = info[1][0]
            off = getVal(info[2])
            if regs[r] == 1:
                pc += off
                continue
        pc += 1
    return regs

def part2(input):
    regs = defaultdict(int)
    regs['a'] = 1
    pc = 0
    while pc < len(input):
        info = input[pc].split(" ")
        if "hlf" == info[0]:
            regs[info[1]] /= 2
        if "tpl" == info[0]:
            regs[info[1]] *= 3
        if "inc" == info[0]:
            regs[info[1]] += 1
        if "jmp" == info[0]:
            off = getVal(info[1])
            pc+=off
            continue
        if "jie" == info[0]:
            r = info[1][0]
            off = getVal(info[2])
            if regs[r] % 2 == 0:
                pc += off 
                continue
        if "jio" == info[0]:
            r = info[1][0]
            off = getVal(info[2])
            if regs[r] == 1:
                pc += off
                continue
        pc += 1
    return regs

def getVal(val):
    if "+" == val[0]:
        return int(val[1:])
    return int(val)

if __name__ == "__main__":
    sys.exit(main())
