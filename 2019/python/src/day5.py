import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    ints = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))
    pc = 0
    io = list()
    io.append(1)

    while ints[pc] != 99:
        inst = str(ints[pc]).zfill(5)
        opcode = int(inst[-2:])

        if opcode == 1:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            val2 = ints[ints[pc+2]] if int(inst[-4]) == 0 else ints[pc+2]
            ints[ints[pc+3]] = val1 + val2
            pc += 4
        elif opcode == 2:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            val2 = ints[ints[pc+2]] if int(inst[-4]) == 0 else ints[pc+2]
            ints[ints[pc+3]] = val1 * val2
            pc += 4
        elif opcode == 3:
            ints[ints[pc+1]] = io.pop(0)
            pc += 2
        elif opcode == 4:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            io.append(val1)
            pc += 2
    
    return io
    
def part2(input):
    ints = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))
    pc = 0
    io = list()
    io.append(5)

    while ints[pc] != 99:
        inst = str(ints[pc]).zfill(5)
        opcode = int(inst[-2:])

        if opcode == 1:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            val2 = ints[ints[pc+2]] if int(inst[-4]) == 0 else ints[pc+2]
            ints[ints[pc+3]] = val1 + val2
            pc += 4
        elif opcode == 2:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            val2 = ints[ints[pc+2]] if int(inst[-4]) == 0 else ints[pc+2]
            ints[ints[pc+3]] = val1 * val2
            pc += 4
        elif opcode == 3:
            ints[ints[pc+1]] = io.pop(0)
            pc += 2
        elif opcode == 4:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            io.append(val1)
            pc += 2
        elif opcode == 5:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            val2 = ints[ints[pc+2]] if int(inst[-4]) == 0 else ints[pc+2]
            if val1 != 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 6:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            val2 = ints[ints[pc+2]] if int(inst[-4]) == 0 else ints[pc+2]
            if val1 == 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 7:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            val2 = ints[ints[pc+2]] if int(inst[-4]) == 0 else ints[pc+2]
            ints[ints[pc+3]] = 1 if val1 < val2 else 0 
            pc += 4
        elif opcode == 8:
            val1 = ints[ints[pc+1]] if int(inst[-3]) == 0 else ints[pc+1]
            val2 = ints[ints[pc+2]] if int(inst[-4]) == 0 else ints[pc+2]
            ints[ints[pc+3]] = 1 if val1 == val2 else 0 
            pc += 4
    
    return io


if __name__ == "__main__":
    sys.exit(main())