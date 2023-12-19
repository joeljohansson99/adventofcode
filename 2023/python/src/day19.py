import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day19.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    parts = []
    flows = dict()
    parse_part = False
    for line in input:
        if parse_part:
            vars = line[1:-1].split(",")
            part = dict()
            for v in vars:
                (var, val) = v.split("=")
                part[var] = int(val)
            parts.append(part)
        elif line != "":
            name, conds = line.split("{")
            conds = conds[:-1].split(",")
            flows[name] = conds
        else:
            parse_part = True 
    ret = 0
    for part in parts:
        flow = "in"
        while (flow != "A" and flow != "R"):
            conds = flows[flow]
            for cond in conds:
                if ":" not in cond:
                    flow = cond
                    break
                var = cond[0:1]
                op = cond[1:2]
                (val,next) = cond[2:].split(":")
                val = int(val)
                if op == ">":
                    if part[var] > val:
                        flow = next
                        break
                if op == "<":
                    if part[var] < val:
                        flow = next
                        break
        if flow == "A":
            for key,val in part.items():
                ret += val
    
    return ret
    
def part2(input):
    flows = dict()
    for line in input:
        if line != "":
            name, conds = line.split("{")
            conds = conds[:-1].split(",")
            flows[name] = conds
        else:
            break
  
    accept = dict()
    accept["x"] = (1,4000)
    accept["m"] = (1,4000)
    accept["a"] = (1,4000)
    accept["s"] = (1,4000)
    
    accepted = rec("in", flows, accept)
    
    ret = 0
    for accept in accepted:
        ways = 1
        for var in ["x","m","a","s"]:
            ways *= accept[var][1] - accept[var][0] + 1
        ret += ways
    
    return ret


def rec(flow, flows, accept):
    if flow == "R":
        return []
    elif flow == "A":
        return [accept]
    
    conds = flows[flow]
    ret = []
    for cond in conds:
        if ":" not in cond:
            ret.extend(rec(cond, flows, accept))
            break
        var = cond[0:1]
        op = cond[1:2]
        (val,next) = cond[2:].split(":")
        val = int(val)
        if accept[var][0] < val and accept[var][1] > val:
            if op == ">":
                    new = dict(accept)
                    new[var] = (val+1, accept[var][1])
                    ret.extend(rec(next, flows, new))
                    accept[var] = (accept[var][0], val)
            if op == "<":
                    new = dict(accept)
                    new[var] = (accept[var][0], val-1)
                    ret.extend(rec(next, flows, new))
                    accept[var] = (val, accept[var][1])
    
    return ret
if __name__ == "__main__":
    sys.exit(main())