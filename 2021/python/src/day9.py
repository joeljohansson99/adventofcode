import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day9.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    cave = [[int(c) for c in line] for line in input]
    risk = 0
    for r in range(len(cave)):
        for c in range(len(cave[0])):
            for (nr, nc) in aoc.neighbours(r,c):
                if 0 <= nr < len(cave) and 0 <= nc < len(cave[0]):
                    if cave[nr][nc] <= cave[r][c]:
                        break
            else:
                risk += cave[r][c]+1
    return risk

def part2(input):
    cave = [[int(c) for c in line] for line in input]
    starts = []
    for r in range(len(cave)):
        for c in range(len(cave[0])):
            for (nr, nc) in aoc.neighbours(r,c):
                if 0 <= nr < len(cave) and 0 <= nc < len(cave[0]):
                    if cave[nr][nc] <= cave[r][c]:
                        break
            else:
                starts.append((r,c))
    
    basins = set()
    for (r,c) in starts:
        pass



if __name__ == "__main__":
    sys.exit(main())