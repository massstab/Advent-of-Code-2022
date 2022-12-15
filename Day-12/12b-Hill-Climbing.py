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

    def neighbour_search_all(self):
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

    def neighbour_search(self):
        for node in self.nodes:
            neighbours = []
            if node.pos2D_x == 0 and node.pos2D_y == 0:
                neighbours.append(self.nodes[node.pos_1D + 1])
                neighbours.append(self.nodes[node.pos_1D + shape[1]])
            elif node.pos2D_x == shape[1] - 1 and node.pos2D_y == 0:
                neighbours.append(self.nodes[node.pos_1D - 1])
                neighbours.append(self.nodes[node.pos_1D + shape[1]])
            elif node.pos2D_x == 0 and node.pos2D_y == shape[0] - 1:
                neighbours.append(self.nodes[node.pos_1D + 1])
                neighbours.append(self.nodes[node.pos_1D - shape[1]])
            elif node.pos2D_x == shape[1] - 1 and node.pos2D_y == shape[0] - 1:
                neighbours.append(self.nodes[node.pos_1D - 1])
                neighbours.append(self.nodes[node.pos_1D - shape[1]])
            elif node.pos2D_x == 0:
                neighbours.append(self.nodes[node.pos_1D + 1])
                neighbours.append(self.nodes[node.pos_1D - shape[1]])
                neighbours.append(self.nodes[node.pos_1D + shape[1]])
            elif node.pos2D_x == shape[1] - 1:
                neighbours.append(self.nodes[node.pos_1D - 1])
                neighbours.append(self.nodes[node.pos_1D - shape[1]])
                neighbours.append(self.nodes[node.pos_1D + shape[1]])
            elif node.pos2D_y == 0:
                neighbours.append(self.nodes[node.pos_1D + shape[1]])
                neighbours.append(self.nodes[node.pos_1D - 1])
                neighbours.append(self.nodes[node.pos_1D + 1])
            elif node.pos2D_y == shape[0] - 1:
                neighbours.append(self.nodes[node.pos_1D - shape[1]])
                neighbours.append(self.nodes[node.pos_1D - 1])
                neighbours.append(self.nodes[node.pos_1D + 1])
            else:
                neighbours.append(self.nodes[node.pos_1D - shape[1]])
                neighbours.append(self.nodes[node.pos_1D + 1])
                neighbours.append(self.nodes[node.pos_1D + shape[1]])
                neighbours.append(self.nodes[node.pos_1D - 1])
            node.neighbours = neighbours

        for node in self.nodes:
            remove_nodes = []
            for i, neighbour in enumerate(node.neighbours):
                neighbourvalue = neighbour.value
                nodevalue = node.value - 1
                if neighbourvalue < nodevalue:
                    remove_nodes.append(neighbour)
            for j in remove_nodes:
                node.neighbours.remove(j)


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
        self.visited = False
        self.parent_node = None


def pathfinder(graph, source_node, target_node):
    history = []
    current_node = source_node

    steps = 0
    while not current_node.is_target:
        steps += 1

        # sorted_neighbours = sorted(current_node.neighbours, key=lambda x: np.sqrt((x.pos2D_x - target_node.pos2D_x)**2 + (x.pos2D_y - target_node.pos2D_y)**2), reverse=False)
        sorted_neighbours = sorted(current_node.neighbours, key=lambda x: x.value, reverse=True)
        for neighbour in list(sorted_neighbours):
            if (neighbour.value <= current_node.value + 1) and (not neighbour.visited):
                history.append(current_node)
                current_node.visited = True
                current_node = neighbour
                break
        if steps > shape[0] * shape[1]:
            print('Too many steps...: ', steps)
            break
    history.append(current_node)
    current_node.visited = True
    current_node = neighbour
    return history


def breadth_first(G, root):
    Q = []
    root.visited = True
    Q.append(root)
    while Q:
        v = Q.pop(0)
        if v.value == 1:
            return v
        for node in v.neighbours:
            if not node.visited:
                node.visited = True
                node.parent_node = v
                Q.append(node)


def prep_data():
    data_folder = Path("data/")
    puzzle_input = data_folder / "input.txt"

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
            convert[idx_S] = 1
        if -27 in convert:
            idx_E = convert.index(-27)
            convert[idx_E] = 27
        heightmap.append(convert)
        for i in convert:
            heightmap_flat.append(i)
    heightmap = np.array(heightmap)
    end_idx = heightmap_flat.index(27)
    print('End idx: ', end_idx)
    return heightmap, heightmap_flat, end_idx


if __name__ == '__main__':
    heightmap, heightmap_flat, end = prep_data()
    shape = heightmap.shape
    area = Graph(heightmap, 0, end, shape)
    for m, n in enumerate(heightmap_flat):
        node = Node(m, n, shape)
        area.nodes.append(node)
    heightmap_flat[end] = 26
    target = area.nodes[end]
    target.value == 26
    area.neighbour_search()
    start = breadth_first(area, target)

    history = []
    current_node = start
    while current_node:
        history.append(current_node.parent_node)
        current_node = current_node.parent_node

    history = list(reversed(history))
    print(len(history)-1)
    fig, ax = plt.subplots(figsize=(20, 20), dpi=150)
    plt.tight_layout()
    im = ax.imshow(heightmap)
    ax.set_xticks(np.arange(shape[1] + 1) - .5, minor=True)
    ax.set_yticks(np.arange(shape[0] + 1) - .5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=.2)
    arrow_length = 0.4
    for i, p in enumerate(history[1:]):
        if i != len(history) - 1:
            p_next = history[i + 1]
        plt.arrow(p.pos2D_x - .1, p.pos2D_y + 0.2, arrow_length * (p_next.pos2D_x - p.pos2D_x),
                  arrow_length * (p_next.pos2D_y - p.pos2D_y), width=.04)
    for p in area.nodes:
        if p.is_source:
            plt.annotate(f'S, {p.value}', (p.pos2D_x - 0.4, p.pos2D_y - 0.2), fontsize=4, c='r')
        elif p.is_target:
            plt.annotate(f'E, {p.value}', (p.pos2D_x - 0.4, p.pos2D_y - 0.2), fontsize=4)
        else:
            plt.annotate(f'{chr(p.value + 96)} {p.value}', (p.pos2D_x, p.pos2D_y), fontsize=4)
    plt.show()
    plt.close()

    # 377 too high
    # 376 too high
    # 375 right!
