import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day18.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    R = 71
    C = 71

    bytes = []
    for line in input:
        [x,y] = list(map(int, re.findall(r'\d+', line)))
        bytes.append((x,y))
    
    fallen = set()
    for (x,y) in bytes[:1024]:
        fallen.add((x,y))
    
    return bfs(R, C, fallen, (0,0))

def part2(input):
    R = 71
    C = 71

    bytes = []
    for line in input:
        [x,y] = list(map(int, re.findall(r'\d+', line)))
        bytes.append((x,y))
    
    cutoff = 1024
    while True:
        fallen = set()
        for (x,y) in bytes[:cutoff]:
            fallen.add((x,y))
        
        if bfs(R, C, fallen, (0,0)) == -1:
            return bytes[cutoff-1]
        cutoff += 1

def bfs(R, C, fallen, start):
    visited = set()
    current = set()
    current.add(start)
    visited.add(start)
    steps = 1
    while current:
        next = set()
        for (r, c) in current:
            for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= dr < R and 0 <= dc < C and (dr,dc) not in visited and (dr,dc) not in fallen:
                    if dr == R-1 and dc == C-1:
                        return steps
                    next.add((dr,dc))
                    visited.add((dr,dc))
        current = next
        steps += 1
    return -1

if __name__ == "__main__":
    sys.exit(main())