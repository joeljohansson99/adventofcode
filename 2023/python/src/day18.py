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
    trench = set()
    pos = (0,0)
    trench.add(pos)
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
            trench.add((pos))
    
    minC = 0
    minR = 0
    for (r,c) in trench:
        if r < minR:
            minR = r
        if c < minC:
            minC = c
    
    norm = set()
    for (r,c) in trench:
        norm.add((r-minR, c-minC))
        
    maxR = max([r for (r,c) in norm])
    maxC = max([c for (r,c) in norm])
    
    out = bfs(norm, maxR, maxC)
    
    count = 0
    for r in range(0,maxR+1):
        for c in range(0,maxC+1):
            if (r,c) in norm or (r,c) in out:
                pass
            else:
                count+=1 
    return count + len(norm)

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
    y = np.array([r for (r,c) in trench])
    x = np.array([c for (r,c) in trench])
    return PolyArea(x,y)

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

def bfs(trench, maxR, maxC):
    seen = set()
    currents = set()
    currents.add((-1,-1))
    seen.add((-1, -1))
    while currents:
        next = set()
        for (r,c) in currents:
            for (dr,dc) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if (dr,dc) in seen or (dr,dc) in trench:
                    continue
                if dr < -1 or dr > maxR+1 or dc < -1 or dc > maxC+1:
                    continue
                else:
                    next.add((dr,dc))
                    seen.add((dr,dc))
        currents = next
    return seen
                        
        

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

if __name__ == "__main__":
    sys.exit(main())