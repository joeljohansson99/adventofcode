from collections import defaultdict
import os
from queue import LifoQueue, Queue
import sys
import threading

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day25.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))

def part1(input):
    state = input[0].split(" ")[-1][0]
    steps = int(input[1].split(" ")[5])
    states = dict()
    for i in range(3, len(input), 10):
        s = input[i].split(" ")[-1][0]
        zero = (int(input[i+2][22]), 1 if input[i+3].split(" ")[-1] == "right." else -1, input[i+4].split(" ")[-1][0])
        one = (int(input[i+6][22]), 1 if input[i+7].split(" ")[-1] == "right." else -1, input[i+8].split(" ")[-1][0])
        states[s] = (zero, one)

    ones = set()
    loc = 0
    for _ in range(steps):
        (zero, one) = states[state]
        if loc in ones:
            (w, m, n) = one
            if w == 0:
                ones.remove(loc)
            loc += m
            state = n
        else:
            (w, m, n) = zero
            if w == 1:
                ones.add(loc)
            loc += m
            state = n

    return len(ones)

if __name__ == "__main__":
    sys.exit(main())