import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day8.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

X = 50
Y = 6

def part1(input):
    screen = list()
    for line in input:
        [a,b] = aoc.ints(line)
        if "rect" in line:
            rect(screen, a, b)
        if "rotate column" in line:
            rot_col(screen, a, b)
        if "rotate row" in line:
            rot_row(screen, a, b)
    
    pixels = 0
    for x in range(50):
        for y in range(6):  
            if [x,y] in screen:
                pixels += 1
    
    return pixels

def part2(input):
    screen = list()
    for line in input:
        [a,b] = aoc.ints(line)
        if "rect" in line:
            rect(screen, a, b)
        if "rotate column" in line:
            rot_col(screen, a, b)
        if "rotate row" in line:
            rot_row(screen, a, b)
    
    for y in range(6):  
        for x in range(50):
            if [x,y] in screen:
                print("#", end="")
            else:
                print(" ", end="")
        print("")

def rect(screen, a, b):
    for y in range(b):
        for x in range(a):
            if [x,y] not in screen:
                screen.append([x,y])

def rot_col(screen, col, steps):
    for i in range(len(screen)):
        if screen[i][0] == col:
            screen[i][1] = (screen[i][1] + steps) % Y

def rot_row(screen, row, steps):
    for i in range(len(screen)):
        if screen[i][1] == row:
            screen[i][0] = (screen[i][0] + steps) % X

if __name__ == "__main__":
    sys.exit(main())
