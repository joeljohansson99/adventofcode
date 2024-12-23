import os
import sys
import re
import networkx as nx

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day23.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    G = nx.Graph()
    edges = []
    nodes = set()
    for line in input:
        [u, v] = line.split("-")
        edges.append((u,v))
        nodes.add(u)
        nodes.add(v)
    
    
    for n in nodes:
        G.add_node(n)

    for e in edges:
        G.add_edge(e[0],e[1])
    
    count = 0
    for clique in list(nx.enumerate_all_cliques(G)):
        if len(clique) == 3:
            if any([n[0] == "t" for n in clique]):
                count += 1

    return count 

def part2(input):
    G = nx.Graph()
    edges = []
    nodes = set()
    for line in input:
        [u, v] = line.split("-")
        edges.append((u,v))
        nodes.add(u)
        nodes.add(v)
    
    
    for n in nodes:
        G.add_node(n)

    for e in edges:
        G.add_edge(e[0],e[1])
    
    best = 0
    for clique in list(nx.enumerate_all_cliques(G)):
        if len(clique) > best:
            best = len(clique)
            code = sorted(clique)

    return ",".join(code) 

if __name__ == "__main__":
    sys.exit(main())