import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day1.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    for line in input:
        fst = findFirst(line)
        lst = findFirst(line[::-1])
        sum += int(fst+lst)
        
    return sum
      
def findFirst(str):
    for c in str:
        if c.isdigit():
            return c

def part2(input):
    sum = 0
    for line in input:
        fst = findFirst2(line)
        lst = findLast2(line)
        sum += int(fst+lst)
        
    return sum

def findFirst2(str):
    for i in range(0, len(str)):
        if str[i].isdigit():
            return str[i]
        else:
            for j in range(0, i):
                if toNum(str[j:i+1]):
                    return toNum(str[j:i+1])

def findLast2(str):
    for i in range(len(str)-1, -1, -1):
        if str[i].isdigit():
            return str[i]
        else:
            for j in range(len(str), i-1, -1):
                if toNum(str[i:j]):
                    return toNum(str[i:j])
        
def toNum(s):
    if s == "one":
        return "1"
    elif s == "two":
        return "2"
    elif s == "three":
        return "3"
    elif s == "four":
        return "4"
    elif s == "five":
        return "5"
    elif s == "six":
        return "6"
    elif s == "seven":
        return "7"
    elif s == "eight":
        return "8"
    elif s == "nine":
        return "9"
    else:
        return ""
    

if __name__ == "__main__":
    sys.exit(main())