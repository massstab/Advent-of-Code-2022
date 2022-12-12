#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Treetop Tree House a
"""

import numpy as np

input_list = []

with open("data/input.txt") as f:
    for line in f:
        chars = line.strip()
        row = [int(i) for i in chars]
        input_list.append(row)

forest = np.array(input_list)
visible = []
for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        ij = forest[i, j]
        if i == 0 or j == 0 or i == forest.shape[0] - 1 or j == forest.shape[1] - 1:
            visible.append(forest[i, j])
            # print('ij: ', i, j)
            continue
        else:
            row = forest[i]
            column = forest.transpose()[j]
            right = row[j + 1:]
            left = row[:j]
            down = column[i + 1:]
            up = column[:i]
            right_bool = all(x < ij for x in right)
            left_bool = all(x < ij for x in left)
            down_bool = all(x < ij for x in down)
            up_bool = all(x < ij for x in up)
            if right_bool or left_bool or down_bool or up_bool:
                visible.append(forest[i, j])

print(len(visible))
