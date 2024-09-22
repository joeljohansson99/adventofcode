import os
import sys
import re

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day4.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    actions = dict()
    dates = list()
    for line in input:
        info = line.split("]")
        [_, month, day, hour, min] = list(map(int, re.findall(r'\d+', info[0])))
        if hour == 23:
            min = 0
            day += 1
            if month == 2 and day == 29:
                day = 1
                month += 1
            elif month in [1, 3, 5, 7, 8, 10, 12] and day == 32:
                day = 1
                month += 1
            elif day == 31:
                day = 1
                month += 1

        if (month, day) not in dates:
            dates.append((month,day))
        if (month, day) not in actions:
            actions[(month, day)] = dict()
        if min not in actions[(month, day)]:
            actions[(month, day)][min] = list()
        actions[(month, day)][min].append(info[1])
    
    dates = sorted(dates, key=lambda date: (date[0], date[1]))

    elves = dict()
    elf = None
    sleeping = False
    for date in dates:
        sleep = set()
        for min in range(0,60):
            if min in actions[date]:
                for action in sorted(actions[date][min]):
                    if "begins" in action:
                        elf = int(re.search(r'\d+', action).group())
                        if elf not in elves:
                            elves[elf] = dict()
                        sleeping = False
                    elif "asleep" in action:
                        sleeping = True
                    elif "wakes" in action:
                        sleeping = False
            if sleeping:
                elves[elf][min] = elves[elf][min] + 1 if min in elves[elf] else 1
    
    sleep = dict()

    for (elv, mins) in elves.items():
        max_sleep = 0
        max_min = 0
        total_sleep = 0
        for (min, time) in mins.items():
            total_sleep += time
            if time > max_sleep:
                max_min = min
                max_sleep = time
        sleep[elv] = (total_sleep, max_min)
    sleepiest = None
    max_sleep = 0

    for (elv, (time, min)) in sleep.items():
        if time > max_sleep:
            sleepiest = elv
            max_sleep = time

    (_, min) = sleep[sleepiest]
    return sleepiest * min


def part2(input):
    actions = dict()
    dates = list()
    for line in input:
        info = line.split("]")
        [_, month, day, hour, min] = list(map(int, re.findall(r'\d+', info[0])))
        if hour == 23:
            min = 0
            day += 1
            if month == 2 and day == 29:
                day = 1
                month += 1
            elif month in [1, 3, 5, 7, 8, 10, 12] and day == 32:
                day = 1
                month += 1
            elif day == 31:
                day = 1
                month += 1

        if (month, day) not in dates:
            dates.append((month,day))
        if (month, day) not in actions:
            actions[(month, day)] = dict()
        if min not in actions[(month, day)]:
            actions[(month, day)][min] = list()
        actions[(month, day)][min].append(info[1])
    
    dates = sorted(dates, key=lambda date: (date[0], date[1]))

    elves = dict()
    elf = None
    sleeping = False
    for date in dates:
        sleep = set()
        for min in range(0,60):
            if min in actions[date]:
                for action in sorted(actions[date][min]):
                    if "begins" in action:
                        elf = int(re.search(r'\d+', action).group())
                        if elf not in elves:
                            elves[elf] = dict()
                        sleeping = False
                    elif "asleep" in action:
                        sleeping = True
                    elif "wakes" in action:
                        sleeping = False
            if sleeping:
                elves[elf][min] = elves[elf][min] + 1 if min in elves[elf] else 1
    
    sleep = dict()

    for (elv, mins) in elves.items():
        max_sleep = 0
        max_min = 0
        for (min, time) in mins.items():
            if time > max_sleep:
                max_min = min
                max_sleep = time
        sleep[elv] = (max_sleep, max_min)
    sleepiest = None
    max_sleep = 0

    for (elv, (sleep_min, min)) in sleep.items():
        if sleep_min > max_sleep:
            sleepiest = elv
            max_sleep = sleep_min

    (_, min) = sleep[sleepiest]
    return sleepiest * min


if __name__ == "__main__":
    sys.exit(main())