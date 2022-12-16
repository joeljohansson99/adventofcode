import sys
import operator

def main():

    input = dict()
    with open('input/day15.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","").replace("Sensor at ", "").replace(": closest beacon is at ", " ").replace(",", "").replace("x=", "").replace("y=", "")
            [sx,sy,bx,by] = l.split(" ")
            input[(int(sx),int(sy))] = (int(bx),int(by))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    dist = dict()
    for ((sx,sy),(bx,by)) in input.items():
        dist[(sx,sy)] = abs(sx - bx) + abs(sy-by)

    blocked = set()
    row = 2000000
    beacons = set([x for (x,y) in input.values() if y == row])
    for ((sx,sy), d) in dist.items():
        steps = d
        steps -= abs(row - sy)
        if steps > 0:
            for i in range(0,2*steps+1):
                if sx-steps+i not in beacons:
                    blocked.add(sx-steps+i)
        
    return len(blocked)

def part2(input):
    dist = dict()
    for ((sx,sy),(bx,by)) in input.items():
        dist[(sx,sy)] = abs(sx - bx) + abs(sy-by)

    outer_points = dict()
    for ((sx,sy),d) in dist.items():

        outer_points[(sx,sy)] = set()
        start = (sx-d-1,sy)
        (x,y) = start
        dir = (1, -1)

        while True:
            if x >= 0 and x <= 4000000 and y >= 0 and y <= 4000000:
                outer_points[(sx,sy)].add((x,y))

            (x,y) = tuple(map(operator.add, (x,y), dir))

            if (x,y) == start:
                break

            if x == sx:
                dir = tuple(map(operator.mul, (1,-1), dir))
            elif y == sy:
                dir = tuple(map(operator.mul, (-1,1), dir))

    for (p,points) in outer_points.items():
        for (x,y) in points:
            possible = True
            for ((sx,sy),d) in dist.items():
                if p == (sx,sy):
                    continue
                if abs(x - sx) + abs(y-sy) <= d:
                    possible = False
                    break
            if possible:
                return x*4000000 + y
    
    return 0

if __name__ == "__main__":
    sys.exit(main())