import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day15.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    words = input[0].split(",")
    sum = 0
    for word in words:
        codes = [ord(x) for x in word]
        val = 0
        for c in codes:
            val += c
            val *= 17
            val = val % 256
        sum += val
    return sum

def part2(input):
    words = input[0].split(",")
    sum = 0
    hashmap = dict()
    for i in range(0,256):
        hashmap[i] = []

    for word in words:
        if '=' in word:
            (w, b) = word.split("=")
            codes = [ord(x) for x in w]
            b = int(b)
            val = 0
            for c in codes:
                val += c
                val *= 17
                val = val % 256
            exist = False
            for i in range(0,len(hashmap[val])):
                if hashmap[val][i][0] == w:
                    hashmap[val][i] = (w,b)
                    exist = True
                    break
            if not exist:
                hashmap[val].append((w,b))

        else:
            w = word.replace("-","")
            codes = [ord(x) for x in w]
            val = 0
            for c in codes:
                val += c
                val *= 17
                val = val % 256

            rem = 0
            for box in hashmap[val]:
                if box[0] == w:
                    rem = box
                    break
            if rem != 0:
                hashmap[val].remove(rem)

    for i in range(0,256):
        for k in range(0, len(hashmap[i])):
            sum += (i+1) * (k+1) * hashmap[i][k][1]

    return sum


if __name__ == "__main__":
    sys.exit(main())