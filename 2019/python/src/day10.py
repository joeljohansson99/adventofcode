import os
import sys
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    asteroids = set()
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == '#':
                asteroids.add((x,y))
    
    max_count = 0
    for (x,y) in asteroids:
        count = 0
        blocked = set()
        for (dx,dy) in asteroids:
            if x == dx and y == dy:
                continue

            angle = math.degrees(math.atan2(-(y-dy), x-dx))
            if angle in blocked:
                continue
            
            blocked.add(angle)
            count += 1

        max_count = max(max_count, count)
    return max_count


def part2(input):
    asteroids = set()
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == '#':
                asteroids.add((x,y))
    
    station = None
    max_count = 0
    for (x,y) in asteroids:
        count = 0
        blocked = set()
        for (dx,dy) in asteroids:
            if x == dx and y == dy:
                continue

            angle = math.degrees(math.atan2(-(y-dy), x-dx))
            if angle in blocked:
                continue
            
            blocked.add(angle)
            count += 1

        if count > max_count:
            max_count = count 
            station = (x,y)

    (x,y) = station
    rots = dict()
    dist = dict()
    for (dx,dy) in asteroids:
        if x == dx and y == dy:
            continue
        
        angle = (math.degrees(math.atan2((dy-y), dx-x)) + 90) % 360
        
        if angle not in rots:
            rots[angle] = list()
        rots[angle].append((dx,dy))
        dist[(dx,dy)] = math.hypot(x-dx, y-dy)
    
    count = 0
    while count < 200:
        for angle in sorted(list(rots.keys())):
            if rots[angle]:
                closest = min(rots[angle], key=lambda p: dist[p])
                rots[angle].remove(closest)
                count += 1
                if count == 200:
                    return 100*closest[0] + closest[1]

if __name__ == "__main__":
    sys.exit(main())