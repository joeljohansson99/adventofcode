import os
import sys
import string

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    poly = input[0]
    i = 0
    while True:
        if abs(ord(poly[i]) - ord(poly[i+1])) == 32:
            poly = poly[:i] + poly[i+2:]
            if i != 0:
                i-=1
        else:
            i+=1
        if i >= len(poly)-1:
            break
    return len(poly)

            

def part2(input):
    best = len(input[0])
    for c in string.ascii_lowercase:
        poly = input[0].replace(c, "").replace(c.upper(), "")
        i = 0
        while True:
            if abs(ord(poly[i]) - ord(poly[i+1])) == 32:
                poly = poly[:i] + poly[i+2:]
                if i != 0:
                    i-=1
            else:
                i+=1
            if i >= len(poly)-1:
                break
        if len(poly) < best:
            best = len(poly)
    return best

if __name__ == "__main__":
    sys.exit(main())