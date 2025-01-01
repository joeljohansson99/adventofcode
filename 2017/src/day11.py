import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    dirs = input[0].split(",")
    p = (0,0)
    for dir in dirs:
        dp = step(dir)
        p = (p[0]+dp[0], p[1]+dp[1])
    
    return max(abs(p[0]), abs(p[1]))

                

def part2(input):
    dirs = input[0].split(",")
    p = (0,0)
    furthest = 0
    for dir in dirs:
        dp = step(dir)
        p = (p[0]+dp[0], p[1]+dp[1])
        furthest = max(furthest, max(abs(p[0]), abs(p[1])))
    
    return furthest

#   \ n  /
# nw +--+ ne
#   /    \
# -+      +-
#   \    /
# sw +--+ se
#   / s  \

def step(dir):
    if dir == "nw":
        return (-1, -1)
    elif dir == "n":
        return (-1, 0)
    elif dir == "ne":
        return (-1, 1)
    elif dir == "sw":
        return (1, -1)
    elif dir == "s":
        return (1, 0)
    elif dir == "se":
        return (1, 1)

if __name__ == "__main__":
    sys.exit(main())