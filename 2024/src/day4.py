import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day4.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for r in range(len(input)):
        for c in range(len(input[0])-3):
            word = input[r][c:c+4]
            if word == "XMAS" or word[::-1] == "XMAS":
                count += 1
    for c in range(len(input[0])):
        for r in range(len(input)-3):
            word = input[r][c] +input[r+1][c] +input[r+2][c]+input[r+3][c]
            if word == "XMAS" or word[::-1] == "XMAS":
                count += 1
    
    for c in range(len(input[0])-3):
        for r in range(len(input)-3):
            word = input[r][c] + input[r+1][c+1] + input[r+2][c+2] + input[r+3][c+3]
            if word == "XMAS" or word[::-1] == "XMAS":
                count += 1

    for c in range(3, len(input[0])):
        for r in range(len(input)-3):
            word = input[r][c] + input[r+1][c-1] + input[r+2][c-2] + input[r+3][c-3]
            if word == "XMAS" or word[::-1] == "XMAS":
                count += 1
    
    return count

def part2(input):
    count = dict()
    
    for c in range(len(input[0])-2):
        for r in range(len(input)-2):
            word = input[r][c] + input[r+1][c+1] + input[r+2][c+2]
            if word == "MAS" or word[::-1] == "MAS":
                if (r+1,c+1) not in count:
                    count[(r+1,c+1)] = 1
                else:
                    count[(r+1,c+1)] += 1

    for c in range(2, len(input[0])):
        for r in range(len(input)-2):
            word = input[r][c] + input[r+1][c-1] + input[r+2][c-2]
            if word == "MAS" or word[::-1] == "MAS":
                if (r+1,c-1) not in count:
                    count[(r+1,c-1)] = 1
                else:
                    count[(r+1,c-1)] += 1

    return len([(k,v) for (k,v) in count.items() if v == 2])

if __name__ == "__main__":
    sys.exit(main())