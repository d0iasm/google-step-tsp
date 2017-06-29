#!/usr/bin/env python3

import sys
import math
from operator import itemgetter

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
    divide = [cities]
    while N > 3:
        cities = max(divide, key=lambda x: len(x))
        max_index = divide.index(cities)
        N = len(cities)
        middle = int(N/2)
        if N <= 3: break
        
        if is_x_longer(cities):
            cities = sorted(cities, key=itemgetter(0))
        else:
            cities = sorted(cities, key=itemgetter(1))
        divide.append(cities[:middle])
        divide.append(cities[middle:])
        divide.pop(max_index)

    return divide


def merge(divide):
    N = len(divide)
    middle = int(N/2)
    # TODO: divideをどこで区切るか!
    #print(divide)
    #divide = sorted(divide, key=lambda x: (x[0],x[1]))
    #print(divide)
    divide1 = divide[:middle]
    divide2 = divide[middle:]
    #print(divide1)
    #print("---")
    #print(divide2)
    #print("===")
    
    
    d1 = distance(cities1[0], cities2[0])
    d2 = distance(cities1[0], cities2[-1])
    d3 = distance(cities1[-1], cities2[0])
    d4 = distance(cities1[-1], cities2[-1])

    d = min(d1, d2, d3, d4)

    if d1 == d:
        return list(reversed(cities1)) + cities2
    elif d2 == d:
        return cities2 + cities1
    elif d3 == d:
        return cities1 + cities2
    elif d4 == d:
        return cities1 + list(reversed(cities2))
    

def solve(cities):
    N = len(cities)
    index = [i for i in range(N)]
    index_cities = dict(zip(cities, index))
    divide_cities = divide(cities)
    sorted_cities = merge(divide_cities)

    solution = []
    #for city in sorted_cities:
    #    solution.append(index_cities[city])
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
