import os
import sys
import re

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day17.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    clay = set()
    for line in input:
        cords = line.split(", ")
        if "x" in cords[0]:
            xs = list(map(int, re.findall(r'\d+', cords[0])))
            if len(xs) == 1:
                xs.append(xs[0])
            ys = list(map(int, re.findall(r'\d+', cords[1])))
            if len(ys) == 1:
                ys.append(ys[0])
        else:
            ys = list(map(int, re.findall(r'\d+', cords[0])))
            if len(ys) == 1:
                ys.append(ys[0])
            xs = list(map(int, re.findall(r'\d+', cords[1])))
            if len(xs) == 1:
                xs.append(xs[0])

        for x in range(xs[0],xs[1]+1):
            for y in range(ys[0],ys[1]+1):
                clay.add((x,y))
    
    max_y = max([y for (_,y) in clay])
    min_y = min([y for (_,y) in clay])
    start = (500,0)
    sources = set()
    water = set()
    visited = set()

    sources.add(start)
    visited.add(start)
    while len(sources) > 0:
        next = set()
        for (x,y) in sources:
            oob = False
            while (x,y) not in water and (x,y) not in clay:
                if y > max_y:
                    oob = True
                    break
                water.add((x,y))
                y+=1
            
            if oob:
                continue
            
            if (x,y) not in water:
                y-=1
            done = False
            while not done:
                for dir in [1,-1]:
                    dx = 0
                    while True:
                        df = dx*dir
                        if (x+df, y) in clay:
                            break
                        if (x+df, y+1) not in clay and (x+df, y+1) not in water: 
                            if (x+df, y) not in visited:
                                if (x+df-1*dir, y) not in visited:
                                    next.add((x+df, y))
                                    visited.add((x+df, y))
                            done = True
                            break
                        water.add((x+df, y))
                        dx += 1
                y-=1
        sources = next

    return len(water) - len([p for p in water if p[1] < min_y])

def part2(input):
    clay = set()
    for line in input:
        cords = line.split(", ")
        if "x" in cords[0]:
            xs = list(map(int, re.findall(r'\d+', cords[0])))
            if len(xs) == 1:
                xs.append(xs[0])
            ys = list(map(int, re.findall(r'\d+', cords[1])))
            if len(ys) == 1:
                ys.append(ys[0])
        else:
            ys = list(map(int, re.findall(r'\d+', cords[0])))
            if len(ys) == 1:
                ys.append(ys[0])
            xs = list(map(int, re.findall(r'\d+', cords[1])))
            if len(xs) == 1:
                xs.append(xs[0])

        for x in range(xs[0],xs[1]+1):
            for y in range(ys[0],ys[1]+1):
                clay.add((x,y))
    
    max_y = max([y for (_,y) in clay])
    start = (500,0)
    sources = set()
    water = set()
    visited = set()

    sources.add(start)
    visited.add(start)
    while len(sources) > 0:
        next = set()
        for (x,y) in sources:
            oob = False
            while (x,y) not in water and (x,y) not in clay:
                if y > max_y:
                    oob = True
                    break
                water.add((x,y))
                y+=1
            
            if oob:
                continue
            
            if (x,y) not in water:
                y-=1
            done = False
            while not done:
                for dir in [1,-1]:
                    dx = 0
                    while True:
                        df = dx*dir
                        if (x+df, y) in clay:
                            break
                        if (x+df, y+1) not in clay and (x+df, y+1) not in water: 
                            if (x+df, y) not in visited:
                                if (x+df-1*dir, y) not in visited:
                                    next.add((x+df, y))
                                    visited.add((x+df, y))
                            done = True
                            break
                        water.add((x+df, y))
                        dx += 1
                y-=1
        sources = next

    count = 0
    for (x,y) in water:
        still = True
        for dir in [1,-1]:
            dx = 0
            while True:
                df = dx*dir
                if (x+df, y) in clay:
                    break
                elif (x+df, y) not in water:
                    still = False
                    break
                dx += 1
        if still:
            count += 1

    return count

if __name__ == "__main__":
    sys.exit(main())