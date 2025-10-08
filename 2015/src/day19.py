import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day19.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    tranformations = list()
    for line in input:
        if "=>" in line:
            [a, b] = line.split(" => ")
            tranformations.append((a,b))
        elif len(line) > 0:
            mol = line
    
    variants = set()
    for (a,b) in tranformations:
        for match in re.finditer(a, mol):
            variants.add(mol[:match.start()] + b + mol[match.end():])

    return len(variants)

def part2(input):
    tranformations = list()
    for line in input:
        if "=>" in line:
            [a, b] = line.split(" => ")
            tranformations.append((a,b))
        elif len(line) > 0:
            mol = line

    mols = [mol]
    seen = set(mol)
    tranformations = sorted(tranformations, key=lambda x: len(x[1]), reverse=True)
    count = 0
    while not any([m == 'e' for m in mols]):
        next_mols = []
        for m in mols:
            for n in replace(m, tranformations):
                if n not in seen:
                    next_mols.append(n)
                    seen.add(n)
                    break
        mols = next_mols
        count += 1
    return count

def replace(mol, tranformations):
    for (a,b) in tranformations:
        for match in re.finditer(b, mol):
            yield mol[:match.start()] + a + mol[match.end():]

if __name__ == "__main__":
    sys.exit(main())
