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


def devide(cities):
    length = len(cities)
    middle = int(length/2)
    if length <= 3:
        print(cities)
        return cities

    if is_x_longer(cities):
        print("xが長い")
        print(sorted(cities, key=lambda x: x[1]))
        devide(cities[:middle])
        devide(cities[middle:])
    else:
        print("yが長い")
        print(sorted(cities, key=lambda x: x[0]))
        devide(cities[:middle])
        devide(cities[middle:])



def solve(cities):
    N = len(cities)
    devide(cities)

    # dist = [[0] * N for i in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    #
    # current_city = 0
    # unvisited_cities = set(range(1, N))
    # solution = [current_city]
    #
    # def distance_from_current_city(to):
    #     return dist[current_city][to]
    #
    # while unvisited_cities:
    #     next_city = min(unvisited_cities, key=distance_from_current_city)
    #     unvisited_cities.remove(next_city)
    #     solution.append(next_city)
    #     current_city = next_city
    # return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    # print_solution(solution)
