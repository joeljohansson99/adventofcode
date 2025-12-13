from collections import defaultdict
import heapq
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day15.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    N = len(input)
    G = dict()
    for r in range(N):
        for c in range(N):
            G[(r,c)] = int(input[r][c])

    return dijkstra(G, (0,0), (N-1, N-1))

def part2(input):
    N = len(input)
    G = dict()
    for r in range(N*5):
        for c in range(N*5):
            base = int(input[r % N][c % N])
            inc = r // N + c // N
            G[(r, c)] = (base + inc - 1) % 9 + 1

    return dijkstra(G, (0,0), (N*5-1, N*5-1))

def dijkstra(G, start, end):
    dists = defaultdict(lambda: float('inf'))
    dists[start] = 0
    Q = [(0, start)]
    
    while Q:
        cur_dist, u = heapq.heappop(Q)

        if u == end:
            break
        for v in aoc.neighbours(u[0], u[1]):
            if v in G:
                new_dist = cur_dist + G[v]
                if new_dist < dists[v]:
                    dists[v] = new_dist
                    heapq.heappush(Q, (new_dist, v))
    
    return dists[end]


if __name__ == "__main__":
    sys.exit(main())