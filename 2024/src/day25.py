import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day25.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    ups = []
    downs = []
    for i in range(0, len(input), 8):
        key = [0,0,0,0,0]
        if ("#####" == input[i]):
            for c in range(5):
                for r in range(i+1,i+8):
                    if input[r][c] == "#":
                        key[c] += 1
                    else:
                        break
            ups.append(key)
        else:
            for c in range(5):
                for r in range(i+5,i, -1):
                    if input[r][c] == "#":
                        key[c] += 1
                    else:
                        break
            downs.append(key)
            
    count = 0
    for up in set([tuple(up) for up in ups]):
        for down in set([tuple(down) for down in downs]):
            for i in range(len(up)):
                if (down[i] + up[i]) >= 6:
                    break
            else:
                count += 1
    return count

def part2(input):
    pass

if __name__ == "__main__":
    sys.exit(main())