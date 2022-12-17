import sys
from copy import copy

def main():
    input = dict()
    with open('input/day16.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","").replace("Valve ", "").replace(" has flow rate=", ":").replace("; tunnels lead to valves ", ":").replace("; tunnel leads to valve ", ":")
            [valve, rate, connections] = l.split(":")
            rate = int(rate)
            connections = connections.split(", ")
            input[valve] = Valve(rate, connections)
    # print([k + " : " + str(v) for (k,v) in input.items()])
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    dist = dict()
    for (n,_) in input.items():

        d = {v:30 for (v,_) in input.items()}
        d[n] = 0

        set_dist(d, input, n)

        dist[n] = d
    
    dist = {k:v for (k,v) in dist.items() if input[k].getRate() > 0 or k == "AA"}
    for (k, v) in dist.items():
        dist[k] = {x:y for (x,y) in v.items() if input[x].getRate() > 0 and x != k}

    return calc_flow(input, dist, "AA", 30, 0)

def part2(input):
    dist = dict()
    for (n,_) in input.items():

        d = {v:30 for (v,_) in input.items()}
        d[n] = 0

        set_dist(d, input, n)

        dist[n] = d
    
    dist = {k:v for (k,v) in dist.items() if input[k].getRate() > 0 or k == "AA"}
    for (k, v) in dist.items():
        dist[k] = {x:y for (x,y) in v.items() if input[x].getRate() > 0 and x != k}

    return calc_flow_with_elephant(input, dist, "AA","AA",26, 26, 0)

def calc_flow_with_elephant(graph, dist, n1, n2, minutes1, minutes2, rate):
    t1 = False
    t2 = False
    if minutes1 < 1 and minutes2 < 1:
        return rate
    if minutes1 > 0: 
        t1 = True
        rate += graph[n1].getRate() * minutes1
    if minutes2 > 0:    
        t2 = True
        rate += graph[n2].getRate() * minutes2

    rates = [rate]
    if t1 and t2:
        for (valve1,cost1) in dist[n1].items():
            if not graph[valve1].is_open():
                graph[valve1].toggle()
                for (valve2,cost2) in dist[n2].items():
                    if not graph[valve2].is_open():
                        graph[valve2].toggle()
                        rates.append(calc_flow_with_elephant(graph, dist, valve1, valve2, minutes1 - cost1 - 1, minutes2-cost2 - 1, rate))
                        graph[valve2].toggle()
                
                graph[valve1].toggle()

    elif t1:
        for (valve,cost) in dist[n1].items():
            if not graph[valve].is_open():
                graph[valve].toggle()
                rates.append(calc_flow_with_elephant(graph, dist, valve, n2, minutes1 - cost - 1, minutes2, rate))
                graph[valve].toggle()

    elif t2:
        for (valve,cost) in dist[n2].items():
            if not graph[valve].is_open():
                graph[valve].toggle()
                rates.append(calc_flow_with_elephant(graph, dist, n1, valve, minutes1, minutes2 - cost - 1, rate))
                graph[valve].toggle()

    
    return max(rates)

def calc_flow(graph, dist, n, minutes, rate):
    if minutes < 1:
        return rate
        
    rate += graph[n].getRate() * minutes

    rates = [rate]
    for (valve,cost) in dist[n].items():
        if not graph[valve].is_open():
            graph[valve].toggle()
            rates.append(calc_flow(graph, dist, valve, minutes - cost - 1, rate))
            graph[valve].toggle()
    
    return max(rates)

def set_dist(dist, graph, n):
    for v in graph[n].getConnections():
        if dist[v] > dist[n] + 1:
            dist[v] = dist[n] + 1
            set_dist(dist,graph,v)
    
class Valve():
    def __init__(self, rate, connections):
        self.rate = rate
        self.connections = connections
        self.open = False
    
    def getRate(self):
        return self.rate
    
    def getConnections(self):
        return self.connections
    
    def is_open(self):
        return self.open
    
    def toggle(self):
        self.open = not self.open

    def __str__(self):
        return "Rate: " + str(self.rate) + ", Connections: " + str(self.connections)

if __name__ == "__main__":
    sys.exit(main())