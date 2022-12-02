#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      02.12.22
   Kurs:      Advent of Code
   Topic:     Rock Paper Scissors b
"""

strat_list = []

with open("data/input.txt") as f:
    for line in f:
        strat = line.strip()
        strat_list.append(strat)



i = 0
round_score = 0
total_score = 0


# X: loose, Y: draw, Z: win
for outcome in strat_list:
    if outcome == 'A X':
        round_score += 3
    if outcome == 'A Y':
        round_score += 4
    if outcome == 'A Z':
        round_score += 8
    if outcome == 'B X':
        round_score += 1
    if outcome == 'B Y':
        round_score += 5
    if outcome == 'B Z':
        round_score += 9
    if outcome == 'C X':
        round_score += 2
    if outcome == 'C Y':
        round_score += 6
    if outcome == 'C Z':
        round_score += 7

    total_score += round_score
    round_score = 0

print(total_score)
