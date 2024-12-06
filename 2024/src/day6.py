import os
import sys
import re
import time

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    pos = (-1,-1)
    dir = (-1,-1)
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "^":
                dir = (-1, 0)
                pos = (r,c)
            elif input[r][c] == "v":
                dir = (1, 0)
                pos = (r,c)
            elif input[r][c] == "<":
                dir = (0, -1)
                pos = (r,c)
            elif input[r][c] == ">":
                dir = (0, 1)
                pos = (r,c)
    
    visited = set()
    visited.add(pos)
    while True:
        next = (pos[0] + dir[0], pos[1]+dir[1])
        if not (0 <= next[0] < len(input) and 0 <= next[1] < len(input[0])):
            break
        if input[next[0]][next[1]] == "#":
            if dir == (-1, 0):
                dir = (0, 1)
            elif dir == (1, 0):
                dir = (0, -1)
            elif dir == (0, -1):
                dir = (-1, 0)
            elif dir == (0, 1):
                dir = (1, 0)
        

        pos = (pos[0] + dir[0], pos[1]+dir[1])
        visited.add(pos)
    
    return len(visited)

def part2(input):
    start = (-1,-1)
    dir2 = (-1,-1)
    pos = (-1,-1)
    dir = (-1,-1)
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "^":
                dir = (-1, 0)
                dir2 = (-1, 0)
                start = (r,c)
                pos = (r,c)
            elif input[r][c] == "v":
                dir = (1, 0)
                dir2 = (1, 0)
                start = (r,c)
                pos = (r,c)
            elif input[r][c] == "<":
                dir = (0, -1)
                dir2 = (0, -1)
                start = (r,c)
                pos = (r,c)
            elif input[r][c] == ">":
                dir = (0, 1)
                dir2 = (0, 1)
                start = (r,c)
                pos = (r,c)
    visited = set()
    visited.add(pos)
    while True:
        next = (pos[0] + dir[0], pos[1]+dir[1])
        if not (0 <= next[0] < len(input) and 0 <= next[1] < len(input[0])):
            break
        if input[next[0]][next[1]] == "#":
            if dir == (-1, 0):
                dir = (0, 1)
            elif dir == (1, 0):
                dir = (0, -1)
            elif dir == (0, -1):
                dir = (-1, 0)
            elif dir == (0, 1):
                dir = (1, 0)
        

        pos = (pos[0] + dir[0], pos[1]+dir[1])
        visited.add(pos)
    
    count = 0
    for ob in visited:
        if ob == start:
            continue
        
        cache = set()
        p = start
        d = dir2

        while True:
            next = (p[0] + d[0], p[1]+d[1])
            if not (0 <= next[0] < len(input) and 0 <= next[1] < len(input[0])):
                break
            if input[next[0]][next[1]] == "#" or next == ob:
                if d == (-1, 0):
                    d = (0, 1)
                elif d == (1, 0):
                    d = (0, -1)
                elif d == (0, -1):
                    d = (-1, 0)
                elif d == (0, 1):
                    d = (1, 0)
                continue
            
            if (p, d) in cache:
                count += 1
                break
            else:
                cache.add((p,d))

            p = (p[0] + d[0], p[1]+d[1])
            
    return count

if __name__ == "__main__":
    sys.exit(main())