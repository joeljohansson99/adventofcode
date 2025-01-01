import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    graph = dict()
    for line in input:
        [program, * connections] = list(map(int, re.findall(r'\d+', line)))
        graph[program] = connections

    group = {0}
    current = {0}

    while current:
        next = set()
        for c in current:
            for n in graph[c]:
                if n not in group:
                    next.add(n)
                    group.add(n)
        current = next
    
    return len(group)
            


def part2(input):
    graph = dict()
    for line in input:
        [program, * connections] = list(map(int, re.findall(r'\d+', line)))
        graph[program] = connections

    seen = set()
    groups = 0
    for start in graph.keys():
        if start in seen:
            continue
        groups += 1
        seen.add(start)
        current = {start}
        while current:
            next = set()
            for c in current:
                for n in graph[c]:
                    if n not in seen:
                        next.add(n)
                        seen.add(n)
            current = next
        
    return groups

if __name__ == "__main__":
    sys.exit(main())