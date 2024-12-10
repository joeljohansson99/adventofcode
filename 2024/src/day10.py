import os
import sys
import re
import time

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    heads = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "0":
                heads.add((r,c))

    score = 0
    for head in heads:
        score += bfs(input, head)

    return score

def part2(input):
    heads = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "0":
                heads.add((r,c))

    score = 0
    for head in heads:
        score += dfs(input, head)

    return score

def bfs(input, start):
    visited = set()
    current = set()
    current.add(start)
    visited.add(start)
    score = 0
    while current:
        next = set()
        for (r, c) in current:
            for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= dr < len(input) and 0 <= dc < len(input[0]) and (dr,dc) not in visited:
                    if int(input[dr][dc]) == (int(input[r][c]) + 1):
                        if input[dr][dc] == "9":
                            score += 1
                        else:
                            next.add((dr,dc))
                        visited.add((dr,dc))
        current = next
    return score

def dfs(input, c):
    (r,c) = c
    score = 0
    for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if 0 <= dr < len(input) and 0 <= dc < len(input[0]):
            if int(input[dr][dc]) == (int(input[r][c]) + 1):
                if input[dr][dc] == "9":
                    score+= 1
                else:
                    score += dfs(input, (dr,dc))
    
    return score

if __name__ == "__main__":
    sys.exit(main())