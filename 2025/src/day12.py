import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    presents = list()
    for i in range(len(input)):
        if len(input[i]) > 1 and input[i][0].isdigit() and input[i][1] == ":":
            present = set()
            for r in range(i+1, i+4):
                for c in range(len(input[r])):
                    if input[r][c] == "#":
                        present.add((r,c))
            presents.append(present)

    regions = list()
    for line in input:
        if len(line) > 3 and line[0].isdigit() and line[1].isdigit():
            x,y, *indexes = aoc.ints(line)
            regions.append((x,y, indexes))

    count = 0
    for (x,y, indexes) in regions:
        s = 0
        for i in range(len(indexes)):
            s += indexes[i] * len(presents[i])
        if x*y >= s:
            count+=1
    return count

def part2(input):
    pass

if __name__ == "__main__":
    sys.exit(main())