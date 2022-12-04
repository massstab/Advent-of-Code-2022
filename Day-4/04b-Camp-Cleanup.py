#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      04.12.22
   Kurs:      Advent of Code
   Topic:     Camp Cleanup b
"""

cleanup_list = []

with open("data/input.txt") as f:
    for line in f:
        items = line.strip()
        cleanup_list.append(items)

count = 0

for pair in cleanup_list:
    splitted = pair.split(",")
    a = splitted[0].split("-")
    b = splitted[1].split("-")
    a0 = int(a[0])
    a1 = int(a[1]) + 1
    b0 = int(b[0])
    b1 = int(b[1]) + 1
    IDs_a = list(range(a0, a1))
    IDs_b = list(range(b0, b1))
    a_contains_b = any(id in IDs_a for id in IDs_b)
    b_contains_a = any(id in IDs_b for id in IDs_a)
    # print(splitted, IDs_a, IDs_b, f"{a_contains_b}", f"{b_contains_a}")
    if a_contains_b or b_contains_a:
        count += 1

print(count)