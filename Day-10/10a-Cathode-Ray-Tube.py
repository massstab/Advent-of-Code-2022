#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Cathode-Ray Tube a
"""


class CPU():
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.strenghts = []

    def tick(self):
        self.cycle += 1
        if Screen.cycle in [20, 60, 100, 140, 180, 220]:
            strength = Screen.cycle * Screen.X
            print(f'Cycle {self.cycle}: {strength}')
            self.strenghts.append(strength)


if __name__ == '__main__':
    with open("data/input.txt") as f:
        data = f.read().splitlines()

    Screen = CPU()

    for instr in data:
        if instr[:4] == 'addx':
            Screen.tick()
            Screen.tick()
            Screen.X += int(instr[5:])
        if instr[:4] == 'noop':
            Screen.tick()

    print(sum(Screen.strenghts))
