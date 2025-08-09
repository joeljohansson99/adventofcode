import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    cols = len(input[0])
    correct = ""
    for c in range(cols):
        col = [input[r][c] for r in range(len(input))]
        correct += max(col,key=col.count)
    return correct

def part2(input):
    cols = len(input[0])
    correct = ""
    for c in range(cols):
        col = [input[r][c] for r in range(len(input))]
        correct += min(col,key=col.count)
    return correct

if __name__ == "__main__":
    sys.exit(main())
