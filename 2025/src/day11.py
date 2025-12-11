from collections import defaultdict, deque
import os
import sys
import utils.aoc as aoc
import networkx as nx

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    G = nx.DiGraph()
    for line in input:
        u,vs = line.split(":")
        for v in vs.split(" "): 
            G.add_edge(u,v)
    
    return countPaths(G, "you", "out")

def part2(input):
    G = nx.DiGraph()
    for line in input:
        u,vs = line.split(":")
        for v in vs.split(" "): 
            if v != "":
                G.add_edge(u,v)

    svr_fft_dac_out = countPaths(G, "svr", "fft") * countPaths(G, "fft", "dac") * countPaths(G, "dac", "out")
    svr_dac_fft_out = countPaths(G, "svr", "dac") * countPaths(G, "dac", "fft") * countPaths(G, "fft", "out")
    return svr_fft_dac_out+svr_dac_fft_out

def countPaths(G, start, end):
    topo = nx.topological_sort(G)

    ways = defaultdict(int)
    ways[start] = 1

    for u in topo:
        for v in G[u].keys():
            ways[v] += ways[u]

    return ways[end]

if __name__ == "__main__":
    sys.exit(main())