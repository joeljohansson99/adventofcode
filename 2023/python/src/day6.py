import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    times = [int(x) for x in input[0].split(" ")[1:] if len(x) > 0]
    records = [int(x) for x in input[1].split(" ")[1:] if len(x) > 0]
    ret = 1
    for k in range(0,len(times)):
        ways = 0  
        for i in range(0, times[k]):
            if i * (times[k] - i) > records[k]:
                ways+=1
        ret *= ways
    
    return ret
    

def part2(input):
    time = int(input[0].split(":")[1].replace(" ", ""))
    record = int(input[1].split(":")[1].replace(" ", ""))
    ways = 0
    for i in range(0, time):
        if i * (time - i) > record:
            ways+=1
    
    return ways

if __name__ == "__main__":
    sys.exit(main())