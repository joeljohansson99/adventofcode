from collections import defaultdict
import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day19.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    N = 50
    count = 0
    for y in range(N):
        for x in range(N):
            count += run(x, y, input)
    return count

def part2(input):
    (x,y) = (5,6)
    while True:
        if not run(x,y,input):
            (x,y) = (x-1,y)
        if run(x-99, y+99, input):
            return (x-99)*10000 + y
        (x,y) = (x+1,y+1)

def run(x,y, input):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))
    mem = defaultdict(int)
    for i in range(len(nums)):
        mem[i] = nums[i]
    rel = 0
    pc = 0
    i = 0
    
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
            val = (x,y)[i%2]
            i+=1
            write(mem, pc+1, int(inst[-3]), rel, val)
            pc += 2
        elif opcode == 4:
            return read(mem, pc+1, int(inst[-3]), rel)
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

if __name__ == "__main__":
    sys.exit(main())