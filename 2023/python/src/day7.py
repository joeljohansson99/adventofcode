import os
import sys
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    cards = "AKQJT98765432"
    sum = 0
    for i in range(0, len(input)):
        (hand,bid) = input[i].split(" ")
        kind = pairs(hand, False)
        count = 0
        max_hand = max_pair(kind)
        for j in range(0, len(input)):
            if i == j:
                continue
            cmp_hand = input[j].split(" ")[0]
            cmp = pairs(cmp_hand, False)
            max_cmp = max_pair(cmp)
            if max_hand > max_cmp:
                count+=1
            elif max_hand == max_cmp:
                if len(kind) > len(cmp):
                    count += 1
                elif len(kind) == len(cmp):
                    for k in range(0,5):
                        if cards.index(hand[k]) < cards.index(cmp_hand[k]):
                            count += 1
                            break
                        elif cards.index(hand[k]) > cards.index(cmp_hand[k]):
                            break
        sum += (count+1)*int(bid)
    return sum

def max_pair(pairs):
    if len(pairs) == 0:
        return 1
    return max([y for (x,y) in pairs]) 

def pairs(hand, jokers):
    ret = []
    counter = dict() 

    for char in hand:
        counter[char] = counter.get(char, 0) + 1 

    for char, count in counter.items():
        if jokers:
            if char == 'J':
                continue
        if count > 1:
            ret.append((char, count))
    if len(ret) == 0 and jokers:
        for char, count in counter.items():
            if char == 'J':
                continue
            ret.append((char, count))
            if len(ret) == 1:
                return ret
    if len(ret) == 0 and jokers:
        ret.append(('J', 0))
    return ret


def part2(input):
    cards = "AKQT98765432J"
    sum = 0
    for i in range(0, len(input)):
        (hand,bid) = input[i].split(" ")
        kind = pairs(hand, True)
        max_hand = max_pair(kind) + countJ(hand)
        count = 0
        
        for j in range(0, len(input)):
            if i == j:
                continue
            cmp_hand = input[j].split(" ")[0]
            cmp = pairs(cmp_hand, True)
            max_cmp = max_pair(cmp) + countJ(cmp_hand)

            if max_hand > max_cmp:
                count+=1
            elif max_hand == max_cmp:
                if len(kind) > len(cmp):
                    count += 1
                elif len(kind) == len(cmp):
                    for k in range(0,5):
                        if cards.index(hand[k]) < cards.index(cmp_hand[k]):
                            count += 1
                            break
                        elif cards.index(hand[k]) > cards.index(cmp_hand[k]):
                            break

        sum += (count+1)*int(bid)
    return sum

def countJ(hand):
    return hand.count('J')


if __name__ == "__main__":
    sys.exit(main())