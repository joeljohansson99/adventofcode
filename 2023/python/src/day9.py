import os
import sys
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day9.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    for l in input:
        seq = [int(x) for x in l.split(" ")]
        sum += rec(seq)
    return sum

def rec(seq):
    
    if all([True if x == 0 else False for x in seq]):
        return 0
    
    next = []
    
    for i in range(0, len(seq)-1):
        next.append(seq[i+1] - seq[i])
        
    return seq[len(seq)-1] + rec(next)

def part2(input):
    sum = 0
    for l in input:
        seq = [int(x) for x in l.split(" ")]
        sum += rec2(seq)
    return sum

def rec2(seq):
    
    if all([True if x == 0 else False for x in seq]):
        return 0
    
    next = []
    
    for i in range(0, len(seq)-1):
        next.append(seq[i+1] - seq[i])
        
    return seq[0] - rec2(next)

if __name__ == "__main__":
    sys.exit(main())