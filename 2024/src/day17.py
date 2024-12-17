import os
import sys
import re
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day17.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

# The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.

# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)

# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)

def adv(a, b, regs):
    combo = b if b < 4 else regs[b-4]
    return math.trunc(a / (2**combo))

def bxl(a, b, regs):
    return a ^ b

def bst(a, b, regs):
    combo = b if b < 4 else regs[b-4]
    return combo % 8

def jnz(a, b, regs):
    return -1 if a == 0 else b

def bxc(a, b, regs):
    return a ^ b

def out(a, b, regs):
    combo = b if b < 4 else regs[b-4]
    return combo % 8

def bdv(a, b, regs):
    combo = b if b < 4 else regs[b-4]
    return math.trunc(a / (2**combo))

def cdv(a, b, regs):
    combo = b if b < 4 else regs[b-4]
    return math.trunc(a / (2**combo))

def part1(input):
    regs = dict()
    regs[0] = list(map(int, re.findall(r'\d+', input[0])))[0]
    regs[1] = list(map(int, re.findall(r'\d+', input[1])))[0]
    regs[2] = list(map(int, re.findall(r'\d+', input[2])))[0]

    instructions = list(map(int, re.findall(r'\d+', input[4])))
    instructions = list(zip(*[iter(instructions)]*2))

    stdout = []
    pc = 0
    while pc < len(instructions):
        (opcode, operand) = instructions[pc]
        if opcode == 0:
            regs[0] = adv(regs[0], operand, regs)
        if opcode == 1:
            regs[1] = bxl(regs[1], operand, regs)
        if opcode == 2:
            regs[1] = bst(regs[1], operand, regs)
        if opcode == 3:
            npc = jnz(regs[0], operand, regs)
            if npc != -1:
                pc = npc
                continue
        if opcode == 4:
            regs[1] = bxc(regs[1], regs[2], regs)
        if opcode == 5:
            stdout.append(out(regs[0], operand, regs))
        if opcode == 6:
            regs[1] = bdv(regs[0], operand, regs)
        if opcode == 7:
            regs[2] = cdv(regs[0], operand, regs)
        pc+=1
        
    return ",".join([str(o) for o in stdout])
    
def part2(input):
    regs = dict()
    regs[0] = list(map(int, re.findall(r'\d+', input[0])))[0]
    regs[1] = list(map(int, re.findall(r'\d+', input[1])))[0]
    regs[2] = list(map(int, re.findall(r'\d+', input[2])))[0]

    comp = input[4].split(":")[1][1:]
    instructions = list(map(int, re.findall(r'\d+', input[4])))
    instructions = list(zip(*[iter(instructions)]*2))

    stdout = []
    pc = 0
    A = 33200148537459*8 -1
    # 33200148537459 4150018567177 518752320897 64844040080 8105504972 1013188121 126388394 15798549 1974818 246852 30856 3760 470 58 7
    while "2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0" != ",".join([str(o) for o in stdout]):
        A += 1
        stdout = []
        pc = 0
        regs[0] = A
        while pc < len(instructions):
            (opcode, operand) = instructions[pc]
            if opcode == 0:
                regs[0] = adv(regs[0], operand, regs)
            if opcode == 1:
                regs[1] = bxl(regs[1], operand, regs)
            if opcode == 2:
                regs[1] = bst(regs[1], operand, regs)
            if opcode == 3:
                npc = jnz(regs[0], operand, regs)
                if npc != -1:
                    pc = npc
                    continue
            if opcode == 4:
                regs[1] = bxc(regs[1], regs[2], regs)
            if opcode == 5:
                stdout.append(out(regs[0], operand, regs))
            if opcode == 6:
                regs[1] = bdv(regs[0], operand, regs)
            if opcode == 7:
                regs[2] = cdv(regs[0], operand, regs)
            pc+=1

    return A
if __name__ == "__main__":
    sys.exit(main())
