#!/usr/bin/env python3

import sys
import math
from operator import itemgetter

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def divide(cities):
    cities1 = []
    cities2 = []
    max_point = cities[0]
    for city in cities:
        if sum(city) > sum(max_point):
            max_point = city

    diagonal = max_point[1] / max_point[0]
    for city in cities:
        if city[1] > city[0] * diagonal:
            cities1.append(city)
        else:
            cities2.append(city)
            
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
