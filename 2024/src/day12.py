import functools
import os
import sys
import re
from shapely import LineString
from shapely.geometry import Polygon

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    garden = dict()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] not in garden:
                garden[input[r][c]] = set()
            garden[input[r][c]].add((r,c))
    
    regions = dict()
    for (pot,posses) in garden.items():
        regions[pot] = []
        all_visited = set()
        for pos in posses:
            if pos not in all_visited:
                region = bfs(input, pos)
                regions[pot].append(region)
                all_visited = all_visited.union(region)
    
    price = 0
    for (pot,regions) in regions.items():
        for region in regions:
            perimiter = 0
            for pos in region:
                perimiter += check_perimiter(pos, region)
            price += (perimiter*len(region))
    
    return price


def part2(input):
    garden = dict()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] not in garden:
                garden[input[r][c]] = set()
            garden[input[r][c]].add((r,c))
    
    regions = dict()
    for (pot,posses) in garden.items():
        regions[pot] = []
        all_visited = set()
        for pos in posses:
            if pos not in all_visited:
                region = bfs(input, pos)
                regions[pot].append(region)
                all_visited = all_visited.union(region)
    
    price = 0
    for (pot,regions) in regions.items():
        for region in regions:
            perimiter = check_walls(region, input)
            price += (perimiter*len(region))
    return price

def check_walls(region, input):
    up_sides = set()
    down_sides = set()
    left_sides = set()
    right_sides = set()
    for (r,c) in region:
        if (r-1,c) not in region:
            down_sides.add((r-1,c))
        if (r+1,c) not in region:
            up_sides.add((r+1,c))
        if (r,c-1) not in region:
            right_sides.add((r,c-1))
        if (r,c+1) not in region:
            left_sides.add((r,c+1))

    walls = 0
    visited = set()
    for side in up_sides:
        if side not in visited:
            wall = find_wall(up_sides, side)
            visited = visited.union(wall)
            walls += 1

    visited = set()
    for side in down_sides:
        if side not in visited:
            wall = find_wall(down_sides, side)
            visited = visited.union(wall)
            walls += 1

    visited = set()
    for side in left_sides:
        if side not in visited:
            wall = find_wall(left_sides, side)
            visited = visited.union(wall)
            walls += 1

    visited = set()
    for side in right_sides:
        if side not in visited:
            wall = find_wall(right_sides, side)
            visited = visited.union(wall)
            walls += 1

    return walls

def check_perimiter(pos, region):
    (r,c) = pos
    count = 0
    for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if (dr,dc) not in region:
            count+=1
    
    return count

def find_wall(sides, start):
    visited = set()
    current = set()
    current.add(start)
    visited.add(start)
    while current:
        next = set()
        for (r, c) in current:
            for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if (dr,dc) in sides and (dr,dc) not in visited:
                    next.add((dr,dc))
                    visited.add((dr,dc))

        current = next
    return visited

def bfs(input, start):
    visited = set()
    current = set()
    current.add(start)
    visited.add(start)
    while current:
        next = set()
        for (r, c) in current:
            for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= dr < len(input) and 0 <= dc < len(input[0]) and input[dr][dc] == input[r][c] and (dr,dc) not in visited:
                    next.add((dr,dc))
                    visited.add((dr,dc))

        current = next
    return visited

if __name__ == "__main__":
    sys.exit(main())