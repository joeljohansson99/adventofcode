import heapq
import math
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day22.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

SPELLS = {
    'Magic Missile': {'cost': 53, 'damage': 4, 'heal': 0, 'armor': 0, 'duration': 0, 'mana': 0},
    'Drain':         {'cost': 73, 'damage': 2, 'heal': 2, 'armor': 0, 'duration': 0, 'mana': 0},
    'Shield':        {'cost': 113, 'damage': 0, 'heal': 0, 'armor': 7, 'duration': 6, 'mana': 0},
    'Poison':        {'cost': 173, 'damage': 3, 'heal': 0, 'armor': 0, 'duration': 6, 'mana': 0},
    'Recharge':      {'cost': 229, 'damage': 0, 'heal': 0, 'armor': 0, 'duration': 5, 'mana': 101},
}

PLAYER_HP = 50
PLAYER_MANA = 500

def part1(input):
    BOSS_HP = aoc.ints(input[0])[0]
    BOSS_DMG = aoc.ints(input[1])[0]

    heap = [(0, True, PLAYER_HP, PLAYER_MANA, BOSS_HP, {})]
    best_win = math.inf

    while heap:
        (spent, turn, php, pmana, bhp, effects) = heap.pop()
        if spent >= best_win:
            continue

        armor = 0
        for spell, timer in list(effects.items()):
            bhp -= SPELLS[spell]['damage']
            pmana += SPELLS[spell]['mana']
            armor += SPELLS[spell]['armor']
            if timer - 1 > 0:
                effects[spell] = timer - 1
            else:
                del effects[spell]
        
        if bhp <= 0:
            if best_win > spent:
                best_win = spent
            continue

        if turn:
            for spell, info in SPELLS.items():
                if info['cost'] > pmana or spell in effects:
                    continue
                new_spent = spent + info['cost']
                new_pmana = pmana - info['cost']
                new_bhp = bhp
                new_php = php
                if new_spent >= best_win:
                    continue
                new_effects = dict(effects)
                if info['duration'] > 0:
                    new_effects[spell] = info['duration']
                else:
                    new_bhp -= info['damage']
                    new_php += info['heal']
                if new_bhp <= 0:
                    if best_win > spent:
                        best_win = spent
                    continue
                heap.append((new_spent, not turn, new_php, new_pmana, new_bhp, new_effects))
        else:
            dmg = max(BOSS_DMG - armor, 1)
            php -= dmg
            if php <= 0:
                continue
            heap.append((spent, not turn, php, pmana, bhp, effects))
    return best_win

def part2(input):
    BOSS_HP = aoc.ints(input[0])[0]
    BOSS_DMG = aoc.ints(input[1])[0]

    heap = [(0, True, PLAYER_HP, PLAYER_MANA, BOSS_HP, {})]
    best_win = math.inf

    while heap:
        (spent, turn, php, pmana, bhp, effects) = heap.pop()
        if spent >= best_win:
            continue

        armor = 0
        for spell, timer in list(effects.items()):
            bhp -= SPELLS[spell]['damage']
            pmana += SPELLS[spell]['mana']
            armor += SPELLS[spell]['armor']
            if timer - 1 > 0:
                effects[spell] = timer - 1
            else:
                del effects[spell]
        
        if bhp <= 0:
            if best_win > spent:
                best_win = spent
            continue

        if turn:
            php -= 1
            for spell, info in SPELLS.items():
                if info['cost'] > pmana or spell in effects:
                    continue
                new_spent = spent + info['cost']
                new_pmana = pmana - info['cost']
                new_bhp = bhp
                new_php = php
                if new_spent >= best_win:
                    continue
                new_effects = dict(effects)
                if info['duration'] > 0:
                    new_effects[spell] = info['duration']
                else:
                    new_bhp -= info['damage']
                    new_php += info['heal']
                if new_bhp <= 0:
                    if best_win > spent:
                        best_win = spent
                    continue
                heap.append((new_spent, not turn, new_php, new_pmana, new_bhp, new_effects))
        else:
            dmg = max(BOSS_DMG - armor, 1)
            php -= dmg
            if php <= 0:
                continue
            heap.append((spent, not turn, php, pmana, bhp, effects))
    return best_win

if __name__ == "__main__":
    sys.exit(main())
