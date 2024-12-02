import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day2.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for line in input:
        inc = False
        dec = False
        report = list(map(int, re.findall(r'\d+', line)))
        safe = True
        for i in range(len(report)-1):
            if (report[i] > report[i+1]):
                inc = True
            if (report[i] < report[i+1]):
                dec = True
            if not( abs(report[i] - report[i+1]) > 0 and abs(report[i] - report[i+1]) <= 3):
                safe = False
        if safe and ((dec and not inc) or (inc and not dec)):
            count += 1
    
    return count

def part2(input):
    count = 0
    for line in input:
        reports = list(map(int, re.findall(r'\d+', line)))
        for miss in range((len(reports))):
            report = reports.copy()
            del report[miss]
            inc = False
            dec = False
            safe = True
            for i in range(len(report)-1):
                if (report[i] > report[i+1]):
                    inc = True
                if (report[i] < report[i+1]):
                    dec = True
                if not( abs(report[i] - report[i+1]) > 0 and abs(report[i] - report[i+1]) <= 3):
                    safe = False
            if safe and ((dec and not inc) or (inc and not dec)):
                count += 1
                break
    
    return count

if __name__ == "__main__":
    sys.exit(main())