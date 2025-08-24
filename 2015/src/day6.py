from collections import defaultdict
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    N = 1000
    lights = defaultdict(bool)
    for line in input:
        if "turn on" in line:
            [x1,y1,x2,y2] = aoc.ints(line)
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    lights[(x,y)] = True
        elif "turn off" in line:
            [x1,y1,x2,y2] = aoc.ints(line)
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    lights[(x,y)] = False
        elif "toggle" in line:
            [x1,y1,x2,y2] = aoc.ints(line)
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    lights[(x,y)] = not lights[(x,y)]
    
    count = 0
    for y in range(N):
        for x in range(N):
            if lights[(x,y)]:
                count += 1
    return count

def part2(input):
    N = 1000
    lights = defaultdict(int)
    for line in input:
        if "turn on" in line:
            [x1,y1,x2,y2] = aoc.ints(line)
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    lights[(x,y)] += 1
        elif "turn off" in line:
            [x1,y1,x2,y2] = aoc.ints(line)
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    lights[(x,y)] = max(lights[(x,y)]-1, 0)
        elif "toggle" in line:
            [x1,y1,x2,y2] = aoc.ints(line)
            for y in range(y1,y2+1):
                for x in range(x1,x2+1):
                    lights[(x,y)] += 2
    
    brightess = 0
    for y in range(N):
        for x in range(N):
            brightess += lights[(x,y)]
    return brightess

if __name__ == "__main__":
    sys.exit(main())
