#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from time import sleep
import numpy as np


class CPU():
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.sprite = np.array([self.X - 1, self.X, self.X + 1])
        self.screen = np.full((6, 40), ' ')

    def tick(self):
        if self.cycle in self.sprite:
            np.put(self.screen, self.cycle, '#')
        else:
            np.put(self.screen, self.cycle, ' ')
        self.cycle += 1
        if self.cycle != 240:
            self.print_to_console()

    def print_to_console(self, print_on=True):
        if print_on:
            subprocess.run('clear')
            print(np.array2string(DX488.screen, separator='', formatter={'str_kind': lambda x: x}).replace(' [',
                                                                                                           '').replace(
                '[', '').replace(']', ''))
            sleep(0.001)


if __name__ == '__main__':
    with open("data/input.txt") as f:
        data = f.read().splitlines()

    DX488 = CPU()

    for instr in data:
        if instr[:4] == 'addx':
            DX488.tick()
            factor, _ = divmod(DX488.cycle, 40)
            DX488.sprite = np.array([DX488.X - 1, DX488.X, DX488.X + 1]) + factor * 40
            DX488.tick()
            DX488.X = DX488.X + int(instr[5:])
            factor, _ = divmod(DX488.cycle, 40)
            DX488.sprite = np.array([DX488.X - 1, DX488.X, DX488.X + 1]) + factor * 40

        if instr[:4] == 'noop':
            DX488.tick()
            factor, _ = divmod(DX488.cycle, 40)
            DX488.sprite = np.array([DX488.X - 1, DX488.X, DX488.X + 1]) + factor * 40
