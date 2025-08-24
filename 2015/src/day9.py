import itertools
import os
import sys
import networkx as nx

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day9.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    G = nx.Graph()
    for line in input:
        [a, _, b, _, d] = line.split()
        G.add_edge(a,b,weight=int(d))

    return min([shortest_hamiltonian_path(G, a) for a in G.nodes])
    
def part2(input):
    G = nx.Graph()
    for line in input:
        [a, _, b, _, d] = line.split()
        G.add_edge(a,b,weight=int(d))

    return max([longest_hamiltonian_path(G, a) for a in G.nodes])

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

def longest_hamiltonian_path(G, start):
    nodes = list(G.nodes)
    nodes.remove(start)

    best_length = 0

    for perm in itertools.permutations(nodes):
        path = [start] + list(perm)
        length = sum(G[path[i]][path[i+1]]["weight"] for i in range(len(path)-1))

        if length > best_length:
            best_length = length

    return best_length

if __name__ == "__main__":
    sys.exit(main())
