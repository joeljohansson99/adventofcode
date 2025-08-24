import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day8.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    chars = 0
    for line in input:
        decoded = bytes(line[1:-1], "utf-8").decode("unicode_escape")
        chars += len(line)-len(decoded)
    return chars

def part2(input):
    chars = 0
    for line in input:
        encoded = line.encode("unicode_escape").decode('utf-8').replace('"', '\\"')
        chars += len(encoded)+2-len(line)
    return chars

if __name__ == "__main__":
    sys.exit(main())
