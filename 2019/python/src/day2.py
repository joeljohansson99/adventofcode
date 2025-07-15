import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day2.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    ints = list(map(int,re.findall(r'\d+', input[0])))
    ints[1] = 12
    ints[2] = 2
    pc = 0
    while ints[pc] != 99:
        opcode = ints[pc]
        if opcode == 1:
            ints[ints[pc+3]] = ints[ints[pc+1]] + ints[ints[pc+2]]
        elif opcode == 2:
            ints[ints[pc+3]] = ints[ints[pc+1]] * ints[ints[pc+2]]
        pc += 4
    
    return ints[0]
    
def part2(input):
    for x in range(0,100):
        for y in range(0,100):
            ints = list(map(int,re.findall(r'\d+', input[0])))
            ints[1] = x
            ints[2] = y
            pc = 0
            while ints[pc] != 99:
                opcode = ints[pc]
                if opcode == 1:
                    ints[ints[pc+3]] = ints[ints[pc+1]] + ints[ints[pc+2]]
                elif opcode == 2:
                    ints[ints[pc+3]] = ints[ints[pc+1]] * ints[ints[pc+2]]
                pc += 4
            if ints[0] == 19690720:
                return 100*x + y
    
    return "NO FOUND!"

if __name__ == "__main__":
    sys.exit(main())