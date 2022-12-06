#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      03.12.22
   Kurs:      Advent of Code
   Topic:     Rucksack Recognition a
"""
import string

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

for content in items_list:
    mid = int(len(content)/2)
    first = set(content[:mid])
    second = set(content[mid:])
    common = list(first & second)
    idx = items_prior.index(common[0]) + 1
    prior_tot += idx

print(prior_tot)