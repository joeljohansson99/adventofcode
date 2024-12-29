import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day1.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    nums = input[0]
    for i in range(len(nums)):
        if nums[i] == nums[(i+1)%len(nums)]:
            sum += int(nums[i])
    return sum
                

def part2(input):
    sum = 0
    nums = input[0]
    for i in range(len(nums)):
        if nums[i] == nums[(i+(len(nums)//2))%len(nums)]:
            sum += int(nums[i])
    return sum

if __name__ == "__main__":
    sys.exit(main())