from collections import defaultdict
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day3.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    house = (0,0)
    presents = {house}
    dirs = input[0]
    for dir in dirs:
        house = getNext(house, dir)
        presents.add(house)
    return len(presents)


def part2(input):
    houses = [(0,0),(0,0)]
    presents = {(0,0)}
    dirs = input[0]
    for i in range(len(dirs)):
        houses[i%2] = getNext(houses[i%2], dirs[i])
        presents.add(houses[i%2])
    return len(presents)

def getNext(house, dir):
    next = {
        "<": (-1,0),
        ">": (1,0),
        "^": (0,-1),
        "v": (0,1)
    }[dir]
    return (house[0]+next[0], house[1]+next[1])

if __name__ == "__main__":
    sys.exit(main())
