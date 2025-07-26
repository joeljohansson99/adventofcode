from collections import defaultdict
import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))
    mem = defaultdict(int)
    for i in range(len(nums)):
        mem[i] = nums[i]
    rel = 0
    pc = 0
    dir = U
    whites = set()
    pos = (0,0)
    first = True
    painted = set()
    
    while mem[pc] != 99:
        inst = str(mem[pc]).zfill(5)
        opcode = int(inst[-2:])

        if opcode == 1:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, val1 + val2)
            pc += 4
        elif opcode == 2:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, val1 * val2)
            pc += 4
        elif opcode == 3:
            val = 1 if pos in whites else 0
            write(mem, pc+1, int(inst[-3]), rel, val)
            pc += 2
        elif opcode == 4:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            if first:
                first = False
                if val1 == 0:
                    whites.remove(pos)
                if val1 == 1:
                    whites.add(pos)
                painted.add(pos)
            else:
                first = True
                dir = turn(dir, val1)
                pos = (pos[0]+dir[0], pos[1]+dir[1])
            pc += 2
        elif opcode == 5:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            if val1 != 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 6:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            if val1 == 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 7:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, 1 if val1 < val2 else 0)
            pc += 4
        elif opcode == 8:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, 1 if val1 == val2 else 0)
            pc += 4
        elif opcode == 9:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            rel += val1
            pc += 2
    
    return len(painted)

def part2(input):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))
    mem = defaultdict(int)
    for i in range(len(nums)):
        mem[i] = nums[i]
    rel = 0
    pc = 0
    dir = U
    whites = set()
    pos = (0,0)
    first = True
    whites.add(pos)

    while mem[pc] != 99:
        inst = str(mem[pc]).zfill(5)
        opcode = int(inst[-2:])

        if opcode == 1:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, val1 + val2)
            pc += 4
        elif opcode == 2:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, val1 * val2)
            pc += 4
        elif opcode == 3:
            val = 1 if pos in whites else 0
            write(mem, pc+1, int(inst[-3]), rel, val)
            pc += 2
        elif opcode == 4:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            if first:
                first = False
                if val1 == 0 and pos in whites:
                    whites.remove(pos)
                if val1 == 1:
                    whites.add(pos)
            else:
                first = True
                dir = turn(dir, val1)
                pos = (pos[0]+dir[0], pos[1]+dir[1])
            pc += 2
        elif opcode == 5:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            if val1 != 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 6:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            if val1 == 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 7:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, 1 if val1 < val2 else 0)
            pc += 4
        elif opcode == 8:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, 1 if val1 == val2 else 0)
            pc += 4
        elif opcode == 9:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            rel += val1
            pc += 2
    
    rows = [r for (r,c) in whites]
    cols = [c for (r,c) in whites]
    for c in range(min(cols)-1, max(cols)+2):
        for r in range(min(rows)-1, max(rows)+2):
            if (r,c) in whites:
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    return None

def read(mem, i, mode, rel):
    if mode == 0:
        return mem[mem[i]]
    elif mode == 1:
        return mem[i]
    elif mode == 2:
        return mem[rel+mem[i]]

def write(mem, i, mode, rel, val):
    if mode == 0:
        mem[mem[i]] = val
    if mode == 1:
        sys.exit(-1)
    if mode == 2:
        mem[rel+mem[i]] = val


L = (-1,0)
R = (1,0)
U = (0,-1)
D = (0,1)

def turn(dir, inp):
    if inp == 0:
        if dir == L:
            return D
        elif dir == D:
            return R
        elif dir == R:
            return U
        elif dir == U:
            return L
    elif inp == 1:
        if dir == L:
            return U
        elif dir == D:
            return L
        elif dir == R:
            return D
        elif dir == U:
            return R
        

if __name__ == "__main__":
    sys.exit(main())