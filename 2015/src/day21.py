import os
import sys
import utils.aoc as aoc
import itertools

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day21.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

WEAPONS = {
    "Dagger":     (8,4,0),
    "Shortsword": (10,5,0),
    "Warhammer":  (25,6,0),
    "Longsword":  (40,7,0),
    "Greataxe":   (74,8,0)
}

ARMOR = {
    "Leather":     (13,0,1),
    "Chainmail":   (31,0,2),
    "Splintmail":  (53,0,3),
    "Bandedmail":  (75,0,4),
    "Platemail":   (102,0,5)
}

RINGS = {
    "Damage +1":  (25,1,0),
    "Damage +2":  (50,2,0),
    "Damage +3":  (100,3,0),
    "Defense +1": (20,0,1),
    "Defense +2": (40,0,2),
    "Defense +3": (80,0,3)
}

def part1(input):
    [boss_hitpoints] = aoc.ints(input[0])
    [boss_damage] = aoc.ints(input[1])
    [boss_armor] = aoc.ints(input[2])

    options = [itertools.chain([''], lst) for lst in [WEAPONS.values(), ARMOR.values(), RINGS.values(), RINGS.values()]]
    combinations = []
    for combo in itertools.product(*options):
        result = [x for x in combo if x != '']
        if result and len(set(result)) == len(result) and any([w in WEAPONS.values() for w in result]):
            combinations.append(tuple(map(sum, zip(*result))))
    
    combinations = sorted(combinations, key=lambda x: x[0])
    
    for (g,d,a) in combinations:
        my_hp = 100
        boss_hp = boss_hitpoints
        my_dmg = max(d - boss_armor, 1)
        boss_dmg = max(boss_damage - a, 1)
        turn = True
        while my_hp > 0 and boss_hp > 0:
            if turn:
                boss_hp -= my_dmg
            else:
                my_hp -= boss_dmg
            turn = not turn
        if my_hp > 0:
            return g

def part2(input):
    [boss_hitpoints] = aoc.ints(input[0])
    [boss_damage] = aoc.ints(input[1])
    [boss_armor] = aoc.ints(input[2])

    options = [itertools.chain([''], lst) for lst in [WEAPONS.values(), ARMOR.values(), RINGS.values(), RINGS.values()]]
    combinations = []
    for combo in itertools.product(*options):
        result = [x for x in combo if x != '']
        if result and len(set(result)) == len(result) and any([w in WEAPONS.values() for w in result]):
            combinations.append(tuple(map(sum, zip(*result))))
    
    combinations = sorted(combinations, key=lambda x: x[0], reverse=True)
    
    for (g,d,a) in combinations:
        my_hp = 100
        boss_hp = boss_hitpoints
        my_dmg = max(d - boss_armor, 1)
        boss_dmg = max(boss_damage - a, 1)
        turn = True
        while my_hp > 0 and boss_hp > 0:
            if turn:
                boss_hp -= my_dmg
            else:
                my_hp -= boss_dmg
            turn = not turn
        if my_hp <= 0:
            return g

if __name__ == "__main__":
    sys.exit(main())
