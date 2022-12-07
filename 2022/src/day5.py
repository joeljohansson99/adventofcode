import re
import sys
from copy import deepcopy

def main():
    input = []
    instrs = []
    with open('input/day5.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            if "move" in l:
                instrs.append([int(n) for n in re.findall(r'\d+',l)])
            elif l != '':
                input.append(l)

    stacks = []
    idxs = []

    for i in range(0,len(input[len(input)-1])):
        if input[len(input)-1][i].isdigit():
            stacks.append([])
            idxs.append(i)

    for line in reversed(input[:len(input)-1]):
        for i in range(0, len(idxs)):
            if (line[idxs[i]] != ' '):
                stacks[i].append(line[idxs[i]])

    print("Part 1: " + str(part1(deepcopy(stacks), instrs)))
    print("Part 2: " + str(part2(deepcopy(stacks), instrs)))

def part1(stacks, instrs):
    for instr in instrs:
        [amount, fro, to] = instr
        for i in range(0,amount):
            stacks[to-1].append(stacks[fro-1].pop())
    
    ret = ""
    for stack in stacks:
        ret += stack.pop()
    return ret

def part2(stacks, instrs):
    for instr in instrs:
        [amount, fro, to] = instr
        stacks[to-1] = stacks[to-1] + stacks[fro-1][-amount:]
        del stacks[fro-1][-amount:]
    
    ret = ""
    for stack in stacks:
        ret += stack.pop()
    return ret

if __name__ == "__main__":
    sys.exit(main())