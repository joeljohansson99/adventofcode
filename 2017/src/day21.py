import copy
from math import sqrt
import os
import sys

import numpy as np

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day21.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    rules = dict()
    for line in input:
        [arg, _, res] = line.split(" ")
        key = arg.split("/")
        val = res.split("/")
        key = np.array([[1 if key[j][i] == "#" else 0 for i in range(len(key))] for j in range(len(key))])
        val = np.array([[1 if val[j][i] == "#" else 0 for i in range(len(val))] for j in range(len(val))])
        rules[key.tobytes()] = val

    pattern = np.array([[0,1,0],[0,0,1],[1,1,1]])
    return transform(pattern, rules, 5)

def part2(input):
    rules = dict()
    for line in input:
        [arg, _, res] = line.split(" ")
        key = arg.split("/")
        val = res.split("/")
        key = np.array([[1 if key[j][i] == "#" else 0 for i in range(len(key))] for j in range(len(key))])
        val = np.array([[1 if val[j][i] == "#" else 0 for i in range(len(val))] for j in range(len(val))])
        rules[key.tobytes()] = val

    pattern = np.array([[0,1,0],[0,0,1],[1,1,1]])
    return transform(pattern, rules, 18)

def transform(pattern, rules, t):
    if t == 0:
        return np.sum(pattern)

    dim = 2 if len(pattern) % 2 == 0 else 3

    parts = []
    for sub in split(pattern, dim, dim):
        for key in get_keys(sub):
            if key.tobytes() in rules:
                break
        next = rules[key.tobytes()]
        parts.append(next)

    rows = []
    for i in range(int(sqrt(len(parts)))):
        row = parts[i*int(sqrt(len(parts))): i*int(sqrt(len(parts)))+int(sqrt(len(parts)))]
        rows.append(np.hstack(row))
    full = np.concatenate(rows)

    return transform(full, rules, t-1)

def split(array, nrows, ncols):
    _, h = array.shape
    return (array.reshape(h//nrows, nrows, -1, ncols)
                 .swapaxes(1, 2)
                 .reshape(-1, nrows, ncols))

def get_keys(key):
    for _ in range(4):
        key = np.rot90(key)
        yield key
        yield np.flipud(key)

if __name__ == "__main__":
    sys.exit(main())