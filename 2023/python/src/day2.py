import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day2.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))


def part1(input):
    sum = 0
    for i in range(0, len(input)):
        game, sets = input[i].split(":")
        sets = sets.split(";")
        impossible = False
        
        for set in sets:
            bags = set.split(",")
            for bag in bags:
                num, color = filter(len, bag.split(" "))
                if color == "blue":
                    if int(num) > 14:
                        impossible = True
                        break
                if color == "red":
                    if int(num) > 12:
                        impossible = True
                        break 
                if color == "green":
                    if int(num) > 13:
                        impossible = True
                        break 
            if impossible:
                break
            
        if not impossible:
            sum += int(game.split(" ")[1])
    return sum
                

def part2(input):
    sum = 0
    for i in range(0, len(input)):
        game, sets = input[i].split(":")
        sets = sets.split(";")
        
        red = 0
        blue = 0
        green = 0
        
        for set in sets:
            bags = set.split(",")
            for bag in bags:
                num, color = filter(len, bag.split(" "))
                if color == "blue":
                    if int(num) > blue:
                        blue = int(num)
                if color == "red":
                    if int(num) > red:
                        red = int(num)
                if color == "green":
                    if int(num) > green:
                        green = int(num)
            
        sum += (green*red*blue)
        
    return sum



if __name__ == "__main__":
    sys.exit(main())