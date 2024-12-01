import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day1.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    left = []
    right = []
    for line in input:
        [l, r] = list(map(int, re.findall(r'\d+', line)))
        left.append(l)
        right.append(r)
    
    left.sort()
    right.sort()
    
    dist = 0
    for i in range(len(left)):
        d = abs(left[i] - right[i])
        dist += d
    
    return dist


def part2(input):
    left = []
    right = []
    for line in input:
        [l, r] = list(map(int, re.findall(r'\d+', line)))
        left.append(l)
        right.append(r)
    
    left.sort()
    right.sort()
    
    count = 0
    for i in range(len(left)):
        c = left[i] * right.count(left[i])
        count += c
    
    return count

if __name__ == "__main__":
    sys.exit(main())