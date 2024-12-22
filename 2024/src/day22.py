from collections import defaultdict
import functools
import os
import sys
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day22.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    numbers = [int(line) for line in input]
    for _ in range(2000):
        next=[]
        for num in numbers:
            num = mix(num, num*64)
            num = prune(num)
            num = mix(num, (num//32))
            num = prune(num)
            num = mix(num, num*2048)
            num = prune(num)
            next.append(num)
        numbers = next
    return sum(numbers)

def part2(input):
    numbers = [int(line) for line in input]
    price = [[num%10] for num in numbers]
    diff = [[] for _ in numbers]
    bananas = defaultdict(int)
    seen = [set() for _ in numbers]
    for k in range(2000):
        next=[]
        for i in range(len(numbers)):
            num = numbers[i]
            num = mix(num, num*64)
            num = prune(num)
            num = mix(num, (num//32))
            num = prune(num)
            num = mix(num, num*2048)
            num = prune(num)
            price[i].append(num%10)
            diff[i].append(price[i][-1] - price[i][-2])
            if k > 2:
                key = tuple(diff[i][len(diff[i])-4:len(diff[i])])
                if key not in seen[i]:
                    bananas[key] += price[i][-1]
                    seen[i].add(key)
            next.append(num)
        numbers = next
    

    return max(bananas.values())

def mix(secret, num):
    return num ^ secret

def prune(num):
    return num % 16777216


if __name__ == "__main__":
    sys.exit(main())