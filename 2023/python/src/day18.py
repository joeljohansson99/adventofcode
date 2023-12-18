import os
import sys
from shapely.geometry import Point, Polygon
import numpy as np 

R = (0,1)
L = (0,-1)
U = (-1,0)
D = (1,0)

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day18.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    trench = []
    pos = (0,0)
    for cmd in input:
        (dir, steps, _) = cmd.split(" ")
        for i in range(0, int(steps)):
            if dir == "R":
                pos = add(pos, R)
            elif dir == "L":
                pos = add(pos, L)
            elif dir == "U":
                pos = add(pos, U)
            elif dir == "D":
                pos = add(pos, D)
        trench.append(pos)
    
    poly = Polygon(trench)
    return int(poly.area + poly.length // 2 + 1)

def part2(input):
    trench = []
    pos = (0,0)
    trench.append(pos)
    for cmd in input:
        (_, _, code) = cmd.split(" ")
        code = code[2:-1]
        dir = code[-1]
        steps = int(code[:-1], 16)
        if dir == "0":
            pos = add(pos, (0, steps))
        elif dir == "2":
            pos = add(pos, (0, -1*steps))
        elif dir == "3":
            pos = add(pos, (-1*steps, 0))
        elif dir == "1":
            pos = add(pos, (steps, 0))
        
        trench.append((pos))
    
    poly = Polygon(trench)
    return int(poly.area + poly.length // 2 + 1)

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

if __name__ == "__main__":
    sys.exit(main())