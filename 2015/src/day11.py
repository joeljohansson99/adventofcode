import os
import string
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    password = input[0]
    while True:
        password = inc(password)
        if increasing(password) and vowels(password) and pairs(password):
            return password

def part2(input):
    password = input[0]
    second = True
    while True:
        password = inc(password)
        if increasing(password) and vowels(password) and pairs(password):
            if second:
                second = False
            else:
                return password

def increasing(s):
    return any([ord(s[i])+2 == ord(s[i+1])+1 == ord(s[i+2]) for i in range(len(s) - 2)])

def vowels(s):
    return not ('i' in s or 'o' in s or 'l' in s) 

def pairs(s):
    pairs = set([s[i:i+2] for i in range(len(s) - 1) if s[i] == s[i+1]])
    return len(pairs) >= 2

def inc(s):
    alphabet = list(string.ascii_lowercase)
    i = len(s)-1
    next = list(s)
    carry = True
    while i >= 0 and carry:
        carry = False
        ni = (alphabet.index(s[i]) + 1)
        if ni >= len(alphabet):
            ni = 0
            carry = True
        next[i] = alphabet[ni]
        i -= 1
    return ''.join(next)

if __name__ == "__main__":
    sys.exit(main())
