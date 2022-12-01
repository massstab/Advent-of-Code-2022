#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      01.12.22
   Kurs:      Advent of Code
   Topic:     Calorie Counting b
"""

deercal_dict = {}
cal = 0
i = 1

with open("data/input.txt") as f:
    for line in f:
        if line.strip() == '':
            deercal_dict[i] = cal
            cal = 0
            i += 1
        else:
            cal += int(line.strip())

calrank = sorted(deercal_dict.values())
sumtop3 = calrank[-1] + calrank[-2] + calrank[-3]

print(sumtop3)
