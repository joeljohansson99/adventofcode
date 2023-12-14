import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day14.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    rocks = []
    input = [list(x) for x in input]
    for r in range(0, len(input)):
        for c in range(0, len(input[0])):
            if input[r][c] == 'O':
                rocks.append((r,c))
    
    rocks = north(input, rocks)
    
    return countRocks(rocks, len(input))

def part2(input):
    rocks = []
    input = [list(x) for x in input]
    for r in range(0, len(input)):
        for c in range(0, len(input[0])):
            if input[r][c] == 'O':
                rocks.append((r,c))
                
    loops = dict()
    for i in range(0, 300):
        rocks = cycle(input, rocks)
        key = tuple(rocks)
        if key in loops:
            diff = i-loops[key]
            if (1000000000 - 1 - i) % diff == 0:
                break
        else:
            loops[key] = i
    
    return countRocks(rocks, len(input))

def countRocks(rocks, bottom):
    ret = 0
    for rock in rocks:
        ret += bottom - rock[0]
    return ret

def cycle(map, rocks):
    rocks = north(map, rocks)
    rocks = west(map, rocks)
    rocks = south(map, rocks)
    rocks = east(map, rocks)
    return rocks

def east(map, rocks):
    new_rocks = []
    rocks.sort(key=lambda x: x[1], reverse=True)
    for rock in rocks:
        map[rock[0]][rock[1]] = '.'
        pos = (rock[0], len(map[rock[0]])-1)
        for c in range(rock[1], len(map[rock[0]])-1):
            if map[rock[0]][c+1] != '.':
                pos = (rock[0], c)
                break
        map[pos[0]][pos[1]] = 'O'
        new_rocks.append(pos)
    return new_rocks

def west(map, rocks):
    new_rocks = []
    rocks.sort(key=lambda x: x[1])
    
    for rock in rocks:
        map[rock[0]][rock[1]] = '.'
        pos = (rock[0], 0)
        for c in range(rock[1], 0, -1):
            if map[rock[0]][c-1] != '.':
                pos = (rock[0], c)
                break
        map[pos[0]][pos[1]] = 'O'
        new_rocks.append(pos)
    return new_rocks

def south(map, rocks):
    new_rocks = []
    rocks.sort(key=lambda x: x[0], reverse=True)
    
    for rock in rocks:
        map[rock[0]][rock[1]] = '.'
        pos = (len(map)-1,rock[1])
        for r in range(rock[0], len(map)-1):
            if map[r+1][rock[1]] != '.':
                pos = (r, rock[1])
                break
        map[pos[0]][pos[1]] = 'O'
        new_rocks.append(pos)
    return new_rocks

def north(map, rocks):
    rocks.sort(key=lambda x: x[0])
    new_rocks = []
    for rock in rocks:
        map[rock[0]][rock[1]] = '.'
        pos = (0,rock[1])
        for r in range(rock[0], 0, -1):
            if map[r-1][rock[1]] != '.':
                pos = (r, rock[1])
                break
        map[pos[0]][pos[1]] = 'O'
        new_rocks.append(pos)
    return new_rocks

if __name__ == "__main__":
    sys.exit(main())