import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    pc = 0
    step = 0
    maze = [int(offset) for offset in input]
    while 0 <= pc < len(maze):
        jump = maze[pc]
        maze[pc] += 1
        pc += jump 
        step += 1
    return step

def part2(input):
    pc = 0
    step = 0
    maze = [int(offset) for offset in input]
    while 0 <= pc < len(maze):
        jump = maze[pc]
        if maze[pc] >= 3:
            maze[pc] -= 1
        else:
            maze[pc] += 1
        pc += jump 
        step += 1
    return step

if __name__ == "__main__":
    sys.exit(main())