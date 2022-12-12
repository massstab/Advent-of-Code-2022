#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Treetop Tree House b
"""

import numpy as np

input_list = []

with open("data/input.txt") as f:
    for line in f:
        chars = line.strip()
        row = [int(i) for i in chars]
        input_list.append(row)

forest = np.array(input_list)
visibility_dict = {}
for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        visibility_dict[(i, j)] = {'right': 1, 'left': 1, 'down': 1, 'up': 1}

for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        ij = forest[i, j]
        if i == 0:
            visibility_dict[(i, j)]['up'] = 0
        if j == 0:
            visibility_dict[(i, j)]['left'] = 0
        if i == forest.shape[0] - 1:
            visibility_dict[(i, j)]['down'] = 0
        if j == forest.shape[1] - 1:
            visibility_dict[(i, j)]['right'] = 0

        row = forest[i]
        column = forest.transpose()[j]
        right = row[j + 1:]
        left = row[:j]
        down = column[i + 1:]
        up = column[:i]

        dist = 1
        for r in right[:-1]:
            if r >= ij:
                break
            dist += 1
            visibility_dict[(i, j)]['right'] = dist

        dist = 1
        for l in reversed(left[1:]):
            if l >= ij:
                break
            dist += 1
            visibility_dict[(i, j)]['left'] = dist

        dist = 1
        for d in down[:-1]:
            if d >= ij:
                break
            dist += 1
            visibility_dict[(i, j)]['down'] = dist

        dist = 1
        for u in reversed(up[1:]):
            if u >= ij:
                break
            dist += 1
            visibility_dict[(i, j)]['up'] = dist

        print(forest)
        print(i, j)
        print('right: ', visibility_dict[(i, j)]['right'])
        print('left: ', visibility_dict[(i, j)]['left'])
        print('down:', visibility_dict[(i, j)]['down'])
        print('up:'
              '', visibility_dict[(i, j)]['up'])
        print('---------------')

high_score = 0
idx = ()
# print(visibility_dict)
for tree in visibility_dict:
    score = visibility_dict[tree]['right'] * visibility_dict[tree]['left'] * visibility_dict[tree]['down'] * \
            visibility_dict[tree]['up']
    if score > high_score:
        high_score = score
        idx = tree

print('Score: ', high_score)
print('Index: ', idx)
