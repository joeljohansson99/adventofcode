from collections import defaultdict
import math
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day8.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    boxes = list()
    for line in input:
        (x,y,z) = aoc.ints(line)
        boxes.append((x,y,z))
    
    circuits = list()
    connections = defaultdict(set)
    pairs = list()
    for i in range(len(boxes)):
        (x1,y1,z1) = boxes[i]
        for j in range(i+1, len(boxes)):
            (x2,y2,z2) = boxes[j]
            dist = distance(x1, y1, z1, x2, y2, z2)
            pairs.append((dist, (i,j)))

    pairs = sorted(pairs, key=lambda x: x[0])

    for _ in range(1000):
        (_, (i,j)) = pairs.pop(0)
        connections[boxes[i]].add(boxes[j])
        connections[boxes[j]].add(boxes[i])
    
    seen = set()
    circuits = list()
    seen = set()
    for box in boxes:
        if box in seen:
            continue
        current = set()
        circuit = set()
        current.add(box)
        seen.add(box)
        circuit.add(box)
        while current:
            next = set()
            for u in current:
                for v in connections[u]:
                    if v not in seen:
                        next.add(v)
                        seen.add(v)
                        circuit.add(v)
            current = next
        circuits.append(circuit)
    
    circuits = sorted(circuits, key=lambda x: -len(x))

    return len(circuits[0])*len(circuits[1])*len(circuits[2])

def part2(input):
    boxes = list()
    for line in input:
        (x,y,z) = aoc.ints(line)
        boxes.append((x,y,z))
    
    connections = defaultdict(set)
    pairs = list()
    for i in range(len(boxes)):
        (x1,y1,z1) = boxes[i]
        for j in range(i+1, len(boxes)):
            (x2,y2,z2) = boxes[j]
            dist = distance(x1, y1, z1, x2, y2, z2)
            pairs.append((dist, (i,j)))

    pairs = sorted(pairs, key=lambda x: x[0])

    while True:
        (_, (i,j)) = pairs.pop(0)
        connections[boxes[i]].add(boxes[j])
        connections[boxes[j]].add(boxes[i])
    
        seen = set()
        seen = set()
        current = set()
        current.add(boxes[0])
        seen.add(boxes[0])
        while current:
            next = set()
            for u in current:
                for v in connections[u]:
                    if v not in seen:
                        next.add(v)
                        seen.add(v)
            current = next
        if len(seen) == len(boxes):
            return boxes[i][0]*boxes[j][0]

def distance(x1, y1, z1, x2, y2, z2):  
    d = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) +
                math.pow(z2 - z1, 2)* 1.0)
    return d

if __name__ == "__main__":
    sys.exit(main())