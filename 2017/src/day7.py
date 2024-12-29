import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    nodes = set()
    edges = dict()
    for line in input:
        node = line.split(" ")[0]
        nodes.add(node)

        childs = line.split(" -> ")
        if len(childs) > 1:
            childs = childs[1].split(", ")
            edges[node] = set(childs)
    
    for node in nodes:
        for childs in edges.values():
            if node in childs:
                break
        else:
            return node

def part2(input):
    nodes = dict()
    weights = dict()
    edges = dict()
    for line in input:
        node = line.split(" ")[0]
        w = re.search(r'\d+', line).group()
        nodes[node] = int(w)
        weights[node] = int(w)

        childs = line.split(" -> ")
        if len(childs) > 1:
            childs = childs[1].split(", ")
            edges[node] = set(childs)

    for node in nodes:
        for childs in edges.values():
            if node in childs:
                break
        else:
            top = node
            break
    
    update_weight(top, weights, edges)
    return check_weight(top, nodes, weights, edges)

def update_weight(node, weights, edges):
    if node not in edges:
        return weights[node]
    
    for child in edges[node]:
        update_weight(child, weights, edges)
        weights[node] += weights[child]

def check_weight(node, nodes, weights, edges):
    if node not in edges:
        return 0

    children = edges[node]
    for child in children:
        res = check_weight(child, nodes, weights, edges)
        if res != 0:
            return res
    ws = [weights[n] for n in children]
    if len(set(ws)) == 1:
        return 0
    else:
        [a,b] = list(set(ws))
        if ws.count(a) == 1:
            err = b - a
            nerr = a
        else:
            err = a - b
            nerr = b
        for child in children:
            if weights[child] == nerr:
                return nodes[child] + err
    
    return "error"

if __name__ == "__main__":
    sys.exit(main())