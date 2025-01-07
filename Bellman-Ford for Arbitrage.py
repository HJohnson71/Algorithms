# Application of the Bellman-Ford algorithm to identify arbitrage opportunities in currency markets

import math

def detect_negative_cycle(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    distance[start] = 0
    previous = [-1] * n    
    for i in range(n - 1):
        for k in range(n):
            for j in range(n):
                if distance[k] + graph[k][j] < distance[j]:
                    distance[j] = distance[k] + graph[k][j]
                    previous[j] = k
    for i in range(n):
        for k in range(n):
            if distance[i] + graph[i][k] < distance[k]:
                node = k
                cycle = [node]
                while previous[node] != k:
                    node = previous[node]
                    cycle.append(node)
                cycle.append(k)
                return cycle[::-1]
    return None

def calculate_profit(graph, path):
    profit = 1
    for i in range(len(path) - 1):
        profit *= math.exp(-graph[path[i]][path[i + 1]])
    return (profit - 1) * 100

def arbitrage(currency):
    n = len(currency)
    lnrates = [[-math.log(rate) for rate in row] for row in currency]
    path = detect_negative_cycle(lnrates, 0)
    if path:
        profit = calculate_profit(lnrates, path)
        print("Arbitrage opportunity found:")
        print("Arbitrage Path:")
        print(' -> '.join(map(str, path)))
        print("Arbitrage Profit Percentage")
        return profit
    else:
        print("No arbitrage opportunity found")
        
#Test:

currency = [ [ 1, 49, 1/(0.0107) ],
[ 1/49, 1, 2 ],
[ 0.0107, 0.5, 1 ] ]
print(arbitrage(currency))
