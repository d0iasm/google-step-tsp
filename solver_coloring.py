#!/usr/bin/env python3

import sys
import math
from operator import itemgetter

from common import print_solution, read_input


def divide(cities):
    N = len(cities)
    middle = int(N/2)
        
    cities = sorted(cities, key=itemgetter(0))
    cities1 = cities[:middle]
    cities2 = cities[middle:]

    return merge(cities1, cities2)


def merge(cities1, cities2):
    cities1 = sorted(cities1, key=lambda x: sum(x))
    cities2 = sorted(cities2, key=lambda x: sum(x))

    return cities1 + cities2[::-1]


def solve(cities):
    N = len(cities)
    index = [i for i in range(N)]
    index_cities = dict(zip(cities, index))
    sorted_cities = divide(cities)
    
    solution = []
    for city in sorted_cities:
        solution.append(index_cities[city])
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
