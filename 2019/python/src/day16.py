
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day16.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    signal = list([int(i) for i in input[0]])
    base = [0, 1, 0, -1]

    for _ in range(100):
        for i in range(len(signal)):
            mod_base = [b for b in base for _ in range(i+1)]
            new = 0
            for k in range(i, len(signal)):
                new += signal[k]*mod_base[(k+1)%len(mod_base)]
            signal[i] = abs(new) % 10

    return "".join([str(n) for n in signal[:8]])

def part2(input):
    signal = list(map(int, input[0])) * 10000
    offset = int(input[0][:7])

    for _ in range(100):
        num = sum([signal[i] for i in range(offset, len(signal))])
        for i in range(offset, len(signal)):
            tmp = abs(num) % 10
            num -= signal[i]
            signal[i] = tmp

    return "".join(str(n) for n in signal[offset:offset+8])

if __name__ == "__main__":
    sys.exit(main())