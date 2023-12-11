import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    tmp = []
    for r in range(0, len(input)):
        tmp.append(input[r])
        exp = True
        for c in range(0, len(input[r])):
            if input[r][c] == '#':
                exp = False
                break
        if exp :
            tmp.append(input[r])

    input = tmp
    tmp = ["" for r in input]
    for c in range(0,len(input[0])):
        exp = True
        for r in range(0, len(input)):
            if input[r][c] == "#":
                exp = False
                break
        for r in range(0, len(input)):
            tmp[r] += input[r][c]
            if exp:
                tmp[r] += input[r][c]
    input = tmp

    galax = set()
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c] == '#':
                galax.add((r,c))
    sum = 0
    done = set()
    for s in galax:
        done.add(s)
        for e in galax: 
            if s != e and e in done:
                sum += findClosest(s,e,input)
    return sum
    
def findClosest(s,e,map):
    return abs(s[0] - e[0]) + abs(s[1] - e[1])
        

def part2(input):
    tmp = []
    expsR = set()
    expsC = set()
    for r in range(0, len(input)):
        tmp.append(input[r])
        exp = True
        for c in range(0, len(input[r])):
            if input[r][c] == '#':
                exp = False
                break
        if exp:
            expsR.add(r)

    input = tmp
    tmp = ["" for r in input]
    for c in range(0,len(input[0])):
        exp = True
        for r in range(0, len(input)):
            if input[r][c] == "#":
                exp = False
                break
        if exp:
            expsC.add(c)

    galax = set()
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c] == '#':
                galax.add((r,c))
    sum = 0
    done = set()
    for s in galax:
        done.add(s)
        for e in galax: 
            if s != e and e in done:
                sum += findClosest2(s,e, expsR, expsC)
    return sum

def findClosest2(s,e,expR, expC):
    countR = 0
    countC = 0
    start = (s[0], e[0])
    end = (s[1], e[1])
    for r in range(min(start), max(start)):
        if r in expR:
            countR+=1
    for c in range(min(end), max(end)):
        if c in expC:
            countC+=1

    return abs(s[0] - e[0]) + abs(s[1] - e[1]) + countR *(1000000-1) + countC * (1000000-1)

if __name__ == "__main__":
    sys.exit(main())