import os
import sys

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    next = dict()
    pre = dict()
    for line in input:
        [u, v] = filter(lambda x: len(x) == 1, line.split(" "))
        if u not in next:
            next[u] = set()
        next[u].add(v)
        if v not in pre:
            pre[v] = set()
        pre[v].add(u)
    
    for n in next.keys():
        if n not in pre:
            pre[n] = set()

    for n in pre.keys():
        if n not in next:
            next[n] = set()
    
    iter = sorted([n for n in next.keys()])

    order = ""

    while len(iter) > 0:
        for u in iter:
            if len(pre[u]) == 0:
                for v in next[u]:
                    pre[v].remove(u)
                iter.remove(u)
                order += u
                break

    return order

def part2(input):
    next = dict()
    pre = dict()
    for line in input:
        [u, v] = filter(lambda x: len(x) == 1, line.split(" "))
        if u not in next:
            next[u] = set()
        next[u].add(v)
        if v not in pre:
            pre[v] = set()
        pre[v].add(u)
    
    for n in next.keys():
        if n not in pre:
            pre[n] = set()

    for n in pre.keys():
        if n not in next:
            next[n] = set()
    
    iter = sorted([n for n in next.keys()])

    order = ""

    sec = -1
    working = dict()
    workers = 5

    while len(iter) > 0:
        sec+=1
        for u in list(working):
            if working[u] <= sec:
                for v in next[u]:
                    pre[v].remove(u)
                iter.remove(u)
                del working[u]
                order += u
                workers += 1
        
        for u in iter:
            if len(pre[u]) == 0 and u not in working and workers > 0:
                working[u] = sec + ord(u) - 4
                workers -= 1
                if workers == 0:
                    break

    return sec


if __name__ == "__main__":
    sys.exit(main())