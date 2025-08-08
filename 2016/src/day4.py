from collections import defaultdict
import os
import re
import string
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day4.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    id_sum = 0
    for line in input:
        [name, rest] = line.rsplit('-', 1)
        checksum = re.search(r"\[([A-Za-z0-9_]+)\]", rest).group(1)
        sector_id = int(re.search(r"[+-]?\d+(?:\.\d+)?", rest).group())
        name = name.replace("-", "")
        counts = defaultdict(int)
        for c in name:
            counts[c] += 1
        order = sorted(counts.keys(), key=lambda x: (counts[x], -ord(x)), reverse=True)
        if checksum == "".join(order[:5]):
            id_sum += sector_id
    return id_sum


def part2(input):
    alphabet = string.ascii_lowercase
    for line in input:
        [name, rest] = line.rsplit('-', 1)
        checksum = re.search(r"\[([A-Za-z0-9_]+)\]", rest).group(1)
        sector_id = int(re.search(r"[+-]?\d+(?:\.\d+)?", rest).group())
        counts = defaultdict(int)
        for c in name.replace("-", ""):
            counts[c] += 1
        order = sorted(counts.keys(), key=lambda x: (counts[x], -ord(x)), reverse=True)
        if checksum == "".join(order[:5]):
            room = []
            for i in range(len(name)):
                if name[i] == '-':
                    room.append(" ")
                    continue
                idx = alphabet.index(name[i])
                new_idx = (idx+sector_id) % len(alphabet)
                room.append(alphabet[new_idx])
            room = "".join(room)
            if "north" in room:
                return sector_id

if __name__ == "__main__":
    sys.exit(main())
