import math
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day16.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    packet = ""
    for c in input[0]:
        packet += bin(int(c, 16))[2:].zfill(4)
    return parse(packet, 0)[0]

def part2(input):
    packet = ""
    for c in input[0]:
        packet += bin(int(c, 16))[2:].zfill(4)
    return parse(packet, 0)[1]

def parse(packet, i):
    version_sum = int(packet[i:i+3], 2)
    i+=3
    type = int(packet[i:i+3], 2)
    i+=3
    val = 0
    if type == 4:
        strval = ""
        while True:
            sub = packet[i:i+5]
            strval += sub[1:]
            i+=5
            if sub[0] == "0":
                break
        val = int(strval,2)
    else:
        id = int(packet[i])
        i+=1
        subvals = list()
        if id == 0:
            length = int(packet[i:i+15],2)
            i+=15
            end = i + length
            while True:
                (subsum, subval, i) = parse(packet, i)
                version_sum += subsum
                subvals.append(subval)
                if i >= end:
                    break
        else:
            length = int(packet[i:i+11],2)
            i+=11
            for _ in range(length):
                (subsum, subval, i) = parse(packet, i)
                version_sum += subsum
                subvals.append(subval)

        if type == 0:
            val = sum(subvals)
        if type == 1:
            val = math.prod(subvals)
        if type == 2:
            val = min(subvals)
        if type == 3:
            val = max(subvals)
        if type == 5:
            val = 1 if subvals[0] > subvals[1] else 0
        if type == 6:
            val = 1 if subvals[0] < subvals[1] else 0
        if type == 7:
            val = 1 if subvals[0] == subvals[1] else 0

    return (version_sum, val, i)


if __name__ == "__main__":
    sys.exit(main())