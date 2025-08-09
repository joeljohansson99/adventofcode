import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day1.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    pos = (0,0)
    dir = (1,0)
    instructions = [inst.strip() for inst in input[0].split(",")]
    for inst in instructions:
        (turn, steps) = (inst[0], int(inst[1:]))
        if turn == "L":
            dir = aoc.left(dir)
        if turn == "R":
            dir = aoc.right(dir)
        pos = (pos[0]+dir[0]*steps, pos[1]+dir[1]*steps)
    
    return abs(pos[0]) + abs(pos[1])

def part2(input):
    pos = (0,0)
    dir = (1,0)
    seen = set()
    instructions = [inst.strip() for inst in input[0].split(",")]
    for inst in instructions:
        (turn, steps) = (inst[0], int(inst[1:]))
        if turn == "L":
            dir = aoc.left(dir)
        if turn == "R":
            dir = aoc.right(dir)
        
        for _ in range(steps):
            if pos in seen:
                return abs(pos[0]) + abs(pos[1])
            seen.add(pos)
            pos = (pos[0]+dir[0], pos[1]+dir[1])

if __name__ == "__main__":
    sys.exit(main())
