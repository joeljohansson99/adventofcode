import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    data = int(input[0])
    inc = 2
    carry = 2
    num = 1
    while True:
        for _ in range(4):
            if num <= data <= num+inc:
                high = num+inc
                low = num
                while data != high and data != low:
                    carry -= 1
                    high -= 1
                    low += 1
                return carry
            num += inc
        inc += 2
        carry += 2

def part2(input):
    data = int(input[0])
    grid = dict()
    grid[(0,0)] = 1
    dir = (0,1)
    pos = (0,1)
    grid[pos] = 1
    while True:
        if add(pos, left(dir)) not in grid:
            dir = left(dir)
            continue
        else:
            pos = add(pos, dir)
            grid[pos] = sum([grid[n] for n in neighbours(pos) if n in grid])
            if grid[pos] > data:
                return grid[pos]

def neighbours(pos):
    (r,c) = pos
    return [(r+1,c+1), (r+1,c), (r+1,c-1), (r, c+1), (r, c-1), (r-1, c+1), (r-1, c), (r-1, c-1)]

def left(dir):
    return {(0,1)  : (-1,0),
            (-1,0) : (0,-1),
            (0,-1) : (1,0),
            (1,0)  : (0,1)}[dir]

def add(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])
            

if __name__ == "__main__":
    sys.exit(main())