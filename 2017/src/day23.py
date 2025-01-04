from collections import defaultdict
import os
import sys

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
    count = 0
    while 0 <= pc < len(input):
        [op, * params] = input[pc].split(" ")
        [x,y] = params
        if op == "set":
            regs[x] = int(y) if check_int(y) else regs[y]
        elif op == "sub":
            regs[x] -= int(y) if check_int(y) else regs[y]
        elif op == "mul":
            regs[x] *= int(y) if check_int(y) else regs[y]
            count += 1
        elif op == "jnz":
            if int(y) if check_int(x) else regs[x] != 0:
                pc += int(y) if check_int(y) else regs[y]
                continue
        pc += 1
    
    return count

def part2(input):
    b = 105700
    c = 122700
    h = 0
    while b <= c:
        f = 1
        for i in range(2, b):
            if b%i == 0: 
                f = 0
                break
            
        if f == 0:
            h+=1
        b+=17

    return h

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

if __name__ == "__main__":
    sys.exit(main())