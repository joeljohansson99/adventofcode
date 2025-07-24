import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day4.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    [low, high] = list(map(int, re.findall(r'\d+', input[0])))
    count = 0
    for num in range(low, high):
        passwd = str(num)
        dec = False
        adj = False
        for i in range(len(passwd)-1):
            if ord(passwd[i]) > ord(passwd[i+1]):
                dec = True
                break
            elif ord(passwd[i]) == ord(passwd[i+1]):
                adj = True
        if (adj and not dec):
            count += 1
    return count

def part2(input):
    [low, high] = list(map(int, re.findall(r'\d+', input[0])))
    count = 0
    for num in range(low, high):
        passwd = str(num)
        dec = False
        adj = False
        for i in range(len(passwd)-1):
            if ord(passwd[i]) > ord(passwd[i+1]):
                dec = True
                break
            elif ord(passwd[i]) == ord(passwd[i+1]):
                if i-1 < 0 or ord(passwd[i-1]) != ord(passwd[i]):
                    if i+2 >= len(passwd) or ord(passwd[i+2]) != ord(passwd[i]):
                        adj = True
        if (adj and not dec):
            count += 1
    return count

if __name__ == "__main__":
    sys.exit(main())