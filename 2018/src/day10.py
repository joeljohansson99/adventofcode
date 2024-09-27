import os
import sys
import re

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    points = dict()
    velocity = dict()
    for i in range(0, len(input)):
        [x, y, dx, dy] = list(map(int, re.findall(r'(-?\d+\.?\d*)', input[i])))
        points[i] = (x,y)
        velocity[i] = (dx,dy)
    
    while True:
        ys = set()
        xs = set()
        for i in range(0, len(input)):
            (x,y) = points[i]
            (dx,dy) = velocity[i]
            points[i] = (x+dx, y+dy)
            ys.add(y+dy)
            xs.add(x+dx)
        if len(ys) <= 10:
            for y in range(min(ys), max(ys)+1):
                for x in range(min(xs), max(xs)+1):
                    if (x,y) in points.values():
                        print(chr(9608), end="")
                    else:
                        print(" ", end="")
                print("")
            break
    return "Done"

def part2(input):
    points = dict()
    velocity = dict()
    for i in range(0, len(input)):
        [x, y, dx, dy] = list(map(int, re.findall(r'(-?\d+\.?\d*)', input[i])))
        points[i] = (x,y)
        velocity[i] = (dx,dy)
    
    sec = 1
    while True:
        ys = set()
        xs = set()
        for i in range(0, len(input)):
            (x,y) = points[i]
            (dx,dy) = velocity[i]
            points[i] = (x+dx, y+dy)
            ys.add(y+dy)
            xs.add(x+dx)
        if len(ys) <= 10:
            return sec
        sec+=1

if __name__ == "__main__":
    sys.exit(main())