#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Hill Climbing Algorithm b
"""

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt


class Graph():
    def __init__(self, heights_array, start_1D, end_1D, shape):
        self.array = heights_array
        self.nodes = []
        self.start_1D = start_1D
        self.start_2D_x = int(start_1D % shape[1])
        self.start_2D_y = int(start_1D / shape[1])
        self.end_1d = end_1D
        self.end_2d_x = int(end_1D % shape[1])
        self.end_2d_y = int(end_1D / shape[1])

    def neighbour_search(self):
        for node in self.nodes:
            neighbours = []
            rowU_exists = False
            rowD_exists = False

            # The row above the node
            idx = node.pos2D_y - 1
            if idx >= 0:
                rowU = self.array[idx]
                rowU_exists = True

            # The row from the node itself
            idx = node.pos2D_y
            row = self.array[idx]

            # The row below the node
            try:
                idx = node.pos2D_y + 1
                rowD = self.array[idx]
                rowD_exists = True
            except IndexError as e:
                print(f'LIVIN ON THE EDGE! Node ({node.pos2D_x}, {node.pos2D_y}) can not find a row above: ', e)

            # Now the index inside the rows: For rowU
            if rowU_exists:
                idx = node.pos2D_x - 1
                if idx >= 0:
                   neighbours.append(self.nodes[node.pos_1D - shape[1] - 1])
                neighbours.append(self.nodes[node.pos_1D - shape[1]])
                try:
                    idx = node.pos2D_x + 1
                    rowU[idx]
                    neighbours.append(self.nodes[node.pos_1D - shape[1] + 1])
                except IndexError as e:
                    print(f'LIVIN ON THE EDGE! Node ({node.pos2D_x}, {node.pos2D_y}) can not find a neighbour NE: ', e)

            # For row
            idx = node.pos2D_x - 1
            if idx >= 0:
                neighbours.append(self.nodes[node.pos_1D - 1])
            try:
                idx = node.pos2D_x + 1
                row[idx]
                neighbours.append(self.nodes[node.pos_1D + 1])
            except IndexError as e:
                print(f'LIVIN ON THE EDGE! Node ({node.pos2D_x}, {node.pos2D_y}) can not find a neighbour E: ', e)

            # For rowD
            if rowD_exists:
                idx = node.pos2D_x - 1
                if idx >= 0:
                    neighbours.append(self.nodes[node.pos_1D + shape[1] - 1])
                neighbours.append(self.nodes[node.pos_1D + shape[1]])
                try:
                    idx = node.pos2D_x + 1
                    rowD[idx]
                    neighbours.append(self.nodes[node.pos_1D + shape[1] + 1])
                except IndexError as e:
                    print(f'LIVIN ON THE EDGE! Node ({node.pos2D_x}, {node.pos2D_y}): can not find a neighbour SE', e)

            node.neighbours = neighbours


class Node():
    def __init__(self, idx_1D, value, shape):
        self.value = value
        self.neighbours = []
        self.dist_n = np.inf
        self.prev = None
        self.pos_1D = idx_1D
        self.pos2D_x = int(idx_1D % shape[1])  # Row
        self.pos2D_y = int(idx_1D / shape[1])  # Column
        self.is_source = False
        self.is_target = False

def dijkstra(graph, source_node):
    history = []
    queue = graph.nodes
    for i in range(len(graph.nodes)):
        pass
        # print(i)
        # print(graph.nodes[i].is_target)
    # while queue:
    #     pass


def prep_data():
    data_folder = Path("data/")
    puzzle_input = data_folder / "input_test.txt"

    input_list = []

    with open(puzzle_input) as f:
        for line in f:
            chars = line.strip()
            input_list.append(chars)

    heightmap = []
    heightmap_flat = []
    for chars in input_list:
        convert = [ord(c) - 96 for c in chars]
        if -13 in convert:
            idx_S = convert.index(-13)
            convert[idx_S] = 0
        if -27 in convert:
            idx_E = convert.index(-27)
            convert[idx_E] = 27
        heightmap.append(convert)
        for i in convert:
            heightmap_flat.append(i)
    heightmap = np.array(heightmap)
    return heightmap, heightmap_flat, heightmap_flat.index(0), heightmap_flat.index(27)

if __name__ == '__main__':
    heightmap, heightmap_flat, start, end = prep_data()
    shape = heightmap.shape
    print(heightmap.shape)
    area = Graph(heightmap, start, end, shape)
    for loc, val in enumerate(heightmap_flat):
        node = Node(loc, val, shape)
        area.nodes.append(node)
        if loc == start:
            node.is_source = True
        if loc == end:
            node.is_target = True
    area.neighbour_search()
    dijkstra(area, shape)



    fig, ax = plt.subplots()
    im = ax.imshow(heightmap)
    for p in area.nodes[:]:
        plt.arrow(p.pos2D_x, p.pos2D_y, .3, 0, width=.05)
    for p in area.nodes:
        if p.value == 0:
            plt.annotate('Start', (p.pos2D_x, p.pos2D_y))
        elif p.value == 27:
            plt.annotate('Target', (p.pos2D_x, p.pos2D_y))
        else:
            plt.annotate(f'{chr(p.value + 96)}', (p.pos2D_x, p.pos2D_y))
    plt.show()