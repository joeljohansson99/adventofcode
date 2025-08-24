from itertools import permutations
import os
import sys
import utils.aoc as aoc
import networkx as nx

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day13.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    G = nx.DiGraph()
    for line in input:
        info = line[:-1].split()
        (a,b) = (info[0], info[-1])
        if info[2] == "gain":
            happy = int(info[3])
        else:
            happy = -int(info[3])
        G.add_edge(a,b,weight=happy)
    
    nodes = list(G.nodes)
    best = 0
    for perm in permutations(nodes):
        order = list(perm)
        order.append(perm[0])
        happiness = sum(G[order[i]][order[i+1]]["weight"] + G[order[i+1]][order[i]]["weight"] for i in range(len(order)-1))
        if best < happiness:
            best = happiness

    return best

def part2(input):
    G = nx.DiGraph()
    for line in input:
        info = line[:-1].split()
        (a,b) = (info[0], info[-1])
        if info[2] == "gain":
            happy = int(info[3])
        else:
            happy = -int(info[3])
        G.add_edge(a,b,weight=happy)
    for n in list(G.nodes):
        G.add_edge("Me", n, weight=0)
        G.add_edge(n, "Me", weight=0)
    
    nodes = list(G.nodes)
    best = 0
    for perm in permutations(nodes):
        order = list(perm)
        order.append(perm[0])
        happiness = sum(G[order[i]][order[i+1]]["weight"] + G[order[i+1]][order[i]]["weight"] for i in range(len(order)-1))
        if best < happiness:
            best = happiness

    return best

if __name__ == "__main__":
    sys.exit(main())
