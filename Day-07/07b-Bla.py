#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Bla b
"""

char_list = []

with open("data/input.txt") as f:
    while True:
        char = f.read(1)
        if not char:
            break
        char_list.append(char)

