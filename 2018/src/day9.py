import os
import sys
import re
from collections import deque

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day9.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    [players, last] = list(map(int, re.findall(r'\d+', input[0])))
    points = dict()
    marbles = deque()
    marbles.append(0)

    for marble in range(1, last+1):
        if marble % 23 == 0:
            marbles.rotate(7)    
            player = marble % players
            points[player] = points[player] + marble if player in points else marble
            points[player] += marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)
            
    return max(points.values())

def part2(input):
    [players, last] = list(map(int, re.findall(r'\d+', input[0])))
    points = dict()
    marbles = deque()
    marbles.append(0)

    for marble in range(1, last*100+1):
        if marble % 23 == 0:
            marbles.rotate(7)    
            player = marble % players
            points[player] = points[player] + marble if player in points else marble
            points[player] += marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)

    return max(points.values())

if __name__ == "__main__":
    sys.exit(main())