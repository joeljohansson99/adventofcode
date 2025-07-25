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
    data = [input[0][i:i+25] for i in range(0, len(input[0]), 25)]
    layers = [data[i:i+6] for i in range(0, len(data), 6)]

    minimum = (10000000, 0, 0)
    
    for layer in layers:
        zeros = 0
        ones = 0
        twos = 0
        for row in layer:
            for pixel in row:
                if pixel == '0':
                    zeros += 1
                if pixel == '1':
                    ones += 1
                if pixel == '2':
                    twos += 1

        if zeros < minimum[0]:
            minimum = (zeros, ones, twos)
    
    return minimum[1] * minimum[2]

def part2(input):
    data = [input[0][i:i+25] for i in range(0, len(input[0]), 25)]
    layers = [data[i:i+6] for i in range(0, len(data), 6)]

    image = [['2']*25 for _ in range(6)]
    
    for layer in layers:
        for r in range(len(layer)):
            for c in range(len(layer[r])):
                if image[r][c] == '2':
                    image[r][c] = layer[r][c]
    
    return "\n"+"\n".join(["".join(row).replace('0', ' ').replace('1', '#') for row in image])

if __name__ == "__main__":
    sys.exit(main())