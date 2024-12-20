import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day20.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    area = set()
    walls = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "S":
                start = (r,c)
                area.add((r,c))
            elif input[r][c] == "E":
                end = (r,c)
                area.add((r,c))
            elif input[r][c] == ".":
                area.add((r,c))
            elif input[r][c] == "#":
                walls.add((r,c))
    
    step_map = bfs(area, start, end)

    return sum([v for (k,v) in cheat(walls,step_map).items() if k >= 100])

def part2(input):
    area = set()
    walls = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "S":
                start = (r,c)
                area.add((r,c))
            elif input[r][c] == "E":
                end = (r,c)
                area.add((r,c))
            elif input[r][c] == ".":
                area.add((r,c))
            elif input[r][c] == "#":
                walls.add((r,c))
    
    step_map = bfs(area, start, end)
    return sum([v for (k,v) in cheat2(step_map,area).items() if k >= 100])

def cheat2(step_map, area):
    saved = dict()
    for (r,c) in area:
        reachable = find_shortcuts((r,c), step_map)
        reachable = [(step,rr,cc) for (step, rr,cc) in reachable if step_map[(r,c)] < step_map[(rr,cc)]]
        for (step, rr,cc) in reachable:
            diff = abs(step_map[(rr,cc)] - step_map[(r,c)]) - step
            if diff >= 100:
                if diff not in saved:
                    saved[diff] = 1
                else:
                    saved[diff] += 1
    return saved

def find_shortcuts(start, step_map):
    visited = set()
    current = set()
    reachable = set()
    current.add(start)
    visited.add(start)
    step = 1
    for _ in range(20):
        next = set()
        for (r,c) in current:
            for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if (dr,dc) not in visited:
                    next.add((dr,dc))
                    visited.add((dr,dc))
                    if (dr,dc) in step_map:
                        reachable.add((step, dr, dc))
        current = next
        step += 1
    return reachable

def cheat(walls, step_map):
    saved = dict()
    for (r,c) in walls:
        diff = 0
        if (r+1,c) in step_map and (r-1,c) in step_map:
            diff = abs(step_map[(r+1,c)] - step_map[(r-1,c)]) -2
        elif (r,c+1) in step_map and (r,c-1) in step_map:
            diff = abs(step_map[(r,c+1)] - step_map[(r,c-1)]) -2
        if diff != 0:
            if diff not in saved:
                saved[diff] = 1
            else:
                saved[diff] += 1
    return saved

def bfs(area, start, end):
    visited = set()
    current = set()
    current.add(start)
    visited.add(start)
    step_map = dict()
    step_map[start] = 0
    steps = 1
    while current:
        next = set()
        for (r, c) in current:
            for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if (dr,dc) in area and (dr,dc) not in visited:
                    next.add((dr,dc))
                    visited.add((dr,dc))
                    step_map[(dr,dc)] = steps
        current = next
        if end in current:
            break
        steps += 1
    return step_map

if __name__ == "__main__":
    sys.exit(main())