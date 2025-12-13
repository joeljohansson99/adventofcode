import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day8.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for line in input:
        _, output = line.split("|")
        output = output.strip().split(" ")
        count += len([o for o in output if len(o) in [2,3,4,7]])
    return count

def part2(input):
    total = 0
    for line in input:
        nums = dict()
        inp, out = line.split("|")
        inp = inp.strip().split(" ")
        out = out.strip().split(" ")
        inp = [[c for c in i] for i in inp]

        nums[1] = [i for i in inp if len(i) == 2][0]
        nums[4] = [i for i in inp if len(i) == 4][0]
        nums[7] = [i for i in inp if len(i) == 3][0]
        nums[8] = [i for i in inp if len(i) == 7][0]
        for i in inp:
            if len(i) == 6: 
                if all(n in i for n in nums[4]):
                    nums[9] = i
                elif all(n in i for n in nums[1]):
                    nums[0] = i
                else:
                    nums[6] = i
        for i in inp:
            if len(i) == 5:
                if all(n in i for n in nums[1]):
                    nums[3] = i
                elif all(n in nums[6] for n in i):
                    nums[5] = i
                else:
                    nums[2] = i
        nums = {(k, "".join(n)) for k,n in nums.items()}
        val = 0
        for o in out:
            val*=10
            val += [k for (k,v) in nums if sorted(v) == sorted(o)][0]
        total+=val
    return total

if __name__ == "__main__":
    sys.exit(main())