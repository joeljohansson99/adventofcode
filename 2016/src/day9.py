import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day9.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    file = ""
    rest = input[0]
    while True:
        match = re.search(r'\((\d+)+x(\d+)\)', rest)
        if match is None:
            break
        chars = int(match.group(1))
        factor = int(match.group(2))
        file += rest[:match.start()] + rest[match.end():match.end()+chars]*factor
        rest = rest[match.end()+chars:]
    file += rest

    return len(file)

def part2(input):
    file = input[0]
    weigths = [1]*len(file)
    for match in re.finditer(r'\((\d+)+x(\d+)\)', file):
        chars = int(match.group(1))
        factor = int(match.group(2))
        for i in range(match.end(), match.end()+chars):
            weigths[i] *= factor
            
    length = 0
    for i in range(len(file)):
        if file[i].isalpha() and file[i].isupper():
            length += weigths[i]


    return length

if __name__ == "__main__":
    sys.exit(main())
