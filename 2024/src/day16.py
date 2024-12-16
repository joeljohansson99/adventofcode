import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day16.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    walls = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "S":
                src = (r,c)
            if input[r][c] == "E":
                dst = (r,c)
            if input[r][c] == "#":
                walls.add((r,c))

    return dijsktra(src, dst, walls, dict())

def part2(input):
    walls = set()
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "S":
                src = (r,c)
            if input[r][c] == "E":
                dst = (r,c)
            if input[r][c] == "#":
                walls.add((r,c))

    prev = dict()
    dijsktra(src, dst, walls, prev)

    current = set()
    current.add((dst, (-1,0)))
    path = set()
    path.add((dst, (-1,0)))

    while current:
        next = set()
        for c in current:
            for n in prev[c]:
                if n not in path:
                    path.add(n)
                    next.add(n)
        if (src, (0,1)) in next:
            break
        current = next

    return len(set([p[0] for p in path]))
                


def dijsktra(src, dst, walls, prev):
    dist = dict()
    start = (src, (0,1))
    dist[start] = 0
    Q = []
    Q.append(start)
    seen = set()

    while Q:
        (r,c), dir = Q.pop()
        d = dist[((r,c),dir)]
        for (dr,dc) in dirs(dir):
            (nr,nc) = (r+dr,c+dc)

            if (nr,nc) in walls:
                continue

            if not forward(dir, (dr,dc)):
                nd = 1001 + d
            else:
                nd = 1 + d

            if (nr,nc) == dst:
                prev[(dst, (dr,dc))] = []
                prev[(dst, (dr,dc))].append(((r,c),dir))
                return d + 1
            
            seen.add((nr,nc))
            next = ((nr,nc), (dr,dc))
            if next in dist:
                if dist[next] > nd:
                    prev[next] = []
                if dist[next] >= nd:
                    prev[next].append(((r,c),dir))
                dist[next] = min(dist[next], nd)

            else:
                prev[next] = []
                prev[next].append(((r,c),dir))
                dist[next] = nd
                Q.append(next)
                Q = sorted(Q, key=lambda n : dist[n], reverse=True)

def dirs(dir):
    return [dir, dir[::-1], (-dir[::-1][0], -dir[::-1][1])]

def forward(dir, delta):
    return dir[0] == delta[0] and dir[1] == delta[1]

if __name__ == "__main__":
    sys.exit(main())