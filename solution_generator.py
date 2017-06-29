#!/usr/bin/env python3

import sys
import math

from common import format_solution, read_input, read_solution

import solver_greedy
import solver_random
import solver_divide_and_conquer
import solver_divide_greedy
import solver_divide_greedy2
import solver_divide_and_sort
import solver_optimize

CHALLENGES = 7

def generate_sample_solutions():
    # solvers = ((solver_random, 'random'),
            #    (solver_greedy, 'greedy'))
    solvers = ((solver_optimize, 'yours'),)
    for challenge_number in range(CHALLENGES):
        cities = read_input('input/{}.csv'.format(challenge_number))
        other_solution = read_solution('solution_yours/divide_greedy2/{}.csv'.format(challenge_number))
        for solver, solver_name in solvers:
            #solution = solver.solve(cities)
            solution = solver.solve(cities, other_solution)
            with open('solution_{}/{}.csv'.format(solver_name, challenge_number), 'w') as f:
                f.write(format_solution(solution) + '\n')


if __name__ == '__main__':
    generate_sample_solutions()
