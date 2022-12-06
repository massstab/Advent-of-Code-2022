#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      06.12.22
   Kurs:      Advent of Code
   Topic:     Tuning Trouble b
"""

char_list = []

with open("data/input.txt") as f:
    while True:
        char = f.read(1)
        if not char:
            break
        char_list.append(char)

last3 = []
for i, c in enumerate(char_list):
    if len(last3) < 13:
        last3.append(c)
        continue
    last3.append(c)
    len_set = len(set(last3))
    if len_set == 14:
        print(i+1)
        break
    last3.pop(0)
