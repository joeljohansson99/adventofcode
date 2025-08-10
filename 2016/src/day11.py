from itertools import combinations
from collections import deque
import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    element_ids = {}
    pattern = re.compile(r'a (\w+)(?:-compatible)? (microchip|generator)')
    for floor, line in enumerate(input):
        matches = pattern.findall(line)
        for element, type_ in matches:
            if element not in element_ids:
                element_ids[element] = [None, None]  # G, M
            if type_ == "generator":
                element_ids[element][0] = floor
            else:
                element_ids[element][1] = floor

    state = (0, tuple(tuple(v) for v in element_ids.values()))
    
    return solve(state)

def part2(input):
    element_ids = {}
    pattern = re.compile(r'a (\w+)(?:-compatible)? (microchip|generator)')
    for floor, line in enumerate(input):
        matches = pattern.findall(line)
        for element, type in matches:
            if element not in element_ids:
                element_ids[element] = [None, None]  # G, M
            if type == "generator":
                element_ids[element][0] = floor
            else:
                element_ids[element][1] = floor

    element_ids['elerium'] = [0,0]
    element_ids['dilithium'] = [0,0]

    state = (0, tuple(tuple(v) for v in element_ids.values()))
    
    return solve(state)

def is_valid(state):
    _, items = state
    for floor in range(4):
        generators = {i for i, (g, _) in enumerate(items) if g == floor}
        microchips = {i for i, (_, m) in enumerate(items) if m == floor}
        if generators and any(m not in generators for m in microchips):
            return False
    return True

def serialize(state):
    elevator, items = state
    items = tuple(sorted(items))
    return (elevator, items)

def get_possible_moves(items_on_floor):
    return list(combinations(items_on_floor, 1)) + list(combinations(items_on_floor, 2))

def solve(initial_state):
    queue = deque([(initial_state, 0)])
    seen = set()
    seen.add(serialize(initial_state))

    while queue:
        (elevator, items), steps = queue.popleft()

        if all(g == 3 and m == 3 for g, m in items):
            return steps

        items = list(items)
        items_on_floor = [i for i in range(len(items) * 2) if (items[i // 2][i % 2] == elevator)]
        moves = get_possible_moves(items_on_floor)

        for direction in [-1, 1]:
            new_floor = elevator + direction
            if not (0 <= new_floor < 4):
                continue

            for move in moves:
                new_items = [list(x) for x in items]

                for idx in move:
                    item_index = idx // 2
                    is_generator = (idx % 2 == 0)
                    if is_generator:
                        new_items[item_index][0] = new_floor
                    else:
                        new_items[item_index][1] = new_floor

                new_state = (new_floor, tuple(map(tuple, new_items)))
                if is_valid(new_state):
                    ser = serialize(new_state)
                    if ser not in seen:
                        seen.add(ser)
                        queue.append((new_state, steps + 1))

if __name__ == "__main__":
    sys.exit(main())