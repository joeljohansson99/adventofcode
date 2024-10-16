import time
import os
import sys

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day18.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

OPEN = 0
WOOD = 1
LUMBER = 2

def part1(input):
    acres = dict()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == ".":
                acres[(r,c)] = OPEN
            elif input[r][c] == "|":
                acres[(r,c)] = WOOD
            elif input[r][c] == "#":
                acres[(r,c)] = LUMBER

    for _ in range(10):
        next = dict()
        for (acre, type) in acres.items():
            if type == OPEN:
                next[acre] = WOOD if get_neighbours(acre, acres).count(WOOD) >= 3 else OPEN
            if type == WOOD:
                next[acre] = LUMBER if get_neighbours(acre, acres).count(LUMBER) >= 3 else WOOD
            if type == LUMBER:
                neighbors = get_neighbours(acre, acres)
                next[acre] = LUMBER if neighbors.count(LUMBER) >= 1 and neighbors.count(WOOD) >= 1 else OPEN
        acres = next

    types = [type for (_,type) in acres.items()]

    return types.count(WOOD) * types.count(LUMBER)

def part2(input):
    acres = dict()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == ".":
                acres[(r,c)] = OPEN
            elif input[r][c] == "|":
                acres[(r,c)] = WOOD
            elif input[r][c] == "#":
                acres[(r,c)] = LUMBER

    rows = range(len(input))
    cols = range(len(input[0]))

    cache = dict()

    min = 0
    end = 1000000000
    while min < end:
        key = hash(acres, rows, cols)
        if key in cache:
            loop = min - cache[key]
            factor = end
            while factor != 1:
                while min + loop*factor < end:
                    min += loop*factor
                factor = factor / 10
        else:
            cache[key] = min
        next = dict()
        for (acre, type) in acres.items():
            if type == OPEN:
                next[acre] = WOOD if get_neighbours(acre, acres).count(WOOD) >= 3 else OPEN
            if type == WOOD:
                next[acre] = LUMBER if get_neighbours(acre, acres).count(LUMBER) >= 3 else WOOD
            if type == LUMBER:
                neighbors = get_neighbours(acre, acres)
                next[acre] = LUMBER if neighbors.count(LUMBER) >= 1 and neighbors.count(WOOD) >= 1 else OPEN
        acres = next
        min+=1

    types = [type for (_,type) in acres.items()]

    return types.count(WOOD) * types.count(LUMBER)

def hash(acres, rows, cols):
    hash = ""
    for r in rows:
        for c in cols:
            hash += str(acres[(r,c)])
    return hash

def print_acres(acres, rows, cols):
    for r in rows:
        for c in cols:
            if acres[(r,c)] == OPEN:
                print(".", end="")
            if acres[(r,c)] == WOOD:
                print("|", end="")
            if acres[(r,c)] == LUMBER:
                print("#", end="")
        print("")

def get_neighbours(square, acres):
    neighbors = list()
    (r,c) = square
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if (r+dr, c+dc) in acres and (r+dr, c+dc) != square:
                neighbors.append(acres[(r+dr, c+dc)])
    return neighbors

if __name__ == "__main__":
    sys.exit(main())