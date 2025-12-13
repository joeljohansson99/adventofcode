from collections import defaultdict
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day4.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    nums = aoc.ints(input[0])
    boards = list()
    board = list()
    for line in input[2:]:
        if line == "":
            boards.append(board)
            board = list()
        else:
            board.append(aoc.ints(line))
    if board:
        boards.append(board)

    for i in range(len(nums)):
        drawn = nums[:i+1]
        for board in boards:
            for row in board:
                if all([n in drawn for n in row]):
                    return sum([sum([n for n in row if n not in drawn]) for row in board]) * drawn[-1]
            for r in range(len(board)):
                col = [row[r] for row in board]
                if all([n in drawn for n in col]):
                    return sum([sum([n for n in row if n not in drawn]) for row in board]) * drawn[-1]
                

def part2(input):
    nums = aoc.ints(input[0])
    boards = list()
    board = list()
    for line in input[2:]:
        if line == "":
            boards.append(board)
            board = list()
        else:
            board.append(aoc.ints(line))
    if board:
        boards.append(board)

    bingo = set()
    for i in range(len(nums)):
        drawn = nums[:i+1]
        for i in range(len(boards)):
            if i in bingo:
                continue
            board = boards[i]
            for row in board:
                if all([n in drawn for n in row]):
                    bingo.add(i)
                    if len(bingo) == len(boards):
                        return sum([sum([n for n in row if n not in drawn]) for row in board]) * drawn[-1]
            for r in range(len(board)):
                col = [row[r] for row in board]
                if all([n in drawn for n in col]):
                    bingo.add(i)
                    if len(bingo) == len(boards):
                        return sum([sum([n for n in row if n not in drawn]) for row in board]) * drawn[-1]

if __name__ == "__main__":
    sys.exit(main())