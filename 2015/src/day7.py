from collections import defaultdict
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    N = 65535
    wires = dict()
    done = set()
    left = True
    while left:
        left = False
        for line in input:
            if line in done:
                continue
            left = True
            try:
                if "AND" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) & getVal(wires, y)
                elif "OR" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) | getVal(wires, y)
                elif "LSHIFT" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) << getVal(wires, y)
                elif "RSHIFT" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) >> getVal(wires, y)
                elif "NOT" in line:
                    [_, x, _, y] = line.split()
                    wires[y] = getVal(wires, x) ^ N
                else:
                    [x, _, y] = line.split()
                    wires[y] = getVal(wires, x)
                done.add(line)
            except Exception:
                pass

    return wires['a']

def part2(input):
    N = 65535
    wires = dict()
    done = set()
    left = True
    while left:
        left = False
        for line in input:
            if line in done:
                continue
            left = True
            try:
                if "AND" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) & getVal(wires, y)
                elif "OR" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) | getVal(wires, y)
                elif "LSHIFT" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) << getVal(wires, y)
                elif "RSHIFT" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) >> getVal(wires, y)
                elif "NOT" in line:
                    [_, x, _, y] = line.split()
                    wires[y] = getVal(wires, x) ^ N
                else:
                    [x, _, y] = line.split()
                    wires[y] = getVal(wires, x)
                done.add(line)
            except Exception:
                pass
    
    b = wires['a']
    wires = dict()

    N = 65535
    done = set()
    left = True
    while left:
        left = False
        for line in input:
            if line in done:
                continue
            left = True
            try:
                if "AND" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) & getVal(wires, y)
                elif "OR" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) | getVal(wires, y)
                elif "LSHIFT" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) << getVal(wires, y)
                elif "RSHIFT" in line:
                    [x, _, y, _, z] = line.split()
                    wires[z] = getVal(wires, x) >> getVal(wires, y)
                elif "NOT" in line:
                    [_, x, _, y] = line.split()
                    wires[y] = getVal(wires, x) ^ N
                else:
                    [x, _, y] = line.split()
                    if y == 'b':
                        wires[y] = b
                    else:
                        wires[y] = getVal(wires, x)
                done.add(line)
            except Exception:
                pass
    
    return wires['a']

def getVal(wires, x):
    if not x.isdigit() and x not in wires:
        raise Exception
    return int(x) if x.isdigit() else wires[x]

if __name__ == "__main__":
    sys.exit(main())
