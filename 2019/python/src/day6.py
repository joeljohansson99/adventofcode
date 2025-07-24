import os
import sys
import networkx as nx

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    G = nx.DiGraph()
    for line in input:
        [A, B] = line.split(")")
        if not G.has_node(A):
            G.add_node(A)
        if not G.has_node(B):
            G.add_node(B)

        G.add_edge(A, B)

    count = 0
    for U in G.nodes():
        count += len(list(nx.ancestors(G, U)))
    return count

def part2(input):
    G = nx.Graph()
    for line in input:
        [A, B] = line.split(")")
        if not G.has_node(A):
            G.add_node(A)
        if not G.has_node(B):
            G.add_node(B)

        G.add_edge(A, B)

    return len(nx.shortest_path(G, "YOU", "SAN")) - 3

if __name__ == "__main__":
    sys.exit(main())