from collections import defaultdict
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    points = defaultdict(int)
    for line in input:
        [x1,y1,x2,y2] = aoc.ints(line)
        if x1 == x2 or y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    points[(x,y)] += 1

    return len([p for (p,v) in points.items() if v > 1])

def part2(input):
    points = defaultdict(int)
    for line in input:
        [x1,y1,x2,y2] = aoc.ints(line)
        if x1 == x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                points[(x1,y)] += 1
        elif y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                points[(x,y1)] += 1
        else:
            for d in range(abs(x1 - x2)+1):
                x = x1+d if x1 < x2 else x1-d
                y = y1+d if y1 < y2 else y1-d
                points[(x,y)] += 1
                d+=1

    return len([p for (p,v) in points.items() if v > 1])

if __name__ == "__main__":
    sys.exit(main())