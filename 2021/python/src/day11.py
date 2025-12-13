import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    rows = len(input)
    cols = len(input[0])
    octos = dict()
    for r in range(rows):
        for c in range(cols):
            octos[(r,c)] = int(input[r][c])

    flashes = 0
    for _ in range(100):
        flashed = set()
        for o in octos.keys():
            octos[o] += 1
        
        flashing = True
        while flashing:
            flashing = False
            for ((r,c),e) in octos.items():
                if e >= 10:
                    flashes+=1
                    flashed.add((r,c))
                    for n in aoc.diag_neighbours(r,c):
                        if n not in flashed and n in octos:
                            octos[n] += 1
                    octos[(r,c)] = 0
                    flashing = True
    return flashes

def part2(input):
    rows = len(input)
    cols = len(input[0])
    octos = dict()
    for r in range(rows):
        for c in range(cols):
            octos[(r,c)] = int(input[r][c])
    step = 0
    while not sum(octos.values()) == 0:
        flashed = set()
        for o in octos.keys():
            octos[o] += 1
        
        flashing = True
        while flashing:
            flashing = False
            for ((r,c),e) in octos.items():
                if e >= 10:
                    flashed.add((r,c))
                    for n in aoc.diag_neighbours(r,c):
                        if n not in flashed and n in octos:
                            octos[n] += 1
                    octos[(r,c)] = 0
                    flashing = True
        step+=1
    return step

if __name__ == "__main__":
    sys.exit(main())