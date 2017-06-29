#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def minimum_spanning_tree(solution, dist):
    min_cost = [0] * len(solution)
    used = [0] * len(solution)

    for v in solution:
        min_cost[v] = float('inf')
        used[v] = False
        
    min_cost[solution[0]] = 0
    total_cost = 0

    while True:
        new = -1
        for v in solution:
            if used[v] == False and (new == -1 or min_cost[v] < min_cost[new]):
                new = v

        if new == -1: break

        used[new] = True
        total_cost += min_cost[new]

        for v in solution:
            min_cost[v] = min(min_cost[v], dist[v][new])

    return total_cost

    
def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    solution = [i for i in range(N)]
    minimum_spanning_tree(solution, dist)
    
    return solution

    
if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
