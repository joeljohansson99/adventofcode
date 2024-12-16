import sys
import os
import re
from collections import deque

def main():

    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day19.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    bps = []
    for line in input:
        (_, ore1, ore2, ore3, clay1, ore4, obs1) = list(map(int, re.findall(r'\d+', line)))
        ore_cost = (ore1, 0, 0)
        clay_cost = (ore2, 0, 0)
        obs_cost = (ore3, clay1, 0)
        geo_cost = (ore4, 0, obs1)
        bps.append(dict())
        bps[len(bps)-1]["ore"] = ore_cost
        bps[len(bps)-1]["clay"] = clay_cost
        bps[len(bps)-1]["obs"] = obs_cost
        bps[len(bps)-1]["geo"] = geo_cost
    
    sum = 0 
    for i, bp in enumerate(bps):
        sum += collect(bp, 24) * (i+1)
    return sum
       
def part2(input):
    bps = []
    for line in input:
        (_, ore1, ore2, ore3, clay1, ore4, obs1) = list(map(int, re.findall(r'\d+', line)))
        ore_cost = (ore1, 0, 0)
        clay_cost = (ore2, 0, 0)
        obs_cost = (ore3, clay1, 0)
        geo_cost = (ore4, 0, obs1)
        bps.append(dict())
        bps[len(bps)-1]["ore"] = ore_cost
        bps[len(bps)-1]["clay"] = clay_cost
        bps[len(bps)-1]["obs"] = obs_cost
        bps[len(bps)-1]["geo"] = geo_cost
    
    sum = 1
    for bp in bps[:3]:
        sum *= collect(bp, 32)
    return sum

def collect(bp, T):
    
    # (ore, clay, obs, geo, r_ore, r_clay, r_obs, r_geo, min)
    Q = deque([(0, 0, 0, 0, 1, 0, 0, 0, T)])
    seen = set()
    best = 0
    
    m_ore = max(bp["ore"][0], bp["clay"][0], bp["obs"][0], bp["geo"][0])
    m_clay = max(bp["ore"][1], bp["clay"][1], bp["obs"][1], bp["geo"][1])
    m_obs = max(bp["ore"][2], bp["clay"][2], bp["obs"][2], bp["geo"][2])
    
    while Q:
        state = Q.popleft()
        (ore, clay, obs, geo, r_ore, r_clay, r_obs, r_geo, min) = state
        
        best = max(best, geo)
        
        if min == 0:
            continue
        
        if state in seen:
            continue
        seen.add(state)
        
        if min==0 or min * geo + max((min - 2) * (min - 1) / 2, 0) < best:
            continue
        
        if ore > bp["geo"][0] and obs >= bp["geo"][2]:
            Q.append((ore + r_ore - bp["geo"][0], 
                    clay + r_clay, 
                    obs + r_obs - bp["geo"][2], 
                    geo + r_geo, 
                    r_ore, r_clay, r_obs, r_geo+1, min-1))
            continue

        Q.append((ore + r_ore, 
                clay + r_clay, 
                obs + r_obs, 
                geo + r_geo, 
                r_ore, r_clay, r_obs, r_geo, min-1))
        
        if r_ore < m_ore and ore >= bp["ore"][0]:
            Q.append((ore + r_ore - bp["ore"][0], 
                    clay + r_clay, 
                    obs + r_obs, 
                    geo + r_geo, 
                    r_ore+1, r_clay, r_obs, r_geo, min-1))
            
        if r_clay < m_clay and ore >= bp["clay"][0]:
            Q.append((ore + r_ore - bp["clay"][0], 
                    clay + r_clay, 
                    obs + r_obs, 
                    geo + r_geo, 
                    r_ore, r_clay+1, r_obs, r_geo, min-1))
            
        if r_obs < m_obs and ore >= bp["obs"][0] and clay >= bp["obs"][1]:
            Q.append((ore + r_ore - bp["obs"][0], 
                    clay + r_clay - bp["obs"][1], 
                    obs + r_obs, 
                    geo + r_geo, 
                    r_ore, r_clay, r_obs+1, r_geo, min-1))
    
    return best
 
if __name__ == "__main__":
    sys.exit(main())