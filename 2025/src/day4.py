import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day4.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "@":
                ns = 0
                for (dr,dc) in aoc.diag_neighbours(r,c):
                    if 0 <= dr < len(input) and 0 <= dc < len(input[dr]):
                        if input[dr][dc] == "@":
                            ns += 1
                if ns < 4:
                    count += 1
    return count

def part2(input):
    count = 0
    rolls = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "@":
                rolls.add((r,c))
    
    while True:
        next = set()
        for (r,c) in rolls:
            ns = 0
            for n in aoc.diag_neighbours(r,c):
                if n in rolls:
                    ns += 1
            if ns >= 4:
                next.add((r,c))
            else:
                count += 1
        if len(rolls) == len(next):
            break
        rolls = next
    return count

if __name__ == "__main__":
    sys.exit(main())