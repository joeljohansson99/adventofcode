import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day20.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    N = int(input[0]) // 10
    for i in range(1, N):
        if sum(getDivs(i)) >= N:
            return i

def part2(input):
    N = int(input[0]) // 11
    for i in range(1, N):
        if sum([d for d in getDivs(i) if i <= 50*d]) >= N:
            return i

def getDivs(N):
    factors = {1}
    maxP  = int(N**0.5)
    p,inc = 2,1
    while p <= maxP:
        while N%p==0:
            factors.update([f*p for f in factors])
            N //= p
            maxP = int(N**0.5)
        p,inc = p+inc,2
    if N>1:
        factors.update([f*N for f in factors])
    return sorted(factors)


if __name__ == "__main__":
    sys.exit(main())
