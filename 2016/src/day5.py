import hashlib
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    door = input[0].encode('utf-8')
    index = 0
    password = ""
    while len(password) < 10:
        hash = hashlib.md5(door + str(index).encode('utf-8')).hexdigest()
        if hash[:5] == "00000":
            print(password)
            password += hash[5]
        index += 1
    return password

def part2(input):
    door = input[0].encode('utf-8')
    index = 0
    count = 0
    password = ['.']*8
    while count < 8:
        hash = hashlib.md5(door + str(index).encode('utf-8')).hexdigest()
        if hash[:5] == "00000":
            location = int(hash[5], 16)
            if location <= 7 and password[int(hash[5])] == '.':
                password[location] = hash[6]
                count += 1
        index += 1

    return "".join(password)

if __name__ == "__main__":
    sys.exit(main())
