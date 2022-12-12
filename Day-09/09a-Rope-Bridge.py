#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Rope Bridge a
"""

import numpy as np
from pathlib import Path
import string


class Mover:
    def __init__(self, start):
        self.pos = start


if __name__ == '__main__':
    data_folder = Path("data/")
    puzzle_input = data_folder / "input.txt"

    input_list = []

    with open(puzzle_input) as f:
        for line in f:
            chars = line.strip().split(' ')
            chars[1] = int(chars[1])
            input_list.append(chars)

    print(input_list)
    n = 600
    grid = np.chararray((n, n), unicode=True)
    # grid = np.random.choice(list(string.ascii_lowercase),  size=(n,n))
    grid[:] = '.'

    s = [n / 2, n / 2]
    i = s[0] + n * s[1]
    H = Mover(start=s)
    T = Mover(start=s)
    np.put(grid, i, '$')
    k_old = i
    print(np.array2string(grid, separator=' ', formatter={'str_kind': lambda x: x}))
    history_visited = set()
    history_visited2 = []
    for instr in input_list:
        # print('------------')

        for j in range(instr[1]):
            # print(instr)
            pos_old = H.pos.copy()
            if instr[0] == 'L':
                H.pos[0] -= 1
            elif instr[0] == 'R':
                H.pos[0] += 1
            elif instr[0] == 'U':
                H.pos[1] -= 1
            elif instr[0] == 'D':
                H.pos[1] += 1
            i = H.pos[0] + n * H.pos[1]
            # if list(grid.flat)[int(i)] == 'T':
            #     adjacent.append('T')
            i_old = np.take(grid, i)
            np.put(grid, i, 'H')
            x = int(i % n)  # Row
            y = int(i / n)  # Column
            # print(x)
            rowU = grid[y - 1]
            row = grid[y]
            rowD = grid[y + 1]
            adjacent = [rowU[x - 1], rowU[x], rowU[x+1], row[x - 1], row[x], row[x+1], rowD[x - 1], rowD[x], rowD[x+1]]
            if i_old == 'T':
                adjacent.append(i_old)
            # print('adjacent: ', adjacent)
            if not ('T' in adjacent):
                np.put(grid, k_old, '#')
                # print('now!')
                k = pos_old[0] + n * pos_old[1]
                np.put(grid, k, 'T')
                history_visited.add(k)
                history_visited2.append(k)
                k_old = k
            # print(np.array2string(grid, separator=' ', formatter={'str_kind': lambda x: x}))
            # print(count_visited)

        # print(np.array2string(grid, separator=' ', formatter={'str_kind': lambda x: x}))

    count_h = 0
    print(grid.flat)
    for h in grid.flat:
        if h == '#':
            count_h += 1
    print(len(history_visited))
    print(len(set(history_visited2)))
    print(count_h)
    # 5154 too low
    # 6593 too high
    # 6592 too high
    # 6591 too high
    # 6341 ?
    # 6343 ?
