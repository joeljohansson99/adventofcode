import functools
import os
import sys

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    powers = dict()
    serial = int(input[0])
    for x in range(1, 301-3):
        for y in range(1, 301-3):
            powers[(x,y)] = 0
            for dx in range(0, 3):
                for dy in range(0, 3):
                    power = x+dx + 10
                    power *= (y+dy)
                    power += serial
                    power *= (x+dx + 10)
                    power = (power % 1000) // 100
                    power -= 5
                    powers[(x,y)] += power
    
    max = 0
    (mx,my) = (0,0)
    for (c, power) in powers.items():
        if power > max:
            max = power
            (mx,my) = c
    
    return f'{mx},{my}'
                
                
def part2(input):    
    powers = list()
    serial = int(input[0])
    for x in range(1, 301):
        powers.append(list())
        for y in range(1, 301):
            power = x + 10
            power *= y
            power += serial
            power *= (x + 10)
            power = (power % 1000) // 100
            power -= 5
            powers[x-1].append(power)

    @functools.cache
    def get_power(x, y, size):
        if size == 0:
            return 0
        
        power = 0
        for dx in range(x, x+size):
            power += powers[dx][y]
        for dy in range(y+1, y+size):
            power += powers[x][dy]

        power += get_power(x+1, y+1, size-1)

        return power

    best_power = 0
    best_cord = 0
    best_size = 0
    for size in range(0,300):
        for x in range(0, 300-size):
            for y in range(0, 300-size):
                power = get_power(x,y,size)
                if power > best_power:
                    best_power = power
                    best_cord = (x,y)
                    best_size = size
    

    return f'{best_cord[0]+1},{best_cord[1]+1},{best_size}'

if __name__ == "__main__":
    sys.exit(main())