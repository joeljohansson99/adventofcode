import os
import sys
import utils.aoc as aoc
from shapely import Polygon

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day9.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    tiles = list()
    for line in input:
        x, y = aoc.ints(line)
        tiles.append((x,y))
    
    best = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            (x1,y1) = tiles[i]
            (x2,y2) = tiles[j]
            area = (abs(x2-x1)+1) * (abs(y2-y1)+1)
            if area > best:
                best = area
    return best

def part2(input):
    tiles = list()
    first = None
    for line in input:
        x, y = aoc.ints(line)
        if first is None:
            first = (x,y)
        tiles.append((x,y))
    polygon = Polygon(tiles)
    best = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            (x1,y1) = tiles[i]
            (x2,y2) = tiles[j]
            dy = abs(y2-y1)
            dx = abs(x2-x1)
            
            (x,y) = (min(x1,x2), min(y1,y2))
            other = Polygon([(x,y),(x+dx,y),(x+dx,y+dy),(x,y+dy)])
            if other.within(polygon):
                area = (dy+1) * (dx+1)
                if area > best:
                    best = area
    return best

if __name__ == "__main__":
    sys.exit(main())