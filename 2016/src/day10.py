from collections import defaultdict
import os
import utils.aoc as aoc
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    bots = defaultdict(list)
    vals = defaultdict(list)

    full = list()
    for line in input:
        if "value" in line:
            [val, bot] = aoc.ints(line)
            vals[bot].append(val)
            if len(vals[bot]) == 2:
                full.append(bot)
        else:
            info = line.split(" ")
            [bot, low, high] = aoc.ints(line)
            if info[5] == "bot":
                bots[bot].append((0,low))
            if info[10] == "bot":
                bots[bot].append((1,high))

    while full:
        bot = full.pop(0)
        if 61 in vals[bot] and 17 in vals[bot]:
            return bot
        for (x, rec) in bots[bot]:
            if x == 0:
                vals[rec].append(min(vals[bot]))
                if len(vals[rec]) == 2:
                    full.append(rec)
            if x == 1:
                vals[rec].append(max(vals[bot]))
                if len(vals[rec]) == 2:
                    full.append(rec)

def part2(input):
    bots = defaultdict(list)
    vals = defaultdict(list)
    outputs = defaultdict(int)

    full = list()
    for line in input:
        if "value" in line:
            [val, bot] = aoc.ints(line)
            vals[bot].append(val)
            if len(vals[bot]) == 2:
                full.append(bot)
        else:
            info = line.split(" ")
            [bot, low, high] = aoc.ints(line)
            bots[bot].append((0, info[5] != "bot",low))
            bots[bot].append((1, info[10] != "bot",high))

    while full:
        bot = full.pop(0)
        for (x, out, rec) in bots[bot]:
            if out:
                if x == 0:
                    outputs[rec] = min(vals[bot])
                if x == 1:
                    outputs[rec] = max(vals[bot])
            else:
                if x == 0:
                    vals[rec].append(min(vals[bot]))
                    if len(vals[rec]) == 2:
                        full.append(rec)
                if x == 1:
                    vals[rec].append(max(vals[bot]))
                    if len(vals[rec]) == 2:
                        full.append(rec)
    
    return outputs[0] * outputs[1] * outputs[2]

if __name__ == "__main__":
    sys.exit(main())
