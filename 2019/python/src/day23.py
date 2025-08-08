from collections import defaultdict
import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day23.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))

    mems = list()
    pcs = list()
    rels = list()
    ios = list()
    outs = list()
    for i in range(50):
        mems.append(defaultdict(int))
        for k in range(len(nums)):
            mems[i][k] = nums[k]
        pcs.append(0)
        rels.append(0)
        ios.append([i])
        outs.append(list())

    while True:
        for id in range(50):
            run_intcode(mems, pcs, rels, ios, outs, id)
            if len(outs[id]) == 3:
                (a, x, y) = outs[id]
                if a == 255:
                    return y
                ios[a].append(x)
                ios[a].append(y)
                outs[id] = list()

def part2(input):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))

    mems = list()
    pcs = list()
    rels = list()
    ios = list()
    outs = list()
    for i in range(50):
        mems.append(defaultdict(int))
        for k in range(len(nums)):
            mems[i][k] = nums[k]
        pcs.append(0)
        rels.append(0)
        ios.append([i])
        outs.append(list())

    NAT_x = None
    NAT_y = None
    prev_y = None
    while True:
        for id in range(50):
            run_intcode(mems, pcs, rels, ios, outs, id)
            if len(outs[id]) == 3:
                (a, x, y) = outs[id]
                if a == 255:
                    NAT_x = x
                    NAT_y = y
                else:
                    ios[a].append(x)
                    ios[a].append(y)
                outs[id] = list()
        
        if all([len(ios[i]) == 0 for i in range(50)]) and NAT_y is not None:
            if prev_y == NAT_y:
                return NAT_y
            prev_y = NAT_y
            ios[0].append(NAT_x)
            ios[0].append(NAT_y)

def run_intcode(mems, pcs, rels, ios, outs, id):
    while mems[id][pcs[id]] != 99:
        inst = str(mems[id][pcs[id]]).zfill(5)
        opcode = int(inst[-2:])

        if opcode == 1:
            val1 = read(mems[id], pcs[id]+1, int(inst[-3]), rels[id])
            val2 = read(mems[id], pcs[id]+2, int(inst[-4]), rels[id])
            write(mems[id], pcs[id]+3, int(inst[-5]), rels[id], val1 + val2)
            pcs[id] += 4
        elif opcode == 2:
            val1 = read(mems[id], pcs[id]+1, int(inst[-3]), rels[id])
            val2 = read(mems[id], pcs[id]+2, int(inst[-4]), rels[id])
            write(mems[id], pcs[id]+3, int(inst[-5]), rels[id], val1 * val2)
            pcs[id] += 4
        elif opcode == 3:
            waiting = len(ios[id]) == 0
            val = ios[id].pop(0) if not waiting else -1
            write(mems[id], pcs[id]+1, int(inst[-3]), rels[id], val)
            pcs[id] += 2
            if waiting:
                return
        elif opcode == 4:
            val = read(mems[id], pcs[id]+1, int(inst[-3]), rels[id])
            outs[id].append(val)
            pcs[id] += 2
            if len(outs[id]) == 3:
                return
        elif opcode == 5:
            val1 = read(mems[id], pcs[id]+1, int(inst[-3]), rels[id])
            val2 = read(mems[id], pcs[id]+2, int(inst[-4]), rels[id])
            if val1 != 0:
                pcs[id] = val2
            else:
                pcs[id] += 3
        elif opcode == 6:
            val1 = read(mems[id], pcs[id]+1, int(inst[-3]), rels[id])
            val2 = read(mems[id], pcs[id]+2, int(inst[-4]), rels[id])
            if val1 == 0:
                pcs[id] = val2
            else:
                pcs[id] += 3
        elif opcode == 7:
            val1 = read(mems[id], pcs[id]+1, int(inst[-3]), rels[id])
            val2 = read(mems[id], pcs[id]+2, int(inst[-4]), rels[id])
            write(mems[id], pcs[id]+3, int(inst[-5]), rels[id], 1 if val1 < val2 else 0)
            pcs[id] += 4
        elif opcode == 8:
            val1 = read(mems[id], pcs[id]+1, int(inst[-3]), rels[id])
            val2 = read(mems[id], pcs[id]+2, int(inst[-4]), rels[id])
            write(mems[id], pcs[id]+3, int(inst[-5]), rels[id], 1 if val1 == val2 else 0)
            pcs[id] += 4
        elif opcode == 9:
            val1 = read(mems[id], pcs[id]+1, int(inst[-3]), rels[id])
            rels[id] += val1
            pcs[id] += 2

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