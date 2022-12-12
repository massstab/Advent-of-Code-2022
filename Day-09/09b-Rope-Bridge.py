#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Rope Bridge b
"""

import numpy as np
from pathlib import Path


class Mover:
    def __init__(self, start):
        self.pos = start


def move(commands, H, s):
    i = s[0] + n * s[1]
    np.put(grid, i, '$')
    k_old = i
    history_visited = []
    for instr in commands:
        for j in range(instr[1]):
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
            i_old = np.take(grid, i)
            np.put(grid, i, 'H')
            x = int(i % n)  # Row
            y = int(i / n)  # Column
            rowU = grid[y - 1]
            row = grid[y]
            rowD = grid[y + 1]
            adjacent = [rowU[x - 1], rowU[x], rowU[x + 1], row[x - 1], row[x], row[x + 1], rowD[x - 1], rowD[x],
                        rowD[x + 1]]
            if i_old == 'T':
                adjacent.append(i_old)
            if not ('T' in adjacent):
                np.put(grid, k_old, '#')
                k = pos_old[0] + n * pos_old[1]
                np.put(grid, k, 'T')
                if not k in history_visited:
                    history_visited.append(k)
                k_old = k
    #     print(np.array2string(grid, separator=' ', formatter={'str_kind': lambda x: x}))
    # print(len(history_visited))
    return history_visited


if __name__ == '__main__':
    data_folder = Path("data/")
    puzzle_input = data_folder / "input_test.txt"

    input_list = []

    with open(puzzle_input) as f:
        for line in f:
            chars = line.strip().split(' ')
            chars[1] = int(chars[1])
            input_list.append(chars)

    n = 20
    grid = np.chararray((n, n), unicode=True)
    grid[:] = '.'
    s = [n / 2, n / 2]
    H = Mover(start=s)

    visited = move(input_list, H, s)
    print(visited)
    history_visited1 = []
    np.put(grid, s, '$')
    k_old = s
    for m in visited:
        pos_old = m
        m_old = np.take(grid, m)
        np.put(grid, m, 'H')
        x = int(m % n)  # Row
        y = int(m / n)  # Column
        rowU = grid[y - 1]
        row = grid[y]
        rowD = grid[y + 1]
        adjacent = [rowU[x - 1], rowU[x], rowU[x + 1], row[x - 1], row[x], row[x + 1], rowD[x - 1], rowD[x],
                    rowD[x + 1]]
        if m_old == 'T':
            adjacent.append(m_old)
        if not ('T' in adjacent):
            np.put(grid, k_old, '#')
            k = pos_old
            np.put(grid, k, 'T')
            if not k in history_visited1:
                history_visited1.append(k)
            k_old = k
    print(np.array2string(grid, separator=' ', formatter={'str_kind': lambda x: x}))
    print(len(history_visited1))


