import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    nums = []
    for line in input[:-1]:
        nums.append(aoc.ints(line))
    ops = input[-1].split(" ")
    ops = [o for o in ops if o != ""]
    total = 0
    for c in range(len(ops)):
        col = 0 if ops[c] == "+" else 1
        for r in range(len(nums)):
            if ops[c] == "+":
                col += nums[r][c]
            else:
                col *= nums[r][c]
        total += col
    return total

def part2(input):
    rows = len(input[:-1])
    nums = [[] for _ in range(rows)]
    ns = ["" for _ in range(rows)]
    for c in range(len(input[0])):
        if all([input[r][c] == " " for r in range(rows)]):
            for r in range(rows):
                nums[r].append(ns[r])
                ns[r] = ""
            continue
        for r in range(rows):
            ns[r] += input[r][c]
    for r in range(rows):
        nums[r].append(ns[r])

    ops = input[-1].split(" ")
    ops = [o for o in ops if o != ""]
    total = 0
    for c in range(len(ops)):
        col = 0 if ops[c] == "+" else 1
        targets = []
        for r in range(len(nums)):
            targets.append(nums[r][c])
        new_nums = []
        for i in range(len(targets[0])-1,-1,-1):
            new_num = ""
            for r in range(len(targets)):
                new_num += str(targets[r][i])
            if "".join(new_num.split(" ")) == "":
                new_nums.append(0)
            else:
                new_nums.append(int("".join(new_num.split(" "))))
        for r in range(len(new_nums)):
            if ops[c] == "+":
                col += new_nums[r]
            else:
                col *= new_nums[r]
        total += col 
    return total

if __name__ == "__main__":
    sys.exit(main())