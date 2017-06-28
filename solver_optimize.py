#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def opt_2(solution, dist):
    N = len(solution)
    print(solution)
    for i, current in enumerate(solution[:(N-1)]):
        # print("current:{}, current+1:{}".format(current, solution[i+1]))
        best_distance = dist[current][solution[i+1]]
        print("{}".format(best_distance))
        for to in solution[(i+1):]:
        # for to in range(i+1, N):
            print("{}, {} : dist{}".format(current, to, dist[current][to]))
            new_distance = dist[current][to]
            if new_distance < best_distance:
                temp = solution[current]
                solution[current] = solution[to]
                solution[to] = temp
                best_distance = new_distance
                print("swap! c:{}, to:{}".format(current,solution[to]))
    return solution

def or_opr():
    pass


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return opt_2(solution, dist)


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
