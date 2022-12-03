#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      03.12.22
   Kurs:      Advent of Code
   Topic:     Rucksack Recognition b
"""

items_list = []

with open("data/input.txt") as f:
    for line in f:
        items = line.strip()
        items_list.append(items)

items_prior = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z',]

prior_tot = 0
prior_group = 0
groups = []
count = 0

for content in items_list:
    groups.append(content)
    count += 1
    if count == 3:
        prior_group = 0
        first = set(groups[0])
        second = set(groups[1])
        third = set(groups[2])
        set1 = first.intersection(second)
        result_set = list(set1.intersection(third))
        idx = items_prior.index(result_set[0]) + 1
        prior_tot += idx
        count = 0
        groups = []

print(prior_tot)