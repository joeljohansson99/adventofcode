import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for line in input:
        if vowels(line) and double(line) and not illegal(line):
            count += 1
    return count

def part2(input):

    print(non_overlapping_pair("qjhvhtzxzqqjkmpb"))
    print(three_anagram("qjhvhtzxzqqjkmpb"))
    count = 0
    for line in input:
        if non_overlapping_pair(line) and three_anagram(line):
            count += 1
    return count

def vowels(s):
    return sum([c in "aeiou" for c in s]) >= 3

def double(s):
    return any([s[i] == s[i+1] for i in range(len(s) - 1)])

def illegal(s):
    return any([illegal in s for illegal in ["ab", "cd", "pq", "xy"]])

def non_overlapping_pair(s):
    pairs = [s[i:i+2] for i in range(len(s) - 1)]
    for i in range(len(pairs)):
        for j in range(i+2,len(pairs)):
            if pairs[i] == pairs[j]:
                return True
    return False


def three_anagram(s):
    return any([s[i] == s[i+2] != s[i+1] for i in range(len(s) - 2)])

if __name__ == "__main__":
    sys.exit(main())
