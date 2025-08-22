import itertools
import os
import sys
import utils.aoc as aoc
import networkx as nx

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day24.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    robots = dict()
    open = set()
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != "#":
                if input[y][x].isdigit():
                    robots[input[y][x]] = ((x,y))
                open.add((x,y))
    G = nx.Graph()
    for a in robots.keys():
        for b in robots.keys():
            if a != b:
                G.add_edge(a, b, weight=bfs(robots[a], robots[b], open))
        
    return shortest_hamiltonian_path(G, "0")
    
def part2(input):
    robots = dict()
    open = set()
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != "#":
                if input[y][x].isdigit():
                    robots[input[y][x]] = ((x,y))
                open.add((x,y))
    G = nx.Graph()
    for a in robots.keys():
        for b in robots.keys():
            if a != b:
                G.add_edge(a, b, weight=bfs(robots[a], robots[b], open))
    
    return shortest_tsp_path(G, "0")

def shortest_hamiltonian_path(G, start):
    nodes = list(G.nodes)
    nodes.remove(start)

    best_length = float("inf")

    for perm in itertools.permutations(nodes):
        path = [start] + list(perm)
        length = sum(G[path[i]][path[i+1]]["weight"] for i in range(len(path)-1))

        if length < best_length:
            best_length = length

    return best_length

def shortest_tsp_path(G, start):
    nodes = list(G.nodes)
    nodes.remove(start)

    best_length = float("inf")

    for perm in itertools.permutations(nodes):
        path = [start] + list(perm) + [start]
        length = sum(G[path[i]][path[i+1]]["weight"] for i in range(len(path)-1))

        if length < best_length:
            best_length = length

    return best_length


def bfs(start, end, open):
    current = [start]
    seen = {start}
    steps = 1
    while current:
        next = []
        for c in current:
            for n in aoc.neighbours(c[0], c[1]):
                if n == end:
                    return steps
                if n not in seen and n in open:
                    next.append(n)
                    seen.add(n)
        current = next
        steps += 1

if __name__ == "__main__":
    sys.exit(main())
