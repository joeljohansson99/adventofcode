from collections import defaultdict
import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day17.txt') as f:
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
    scaffolds = set()
    (x,y) = (0,0)
    
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
            val = 0
            write(mem, pc+1, int(inst[-3]), rel, val)
            pc += 2
        elif opcode == 4:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            char = chr(val1)
            if char == "#":
                scaffolds.add((x,y))
            if char == "\n":
                y += 1
                x = 0
            else:
                x += 1
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

    count = 0
    for (r,c) in scaffolds:
        if all(n in scaffolds for n in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]):
            count += r*c
    return count

def part2(input):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))
    mem = defaultdict(int)
    for i in range(len(nums)):
        mem[i] = nums[i]
    rel = 0
    pc = 0
    mem[0] = 2

    program = "A,B,A,C,A,C,B,C,C,B\nL,4,L,4,L,10,R,4\nR,4,L,4,L,4,R,8,R,10\nR,4,L,10,R,10\nn\n"
    pi = 0
    collected = 0
    
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
            val = ord(program[pi])
            pi+=1
            write(mem, pc+1, int(inst[-3]), rel, val)
            pc += 2
        elif opcode == 4:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            collected = val1
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
    
    return collected

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

if __name__ == "__main__":
    sys.exit(main())