import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day2.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    numpad = "123\n" \
             "456\n" \
             "789\n".split("\n")
    nums = dict()
    for r in range(len(numpad)):
        for c in range(len(numpad[r])):
            nums[(r,c)] = numpad[r][c]
            if numpad[r][c] == "5":
                pos = (r,c)
                
    code = ""
    for line in input:
        for dir in line:
            (r,c) = pos
            if dir == "U":
                next = (r-1,c)
            if dir == "D":
                next = (r+1,c)
            if dir == "R":
                next = (r,c+1)
            if dir == "L":
                next = (r,c-1)
            if next in nums:
                pos = next
        code += nums[pos]

    return code

def part2(input):
    numpad = "  1\n" \
             " 234\n" \
             "56789\n" \
             " ABC\n" \
             "  D\n".split("\n")
    nums = dict()
    for r in range(len(numpad)):
        for c in range(len(numpad[r])):
            if numpad[r][c] != " ":
                nums[(r,c)] = numpad[r][c]
            if numpad[r][c] == "5":
                pos = (r,c)
                
    code = ""
    for line in input:
        for dir in line:
            (r,c) = pos
            if dir == "U":
                next = (r-1,c)
            if dir == "D":
                next = (r+1,c)
            if dir == "R":
                next = (r,c+1)
            if dir == "L":
                next = (r,c-1)
            if next in nums:
                pos = next
        code += nums[pos]

    return code

if __name__ == "__main__":
    sys.exit(main())
