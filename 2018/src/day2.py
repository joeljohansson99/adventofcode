import os
import sys
import string

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day2.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
	two_count = 0
	three_count = 0

	for line in input:
		count = set()
		for letter in string.ascii_lowercase:
			count.add(line.count(letter))
		if 2 in count:
			two_count += 1
		if 3 in count:
			three_count += 1
		
	return two_count * three_count

def part2(input):
	for i in range(0, len(input)):
		for j in range(i+1, len(input)):
			diff = -1
			for k in range(0,len(input[i])):
				if input[i][k] != input[j][k]:
					if diff != -1:
						diff = -1
						break
					diff = k
			if diff != -1:
				return input[i][:diff] + input[i][diff+1:]

if __name__ == "__main__":
    sys.exit(main())