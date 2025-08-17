import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day22.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    nodes = dict()
    for line in input[2:]:
        [x,y,size,used,avail,use] = aoc.ints(line)
        nodes[(x,y)] = (size,used,avail,use)

    viable = 0
    for (a, (_,a_used,_,_)) in nodes.items():
        for (b, (_,_,b_avail,_)) in nodes.items():
            if a != b and a_used != 0 and a_used <= b_avail:
                viable += 1
    return viable

def part2(input):
    nodes = dict()
    for line in input[2:]:
        [x,y,size,used,avail,use] = aoc.ints(line)
        nodes[(x,y)] = (size,used,avail,use)
        if used == 0:
            empty = (x,y)
    
    X = max([x for (x,_) in nodes.keys()])

    open = set()
    for (a, (_,a_used,_,_)) in nodes.items():
        viable = 0
        for (b, (_,_,b_avail,_)) in nodes.items():
            if a != b and a_used != 0 and a_used <= b_avail:
                viable += 1
        if viable != 0:
            open.add(a)
    
    steps = bfs(empty, (X,0), open)
    steps += 5*(X-1)
    return steps

def bfs(start, end, open):
    current = [start]
    seen = {start}
    steps = 1
    while current:
        next = []
        for c in current:
            for n in aoc.neighbours(c[0], c[1]):
                if n == end:
                    return steps
                if n not in seen and n in open:
                    next.append(n)
                    seen.add(n)
        current = next
        steps += 1

if __name__ == "__main__":
    sys.exit(main())
