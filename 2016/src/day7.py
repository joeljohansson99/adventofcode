import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for line in input:
        hypernet = re.findall(r'\[([A-Za-z0-9_]+)\]', line)
        sequences = [seq for seq in re.split(r'[\[\]]', line) if seq not in hypernet]
        if not any([isABBA(seq) for seq in hypernet]) and any([isABBA(seq) for seq in sequences]):
            count += 1
    return count

def part2(input):
    count = 0
    for line in input:
        hypernet = re.findall(r'\[([A-Za-z0-9_]+)\]', line)
        sequences = [seq for seq in re.split(r'[\[\]]', line) if seq not in hypernet]
        babs = set()
        for seq in sequences:
            addBABs(seq, babs)
        for bab in babs:
            if any([bab in seq for seq in hypernet]):
                count += 1
                break


    return count

def isABBA(seq):
    for i in range(len(seq)):
        if list(seq[i:i+2]) == list(reversed(seq[i+2:i+4])) and seq[i] != seq[i+1]:
            return True
    return False

def addBABs(seq, pairs):
    for i in range(len(seq)-2):
        if seq[i] == seq[i+2] != seq[i+1]:
            BAB = seq[i+1] + seq[i] + seq[i+1]
            pairs.add(BAB)

if __name__ == "__main__":
    sys.exit(main())
