from collections import defaultdict
import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day25.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(inputs):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', inputs[0])))
    mem = defaultdict(int)
    for i in range(len(nums)):
        mem[i] = nums[i]
    rel = 0
    pc = 0
    inp = ""
    pos = (0,0)
    seen = set()
    seen.add(pos)
    while True:
        (output, pc, rel, mem) = run_intcode(mem, pc, rel, inp)
        output = "".join(output)
        if output.replace("\n", "").replace(" ", "") == "Command?":
            print(output, end="")
            inp = input() + "\n"
            if inp == "north\n":
                pos = (pos[0]-1, pos[1])
                seen.add(pos)
            if inp == "south\n":
                pos = (pos[0]+1, pos[1])
                seen.add(pos)
            if inp == "east\n":
                pos = (pos[0], pos[1]+1)
                seen.add(pos)
            if inp == "west\n":
                pos = (pos[0], pos[1]-1)
                seen.add(pos)
            if inp == "print\n":
                print_map(pos, seen)
            

        elif (output.replace("\n", "").replace(" ", "")) != 0:
            print(output, end="")

def print_map(pos, seen):
    cols = [c for (r,c) in seen]
    rows = [r for (r,c) in seen]

    for r in range(min(rows)-1, max(rows)+2):
        for c in range(min(cols)-1, max(cols)+2):
            if (r,c) == pos:
                print("X", end="")
            elif (r,c) in seen:
                print(".", end="")
            else:
                print(" ", end="")
        print("")

def part2(input):
    pass

def run_intcode(mem, pc, rel, input):
    output = []
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
            val = ord(input[i])
            i+=1
            write(mem, pc+1, int(inst[-3]), rel, val)
            pc += 2
        elif opcode == 4:
            val = read(mem, pc+1, int(inst[-3]), rel)
            output.append(chr(val))
            pc += 2
            if val == 10:
                return (output, pc, rel, mem)
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