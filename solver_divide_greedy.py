#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def is_x_longer(cities):
    x1 = min(map(lambda x: x[0], cities))
    y1 = min(map(lambda x: x[1], cities))
    x2 = max(map(lambda x: x[0], cities))
    y2 = max(map(lambda x: x[1], cities))
    return x2 - x1 > y2 - y1


def divide(cities):
    N = len(cities)
    if N <= 3:
        return cities

    middle = int(N/2)
    if is_x_longer(cities):
        cities = sorted(cities, key=lambda x: x[0])
    else:
        cities = sorted(cities, key=lambda x: x[1])
    cities1 = cities[:middle]
    cities2 = cities[middle:]

    return cities1, cities2


def greedy(cities, dist, index_cities):
    unvisited_cities = []
    for city in cities:
        unvisited_cities.append(index_cities[city])
    current_city = unvisited_cities.pop(0)
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return solution


def merge(cities1, cities2):
    assert cities1 is not None, "error cities1 is None"
    assert cities2 is not None, "error cities2 is None"

    return cities1 + cities2

    
def solve(cities):
    N = len(cities)
    index = [i for i in range(N)]
    index_cities = dict(zip(cities, index))

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    cities1, cities2 = divide(cities)
    cities1_solution = greedy(cities1, dist, index_cities)
    cities2_solution = greedy(cities2, dist, index_cities)
    solution = merge(cities1_solution, cities2_solution)
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
