import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day16.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    programs = list("abcdefghijklmnop")
    
    for move in input[0].split(","):
        if move[0] == "s":
            i = int(re.search(r'\d+', move).group())
            programs = programs[-i:] + programs[:-i]
        if move[0] == "x":
            [i,j] = list(map(int, re.findall(r'\d+', move)))
            tmp = programs[i]
            programs[i] = programs[j]
            programs[j] = tmp
        if move[0] == "p":
            i = programs.index(move[1])
            j = programs.index(move[3])
            tmp = programs[i]
            programs[i] = programs[j]
            programs[j] = tmp

    return "".join(programs)

def part2(input):
    programs = list("abcdefghijklmnop")
    
    cache = dict()
    done = False
    dance = 0
    while dance < 1000000000:
        if tuple(programs) in cache:
            if not done:
                diff = dance - cache[tuple(programs)]
                left = (1000000000-dance)
                factor = left // diff
                dance += diff*factor
            done = True
        cache[tuple(programs)] = dance
        for move in input[0].split(","):
            if move[0] == "s":
                i = int(re.search(r'\d+', move).group())
                programs = programs[-i:] + programs[:-i]
            if move[0] == "x":
                [i,j] = list(map(int, re.findall(r'\d+', move)))
                tmp = programs[i]
                programs[i] = programs[j]
                programs[j] = tmp
            if move[0] == "p":
                i = programs.index(move[1])
                j = programs.index(move[3])
                tmp = programs[i]
                programs[i] = programs[j]
                programs[j] = tmp
        dance += 1

    return "".join(programs)

if __name__ == "__main__":
    sys.exit(main())