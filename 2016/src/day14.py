from collections import defaultdict
import functools
import hashlib
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day14.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    salt = input[0].encode('utf-8')
    triples = defaultdict(set)
    keys = set()
    index = 0
    while len(keys) < 64:
        hash = hashlib.md5(salt + str(index).encode()).digest().hex()
        fives = getFive(hash)
        for five in fives:
            if five in triples:
                for n in sorted(triples[five]):
                    diff = index - n
                    if diff <= 1000 and n not in keys:
                        keys.add(n)
        
        triple = getTriple(hash)
        if triple:
            triples[triple].add(index)
        index += 1
    
    return sorted(keys)[63]


def part2(input):
    sys.setrecursionlimit(30000)
    salt = input[0]
    triples = defaultdict(set)
    keys = set()
    index = 0
    while len(keys) < 64:
        hash = getHash(salt + str(index), 2016)
        fives = getFive(hash)
        for five in fives:
            if five in triples:
                for n in sorted(triples[five]):
                    diff = index - n
                    if diff <= 1000 and n not in keys:
                        keys.add(n)
        
        triple = getTriple(hash)
        if triple:
            triples[triple].add(index)
        index += 1
    
    return sorted(keys)[63]

def getHash(hash, left):
    if left == 0:
        return hashlib.md5(hash.encode()).digest().hex()
    return hashlib.md5(getHash(hash, left-1).encode()).digest().hex()

def getTriple(hash):
    for i in range(len(hash)-2):
        if len(set(hash[i:i+3])) == 1:
            return hash[i]

def getFive(hash):
    fives = set()
    for i in range(len(hash)-4):
        if len(set(hash[i:i+5])) == 1:
            fives.add(hash[i])
    return fives


if __name__ == "__main__":
    sys.exit(main())
