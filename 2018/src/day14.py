import os
import sys

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day14.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    recipes = "37"
    end = int(input[0])
    fst = 0
    snd = 1
    while len(recipes) < end + 10:
        recipes += str(int(recipes[fst]) + int(recipes[snd]))
        fst = (fst + int(recipes[fst]) + 1) % len(recipes)
        snd = (snd + int(recipes[snd]) + 1) % len(recipes)
    
    return recipes[end:end+10]

def part2(input):
    recipes = "37"
    end = input[0]
    check = recipes.zfill(len(end))
    fst = 0
    snd = 1
    searcing = True
    while searcing:
        added = str(int(recipes[fst]) + int(recipes[snd]))
        for add in added:
            check = check[1:] + add
            recipes += add
            if check == end:
                searcing = False
                break

        fst = (fst + int(recipes[fst]) + 1) % len(recipes)
        snd = (snd + int(recipes[snd]) + 1) % len(recipes)

    return len(recipes)-len(end)


if __name__ == "__main__":
    sys.exit(main())