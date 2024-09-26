import os
import re
import sys

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day8.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    tree = list(map(int, re.findall(r'\d+', input[0])))

    (_, sum) = parse(tree, 0)
    return sum

def parse(tree, start):
    children = tree[start]
    metadata = tree[start+1]

    sum = 0
    next = start+2
    for _ in range(0,children):
        (n, metasum) = parse(tree, next)
        sum += metasum
        next = n
    
    for _ in range(0,metadata):
        sum += tree[next]
        next += 1

    return (next, sum)

def part2(input):
    tree = list(map(int, re.findall(r'\d+', input[0])))

    (_, sum) = parse2(tree, 0)
    return sum

def parse2(tree, start):
    children = tree[start]
    metadata = tree[start+1]

    next = start+2
    child_sums = list()
    for i in range(0,children):
        (n, metasum) = parse2(tree, next)
        child_sums.append(metasum)
        next = n
    
    sum = 0
    if children == 0:
        for _ in range(0,metadata):
            sum += tree[next]
            next += 1
    else:
        for _ in range(0,metadata):
            sum += 0 if tree[next] > children or tree[next] < 0 else child_sums[tree[next]-1]
            next += 1

    return (next,sum)

if __name__ == "__main__":
    sys.exit(main())