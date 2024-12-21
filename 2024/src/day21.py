from itertools import permutations
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day21.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

KEYPAD = [
    {
       "^":(0,1),
       "A":(0,2),
       "<":(1,0),
       "v":(1,1),
       ">":(1,2)
   }, {
       "7":(0,0),
       "8":(0,1),
       "9":(0,2),
       "4":(1,0),
       "5":(1,1),
       "6":(1,2),
       "1":(2,0),
       "2":(2,1),
       "3":(2,2),
       "0":(3,1),
       "A":(3,2)
   } 
]

DIR = {
       "^":(-1,0),
       "<":(0,-1),
       "v":(1,0),
       ">":(0,1)
}

def part1(input):
    ans = 0
    for code in input:
        seq = path(code, 2, KEYPAD[1])
        ans += seq * int(code[:-1])
    return ans

def part2(input):
    ans = 0
    for code in input:
        seq = path(code, 25, KEYPAD[1])
        ans += seq * int(code[:-1])
    return ans

def path(code, level, keypad):
    if level < 0:
        return len(code)
    presses = 0
    start = "A"
    for c in code:
        presses += press(start, c, keypad, level)
        start = c
    return presses

cache = dict()
def press(start, end, keypad, level):
    key = (start, end, level)
    if key in cache:
        return cache[key]
    dr, dc = keypad[start][0] - keypad[end][0], keypad[start][1] - keypad[end][1]
    
    buttons = ""
    if dr > 0:
        buttons += "^"*abs(dr)
    if dr < 0:
        buttons += "v"*abs(dr)
    if dc > 0:
        buttons += "<"*abs(dc)
    if dc < 0:
        buttons += ">"*abs(dc)

    count = float('inf')
    for order in set(permutations(buttons)):
        (r, c) = keypad[start]
        for o in order:
            (dr, dc) = DIR[o]
            (r, c) = (r+dr, c+dc)
            if (r,c) not in keypad.values():
                break
        else:
            count = min(path(list(order)+["A"], level-1, KEYPAD[0]), count)
    cache[key] = count
    return count

if __name__ == "__main__":
    sys.exit(main())