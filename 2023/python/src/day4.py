import os
import sys
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day4.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    for card in input:
        [game, cards] = card.split(":")
        [winning, nums] = cards.split("|")
        winning = winning.split(" ")
        nums = nums.split(" ")
        winning = [int(x) for x in winning if len(x) != 0]
        nums = [int(x) for x in nums if len(x) != 0]
        
        count = 0
        for num in nums:
            if num in winning:
                count +=1
        tmp = 0 if count == 0 else 1
        while (count > 1):
            tmp = tmp * 2
            count -= 1
        sum += tmp
    
    return sum

      

def part2(input):
    wins = dict()
    for i in range (1, len(input) +1 ):
        wins[i] = 1
    for card in input:
        [game, cards] = card.split(":")
        [winning, nums] = cards.split("|")
        winning = winning.split(" ")
        nums = nums.split(" ")
        winning = [int(x) for x in winning if len(x) != 0]
        nums = [int(x) for x in nums if len(x) != 0]
        game = [x for x in game.split(" ") if len(x) != 0]
        game = int(game[1])
        
        count = 0
        for num in nums:
            if num in winning:
                count +=1
            
        inc = wins[game]

        for i in range(0,count):
            wins[game+i+1] += inc
    
    sum = 0

    for key, value in wins.items():
        sum += value
            
    
    return sum


if __name__ == "__main__":
    sys.exit(main())