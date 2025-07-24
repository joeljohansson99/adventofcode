import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

L = (-1,0)
R = (1,0)
U = (0,-1)
D = (0,1)

def add(a,b):
    return tuple(map(lambda x, y: x + y, a, b))

def part1(input):
    wire1 = set(getWire(input[0].split(",")).keys())
    wire2 = set(getWire(input[1].split(",")).keys())
    points = wire1.intersection(wire2)
    return min([abs(x) + abs(y) for (x,y) in points])
    
def part2(input):
    map1 = getWire(input[0].split(","))
    map2 = getWire(input[1].split(","))
    wire1 = set(map1.keys())
    wire2 = set(map2.keys())
    points = wire1.intersection(wire2)
    return min([map1[p] + map2[p] for p in points])

def getWire(insts):
    wire = dict()
    pos = (0,0)
    dir = None
    step = 0
    for inst in insts:
        if inst[0] == "L":
            dir = L
        elif inst[0] == "R":
            dir = R
        elif inst[0] == "U":
            dir = U
        elif inst[0] == "D":
            dir = D
        
        steps = list(map(int,re.findall(r'\d+', inst)))[0]
        for _ in range(0,steps):
            step+=1
            pos = add(pos, dir)
            wire[pos] = step
        
    return wire

if __name__ == "__main__":
    sys.exit(main())