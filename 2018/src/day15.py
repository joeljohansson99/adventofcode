import os
import sys
import heapq

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day15.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

HITPOINTS = 200
ATTACK = 3
ELF = True 
GOBLIN = False

def part1(input):
    walls = set()
    map = dict()
    units = []
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c] == "#":
                walls.add((r,c))
            if input[r][c] == "G":
                heapq.heappush(units, (r,c,GOBLIN))
                map[(r,c)] = (GOBLIN, HITPOINTS)
            if input[r][c] == "E":
                heapq.heappush(units, (r,c,ELF))
                map[(r,c)] = (ELF, HITPOINTS)

    rounds = 0
    done = False

    while not done:
        next_units = []
        while len(units) != 0:
            heapq.heapify(units)
            unit = heapq.heappop(units)
            enemies = get_enemies(map, unit[2])
            if len(enemies) == 0:
                done = True
                break
            friends = get_enemies(map, not unit[2])
            reachable = get_reachable(unit[0], unit[1], walls, friends)
            if len(reachable) == 0:
                heapq.heappush(next_units, unit)
                continue
            attackable = get_attackable(reachable, enemies)

            if len(attackable) == 0:
                move = get_move(reachable, enemies, walls, friends)
                if move is None:
                    heapq.heappush(next_units, unit)
                    continue
                (r,c) = move
                map[(r,c)] = map[(unit[0],unit[1])]
                del map[(unit[0],unit[1])]
                unit = (r,c,unit[2])
                reachable = get_reachable(r, c, walls, friends)
                attackable = get_attackable(reachable, enemies)
            
            if len(attackable) != 0:
                min_hp = min([map[square][1] for square in attackable])
                lowest = filter(lambda square: map[square][1] == min_hp, attackable)
                chosen = next(lowest)
                map[chosen] = (map[chosen][0],map[chosen][1]-ATTACK)
                if map[chosen][1] <= 0:
                    del map[chosen]
                    dead = (chosen[0],chosen[1],not unit[2])
                    if dead in next_units: 
                        next_units.remove(dead)
                    if dead in units: 
                        units.remove(dead)
                            
            heapq.heappush(next_units, unit)
        
        units = next_units
        if not done:
            rounds += 1
    
    outcome = sum([hp for (_, (_, hp)) in map.items()])
    return outcome * rounds
    
def part2(input):
    damage = 4
    while True:
        died = False
        walls = set()
        map = dict()
        units = []
        for r in range(0, len(input)):
            for c in range(0, len(input[r])):
                if input[r][c] == "#":
                    walls.add((r,c))
                if input[r][c] == "G":
                    heapq.heappush(units, (r,c,GOBLIN))
                    map[(r,c)] = (GOBLIN, HITPOINTS)
                if input[r][c] == "E":
                    heapq.heappush(units, (r,c,ELF))
                    map[(r,c)] = (ELF, HITPOINTS)

        rounds = 0
        done = False
        while not done:
            next_units = []
            while len(units) != 0:
                heapq.heapify(units)
                unit = heapq.heappop(units)
                enemies = get_enemies(map, unit[2])
                if len(enemies) == 0:
                    done = True
                    break
                friends = get_enemies(map, not unit[2])
                reachable = get_reachable(unit[0], unit[1], walls, friends)
                if len(reachable) == 0:
                    heapq.heappush(next_units, unit)
                    continue
                attackable = get_attackable(reachable, enemies)

                if len(attackable) == 0:
                    move = get_move(reachable, enemies, walls, friends)
                    if move is None:
                        heapq.heappush(next_units, unit)
                        continue
                    (r,c) = move
                    map[(r,c)] = map[(unit[0],unit[1])]
                    del map[(unit[0],unit[1])]
                    unit = (r,c,unit[2])
                    reachable = get_reachable(r, c, walls, friends)
                    attackable = get_attackable(reachable, enemies)
                
                if len(attackable) != 0:
                    min_hp = min([map[square][1] for square in attackable])
                    lowest = filter(lambda square: map[square][1] == min_hp, attackable)
                    chosen = next(lowest)
                    if unit[2] == ELF:
                        map[chosen] = (map[chosen][0],map[chosen][1]-damage)
                    else:
                        map[chosen] = (map[chosen][0],map[chosen][1]-ATTACK)
                    if map[chosen][1] <= 0:
                        if map[chosen][0] == ELF:
                            done = True
                            died = True
                        del map[chosen]
                        dead = (chosen[0],chosen[1],not unit[2])
                        if dead in next_units: 
                            next_units.remove(dead)
                        if dead in units: 
                            units.remove(dead)
                                
                heapq.heappush(next_units, unit)
            
            units = next_units
            if not done:
                rounds += 1
    
        if not died:
            outcome = sum([hp for (_, (_, hp)) in map.items()])
            return outcome * rounds
        damage += 1



def get_enemies(map, team):
    enemies = []
    for (square, (race,_)) in map.items():
        if race != team:
            enemies.append(square)
    return enemies

def get_reachable(r,c, walls, friends):
    reachable = []
    for square in [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]:
        if square not in walls and square not in friends:
            reachable.append(square)
    return reachable

def get_move(reachable, enemies, walls, friends):
    squares = []
    for square in reachable:
        steps = get_steps(square, enemies, walls, friends)
        if steps is not None:
            squares.append((square, steps))
    if len(squares) == 0:
        return None
    min_steps = min([steps for (_, steps) in squares])
    closest = next(filter(lambda square: square[1] == min_steps, squares))
    return (closest[0][0],closest[0][1])

def get_steps(square, enemies, walls, friends):
    steps = 0
    current = set()
    visited = set()
    current.add(square)
    visited.add(square)
    while len(current) != 0:
        nexts = set()
        for next in current:
            if next in enemies:
                return steps
            else:
                for n in get_reachable(next[0], next[1], walls, friends):
                    if n not in visited:
                        visited.add(n)
                        nexts.add(n)
        current = nexts
        steps += 1
    return None
                
def get_attackable(reachable, enemies):
    attackable = []
    for square in reachable:
        if square in enemies:
            attackable.append(square)
    return attackable
   

if __name__ == "__main__":
    sys.exit(main())