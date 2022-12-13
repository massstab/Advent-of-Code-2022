#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Hill Climbing Algorithm b
"""

import numpy as np
from pathlib import Path


if __name__ == '__main__':
    data_folder = Path("data/")
    puzzle_input = data_folder / "input_test.txt"

    input_list = []

    with open(puzzle_input) as f:
        for line in f:
            chars = line.strip().split(' ')
            chars[1] = int(chars[1])
            input_list.append(chars)

