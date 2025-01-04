import os
import sys

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day22.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    infected = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "#":
                infected.add((r,c))
    
    loc = (len(input)//2, len(input[0])//2)
    dir = UP

    count = 0
    for _ in range(10000):
        if loc in infected:
            dir = right(dir)
            infected.remove(loc)
        else:
            dir = left(dir)
            infected.add(loc)
            count += 1
        loc = (loc[0]+dir[0], loc[1]+dir[1])
    
    return count

def part2(input):
    infected = set()
    weaken = set()
    flagged = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "#":
                infected.add((r,c))
    
    loc = (len(input)//2, len(input[0])//2)
    dir = UP

    count = 0
    for _ in range(10000000):
        if loc in infected:
            dir = right(dir)
            infected.remove(loc)
            flagged.add(loc)
        elif loc in weaken:
            weaken.remove(loc)
            infected.add(loc)
            count += 1
        elif loc in flagged:
            dir = (-dir[0], -dir[1])
            flagged.remove(loc)
        else:
            dir = left(dir)
            weaken.add(loc)
        loc = (loc[0]+dir[0], loc[1]+dir[1])
    
    return count

def left(dir):
    return {UP:LEFT,
        DOWN:RIGHT,
        LEFT:DOWN,
        RIGHT:UP}[dir]

def right(dir):
    return {UP:RIGHT,
        DOWN:LEFT,
        LEFT:UP,
        RIGHT:DOWN}[dir]

if __name__ == "__main__":
    sys.exit(main())