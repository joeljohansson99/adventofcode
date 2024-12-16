import os
import sys
import re
import time

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day8.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    freqs = dict()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] != ".":
                if input[r][c] not in freqs:
                    freqs[input[r][c]] = set()
                freqs[input[r][c]].add((r,c))
    
    anti = set()
    for (f, cords) in freqs.items():
        cords = sorted(cords)
        for i in range(len(cords)):
            for j in range(i+1, len(cords)):
                (r1,c1) = cords[i]
                (r2,c2) = cords[j]
                (dr,dc) = (r2-r1, c2-c1)
                
                (ar1, ac1) = ((r1-dr), (c1-dc))
                (ar2, ac2) = ((r2+dr), (c2+dc))

                if 0 <= ar1 < len(input) and 0 <= ac1 < len(input[0]):
                    anti.add((ar1,ac1))
                if 0 <= ar2 < len(input) and 0 <= ac2 < len(input[0]):
                    anti.add((ar2,ac2))
    
    return len(anti)


def part2(input):
    freqs = dict()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] != ".":
                if input[r][c] not in freqs:
                    freqs[input[r][c]] = set()
                freqs[input[r][c]].add((r,c))
    
    anti = set()
    for (f, cords) in freqs.items():
        cords = sorted(cords)
        for i in range(len(cords)):
            for j in range(i+1, len(cords)):
                (r1,c1) = cords[i]
                (r2,c2) = cords[j]
                (dr,dc) = (r2-r1, c2-c1)
                
                (ar1, ac1) = (r1, c1)
                k = 1
                while 0 <= ar1 < len(input) and 0 <= ac1 < len(input[0]):
                    anti.add((ar1,ac1))
                    (ar1, ac1) = ((r1-k*dr), (c1-k*dc))
                    k+=1

                (ar2, ac2) = (r2, c2)
                k = 1
                while 0 <= ar2 < len(input) and 0 <= ac2 < len(input[0]):
                    anti.add((ar2,ac2))
                    (ar2, ac2) = ((r2+k*dr), (c2+k*dc))
                    k+=1

    return len(anti)

if __name__ == "__main__":
    sys.exit(main())
