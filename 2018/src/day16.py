import opcode
import os
import re
import sys

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day16.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def addr(a, b, regs):
    return regs[a] + regs[b]
def addi(a, b, regs):
    return regs[a] + b
def mulr(a, b, regs):
    return regs[a] * regs[b]
def muli(a, b, regs):
    return regs[a] * b
def banr(a, b, regs):
    return regs[a] & regs[b]
def bani(a, b, regs):
    return regs[a] & b
def borr(a, b, regs):
    return regs[a] | regs[b]
def bori(a, b, regs):
    return regs[a] | b
def setr(a, b, regs):
    return regs[a]
def seti(a, b, regs):
    return a
def gtir(a, b, regs):
    return int(a > regs[b])
def gtri(a, b, regs):
    return int(regs[a] > b)
def gtrr(a, b, regs):
    return int(regs[a] > regs[b])
def eqir(a, b, regs):
    return int(a == regs[b])
def eqri(a, b, regs):
    return int(regs[a] == b)
def eqrr(a, b, regs):
    return int(regs[a] == regs[b])

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def part1(input):
    i = 0
    samples = list()
    while i < len(input):
        if len(input[i]) == 0:
            i += 1
            continue
        if "Before" not in input[i]:
            break
        before = list(map(int, re.findall(r'\d+', input[i])))
        inst = list(map(int, re.findall(r'\d+', input[i+1])))
        after = list(map(int, re.findall(r'\d+', input[i+2])))
        samples.append((before, inst, after))
        i+=3
    
    count = 0
    for sample in samples:
        if len(predict_op(sample)) >= 3:
            count += 1
    
    return count

def part2(input):
    i = 0
    samples = list()
    program = list()
    while i < len(input):
        if len(input[i]) == 0:
            i += 1
            continue
        if "Before" not in input[i]:
            program.append(list(map(int, re.findall(r'\d+', input[i]))))
            i += 1
            continue
        before = list(map(int, re.findall(r'\d+', input[i])))
        inst = list(map(int, re.findall(r'\d+', input[i+1])))
        after = list(map(int, re.findall(r'\d+', input[i+2])))
        samples.append((before, inst, after))
        i+=3
    
    opcodes = dict()
    for i in range(16):
        opcodes[i] = set(range(16))

    for sample in samples:
        code = sample[1][0]
        prediction = predict_op(sample)
        opcodes[code] = set.intersection(opcodes[code], prediction)

    pruning = True
    found = set()
    done = set()
    while pruning:
        pruning = False
        for code in range(16):
            if code not in done and len(opcodes[code]) == 1:
                done.add(code)
                opcodes[code] = next(iter(opcodes[code]))
                found.add(opcodes[code])
                pruning = True
        
        for code in range(16):
            if code not in done:
                opcodes[code] -= found

    regs = [0,0,0,0]
    for [code, a, b, c] in program:
        regs[c] = ops[opcodes[code]](a,b,regs)
        
    return regs[0]   

def predict_op(sample):
    (before, inst, after) = sample
    [_, a, b, c] = inst
    prediction = set()

    for i in range(0, len(ops)):
        if after[c] == ops[i](a, b, before):
            prediction.add(i)

    return prediction





if __name__ == "__main__":
    sys.exit(main())