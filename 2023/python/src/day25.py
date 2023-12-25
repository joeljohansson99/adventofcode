import os
import sys
import networkx as nx
import matplotlib.pyplot as plt

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day25.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    G = nx.Graph()
    edges = set()
    nodes = set()
    for line in input:
        w1, values = line.split(":")
        values = [x for x in values.split(" ") if len(x) > 0]
        nodes.add(w1)
        for w2 in values:
            edges.add((w1,w2))
            nodes.add(w2)
   
    for n in nodes:
        G.add_node(n)

    for e in edges:
        G.add_edge(e[0],e[1])
   
    subwires = list(nx.k_edge_components(G, 4))

    return len(subwires[0]) * len(subwires[1])

def part2(input):
    pass

if __name__ == "__main__":
    sys.exit(main())