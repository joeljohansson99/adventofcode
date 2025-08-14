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
    data = input[0]
    disk = 272
    
    while len(data) < disk:
        data = transform(data)
    data = data[:disk]
    while len(data) % 2 == 0:
        data = checksum(data)
    return data

def part2(input):
    data = input[0]
    disk = 35651584
    
    while len(data) < disk:
        data = transform(data)
    data = data[:disk]
    while len(data) % 2 == 0:
        data = checksum(data)
    return data

def transform(a):
    b = ""
    for c in reversed(a):
        b += "1" if c == "0" else "0"
    return a + "0" + b

def checksum(a):
    sum = ""
    for i in range(0, len(a)-1, 2):
        sum += "1" if a[i] == a[i+1] else "0"
    return sum

if __name__ == "__main__":
    sys.exit(main())
