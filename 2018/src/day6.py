import os
import sys
import re

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    ys = set()
    xs = set()
    groups = dict()
    current = dict()
    visited = set()
    for i in range(0, len(input)):
        [x, y] = list(map(int, re.findall(r'\d+', input[i])))
        groups[i] = {(x,y)}
        current[i] = {(x,y)}
        visited.add((x,y))
        ys.add(y)
        xs.add(x)

    (sx,ex) = (min(xs), max(xs))
    (sy,ey) = (min(ys), max(ys))
    out = set()
    next = dict()
    while any([len(current[i]) > 0 for i in range(0,len(current))]):
        for i in range(0, len(groups)):
            next[i] = set()
            for (x,y) in current[i]:
                for (dx, dy) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if dx < sx or dx > ex or dy < sy or dy > ey:
                        out.add(i)
                        continue
                    if (dx,dy) not in visited:
                        next[i].add((dx,dy))
                        visited.add((dx,dy))
                    else:
                        for j in range(0, i):
                            if (dx,dy) in next[j]:
                                next[j].remove((dx,dy))
        
        for i in range(0, len(groups)):
            groups[i] |= next[i]
            current[i] = next[i]
                    
    return max(len(groups[i]) for i in range(0, len(input)) if i not in out)

def part2(input):
    dist = 10000
    cords = set()
    for i in range(0, len(input)):
        [x, y] = list(map(int, re.findall(r'\d+', input[i])))
        cords.add((x,y))

    (sx,ex) = (min([x for (x,_) in cords]), max([x for (x,_) in cords]))
    (sy,ey) = (min([y for (_,y) in cords]), max([y for (_,y) in cords]))

    dx = 0
    dy = 0
    for (x,y) in cords:
        dx += abs(sx - x)
        dy += abs(sy - y)
    
    (sx, ex) = (sx-(dist-dx), ex+(dist-dx))
    (sy, ey) = (sy-(dist-dy), ey+(dist-dy))
    
    count = 0
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            d = 0
            count += 1
            for (cx, cy) in cords:
                d += (abs(y-cy) + abs(x-cx))
                if d >= dist:
                    count -= 1
                    break
            
    return count

if __name__ == "__main__":
    sys.exit(main())