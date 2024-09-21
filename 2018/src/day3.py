import os
import re
import sys

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    claims = dict()
    for line in input:
        [_, sx, sy, dx, dy] = list(map(int, re.findall(r'\d+', line)))
        for x in range(sx, sx+dx):
            for y in range(sy, sy+dy):
                claims[(x,y)] = claims[(x,y)]+1 if (x,y) in claims else 1
    
    sum = 0
    for count in claims.values():
        if count > 1:
            sum += 1
    
    return sum

def part2(input):
    claims = dict()
    for line in input:
        [_, sx, sy, dx, dy] = list(map(int, re.findall(r'\d+', line)))
        for x in range(sx, sx+dx):
            for y in range(sy, sy+dy):
                claims[(x,y)] = claims[(x,y)]+1 if (x,y) in claims else 1

    for line in input:
        [elf, sx, sy, dx, dy] = list(map(int, re.findall(r'\d+', line)))
        intact = True
        for x in range(sx, sx+dx):
            for y in range(sy, sy+dy):
                if claims[(x,y)] > 1:
                    intact = False
                    break
            if not intact:
                break
        
        if intact:
            return elf


if __name__ == "__main__":
    sys.exit(main())