from collections import defaultdict
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    G = defaultdict(set)
    for line in input:
        [u,v] = line.split("-")
        G[u].add(v)
        G[v].add(u)
    return countPaths(G, "start", "end", set(), False)

def part2(input):
    G = defaultdict(set)
    for line in input:
        [u,v] = line.split("-")
        G[u].add(v)
        G[v].add(u)
    return countPaths(G, "start", "end", set(), True)

def countPaths(G, u, end, seen, wildcard):
    if u.islower():
        seen.add(u)
    if u == end:
        return 1
    
    paths = 0
    for v in G[u]:
        if v not in seen:
            paths += countPaths(G, v, end, seen.copy(), wildcard)
        elif wildcard and v != "start":
            paths += countPaths(G, v, end, seen.copy(), False)
    
    return paths

if __name__ == "__main__":
    sys.exit(main())