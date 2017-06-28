#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input, read_solution


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def opt_2(N, path, dist):
    total = 0
    while True:
        count = 0
        for i in range(N - 2):
            i1 = i + 1
            for j in range(i + 2, N):
                if j == N - 1:
                    j1 = 0
                else:
                    j1 = j + 1
                if i != 0 or j1 != 0:
                    l1 = dist[path[i]][path[i1]]
                    l2 = dist[path[j]][path[j1]]
                    l3 = dist[path[i]][path[j]]
                    l4 = dist[path[i1]][path[j1]]
                    if l1 + l2 > l3 + l4:
                        new_path = path[i1:j+1]
                        path[i1:j+1] = new_path[::-1]
                        count += 1
        total += count
        if count == 0: break
    return path, total


def or_opt(N, path, dist):
    total = 0
    while True:
        count = 0
        for i in range(N):
            i0 = i - 1
            i1 = i + 1
            if i0 < 0: i0 = N - 1
            if i1 == N: i1 = 0
            for j in range(N):
                j1 = j + 1
                if j1 == N: j1 = 0
                if j != i and j1 != i:
                    l1 = dist[path[i0]][path[i]]
                    l2 = dist[path[i]][path[i1]]
                    l3 = dist[path[j]][path[j1]]
                    l4 = dist[path[i0]][path[i1]]
                    l5 = dist[path[j]][path[i]]
                    l6 = dist[path[i]][path[j1]]
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        p = path[i]
                        path[i:i + 1] = []
                        if i < j:
                            path[j:j] = [p]
                        else:
                            path[j1:j1] = [p]
                        count += 1
        total += 0
        if count == 0: break
    return path, total


def solve(cities, solution=None):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    if solution is None:
        solution = [i for i in range(N)]
    while True:
        solution, _ = opt_2(N, solution, dist)
        solution, flag = or_opt(N, solution, dist)
        if flag == 0: return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    if len(sys.argv) == 2:
        solution = solve(read_input(sys.argv[1]))
        print_solution(solution)
    elif len(sys.argv) == 3:
        solution = solve(read_input(sys.argv[1]), read_solution(sys.argv[2]))
        print_solution(solution)
