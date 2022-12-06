import sys

def main():

    input = []
    with open('input/day4.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for elves in input:
        [elf1, elf2] = elves.split(",")
        [elf1fst, elf1snd] = elf1.split("-")
        [elf2fst, elf2snd] = elf2.split("-")
        if int(elf1fst) < int(elf2fst):
            if int(elf1snd) >= int(elf2snd):
                count += 1
        elif int(elf1fst) > int(elf2fst):
            if int(elf1snd) <= int(elf2snd):
                count += 1
        else:
            count += 1
    
    return count

def part2(input):
    count = 0
    for elves in input:
        [elf1, elf2] = elves.split(",")
        [elf1fst, elf1snd] = elf1.split("-")
        [elf2fst, elf2snd] = elf2.split("-")
        for seat in range(int(elf1fst), int(elf1snd)+1):
            if seat >= int(elf2fst) and seat <= int(elf2snd):
                count += 1
                break
    
    return count

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    sys.exit(main())