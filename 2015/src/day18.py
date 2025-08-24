import os
import re
import sys
from types import CodeType
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day18.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    N = len(input)
    lights = dict()
    for r in range(N):
        for c in range(N):
            lights[(r,c)] = input[r][c] == "#"

    for _ in range(100):
        next_lights = dict()
        for r in range(N):
            for c in range(N):
                on = 0
                for (dr,dc) in aoc.diag_neighbours(r,c):
                    if 0 <= dr < N and 0 <= dc < N:
                        on += 1 if lights[(dr,dc)] else 0
                if lights[(r,c)]:
                    next_lights[(r,c)] = 2 <= on <= 3
                if not lights[(r,c)]:
                    next_lights[(r,c)] = on == 3
        lights = next_lights
                    
    on = 0
    for r in range(N):
        for c in range(N):
            if lights[(r,c)]:
                on += 1
    return on

def part2(input):
    N = len(input)
    lights = dict()
    for r in range(N):
        for c in range(N):
            if (c == 0 or c == N-1) and (r == 0 or r == N-1):
                lights[(r,c)] = True
            else:
                lights[(r,c)] = input[r][c] == "#"

    for _ in range(100):
        next_lights = dict()
        for r in range(N):
            for c in range(N):
                if (c == 0 or c == N-1) and (r == 0 or r == N-1):
                    next_lights[(r,c)] = True
                    continue
                on = 0
                for (dr,dc) in aoc.diag_neighbours(r,c):
                    if 0 <= dr < N and 0 <= dc < N:
                        on += 1 if lights[(dr,dc)] else 0
                if lights[(r,c)]:
                    next_lights[(r,c)] = 2 <= on <= 3
                if not lights[(r,c)]:
                    next_lights[(r,c)] = on == 3
        lights = next_lights
                    
    on = 0
    for r in range(N):
        for c in range(N):
            if lights[(r,c)]:
                on += 1
    return on

if __name__ == "__main__":
    sys.exit(main())
