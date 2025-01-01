import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day13.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    layers = dict()
    for line in input:
        [d, r] = list(map(int, re.findall(r'\d+', line)))
        layers[d] = r

    severity = 0
    for sec in range(max(layers.keys())+1):
        if sec in layers:
            if sec % ((layers[sec]-1)*2) == 0:
                severity += sec * layers[sec]

    return severity
                

def part2(input):
    layers = dict()
    for line in input:
        [d, r] = list(map(int, re.findall(r'\d+', line)))
        layers[d] = r

    start = 0
    while True:
        for sec in range(max(layers.keys())+1):
            if sec in layers:
                if (start+sec) % ((layers[sec]-1)*2) == 0:
                    break
        else:
            return start
        start += 1

if __name__ == "__main__":
    sys.exit(main())