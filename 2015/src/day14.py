from collections import defaultdict
from email.policy import default
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day14.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    running = dict()
    resting = dict()
    deers = dict()
    distance = defaultdict(int)
    for line in input:
        deer = line.split()[0]
        [speed, run, rest] = aoc.ints(line)
        deers[deer] = (speed, run, rest)
        running[deer] = run
    
    for s in range(2503):
        toRun = []
        toRest = []
        for (deer, t) in running.items():
            if s == t:
                toRest.append(deer)
            else:
                distance[deer] += deers[deer][0]
        for (deer, t) in resting.items():
            if s == t:
                toRun.append(deer)
                distance[deer] += deers[deer][0]
        for deer in toRun:
            running[deer] = s + deers[deer][1]
            del resting[deer]
        for deer in toRest:
            resting[deer] = s + deers[deer][2]
            del running[deer]

    return max([d for (_,d) in distance.items()])

def part2(input):
    running = dict()
    resting = dict()
    deers = dict()
    distance = defaultdict(int)
    points = defaultdict(int)
    for line in input:
        deer = line.split()[0]
        [speed, run, rest] = aoc.ints(line)
        deers[deer] = (speed, run, rest)
        running[deer] = run
    
    for s in range(2503):
        toRun = []
        toRest = []
        for (deer, t) in running.items():
            if s == t:
                toRest.append(deer)
            else:
                distance[deer] += deers[deer][0]
        for (deer, t) in resting.items():
            if s == t:
                toRun.append(deer)
                distance[deer] += deers[deer][0]
        for deer in toRun:
            running[deer] = s + deers[deer][1]
            del resting[deer]
        for deer in toRest:
            resting[deer] = s + deers[deer][2]
            del running[deer]
        
        lead = max([d for (_,d) in distance.items()])
        for (deer, d) in distance.items():
            if d == lead:
                points[deer] += 1
            

    return max([p for (_,p) in points.items()])

if __name__ == "__main__":
    sys.exit(main())
