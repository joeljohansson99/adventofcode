from collections import defaultdict
import os
from queue import LifoQueue, Queue
import sys
import threading

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day24.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    connections = set()
    for line in input:
        [c1,c2] = line.split("/")
        connections.add((int(c1), int(c2)))
    connections = sorted(connections, key=lambda x: max(x[0], x[1]))
    
    return build([(0,0)], 1, connections)

def part2(input):
    connections = set()
    for line in input:
        [c1,c2] = line.split("/")
        connections.add((int(c1), int(c2)))
    connections = sorted(connections, key=lambda x: max(x[0], x[1]))
    
    return sum([c[0] + c[1] for c in build2([(0,0)], 1, connections)])

cache = dict()
def build(bridge, i, connections):
    key = (tuple(bridge), i)
    if key in cache:
        return cache[key]
    strengths = [sum([c1 + c2 for (c1,c2) in bridge])]
    (c1,c2) = bridge[-1]
    for (cc1,cc2) in connections:
        if (cc1,cc2) in bridge:
            continue
        if i == 1 and cc1 == c2:
            strengths.append(build(bridge + [(cc1,cc2)], 1, connections))
        if i == 1 and cc2 == c2:
            strengths.append(build(bridge + [(cc1,cc2)], 0, connections))
        if i == 0 and cc1 == c1:
            strengths.append(build(bridge + [(cc1,cc2)], 1, connections))
        if i == 0 and cc2 == c1:
            strengths.append(build(bridge + [(cc1,cc2)], 0, connections))
    cache[key] = max(strengths)
    return max(strengths)

cache2 = dict()
def build2(bridge, i, connections):
    key = (tuple(bridge), i)
    if key in cache2:
        return cache2[key]
    strengths = [bridge]
    (c1,c2) = bridge[-1]
    for (cc1,cc2) in connections:
        if (cc1,cc2) in bridge:
            continue
        if i == 1 and cc1 == c2:
            strengths.append(build2(bridge + [(cc1,cc2)], 1, connections))
        if i == 1 and cc2 == c2:
            strengths.append(build2(bridge + [(cc1,cc2)], 0, connections))
        if i == 0 and cc1 == c1:
            strengths.append(build2(bridge + [(cc1,cc2)], 1, connections))
        if i == 0 and cc2 == c1:
            strengths.append(build2(bridge + [(cc1,cc2)], 0, connections))
    cache2[key] = max(strengths , key = len)
    return max(strengths , key = len)

if __name__ == "__main__":
    sys.exit(main())