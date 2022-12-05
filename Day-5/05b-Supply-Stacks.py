#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      05.12.22
   Kurs:      Advent of Code
   Topic:     Supply Stacks b
"""

instr_list = []

with open("input2.txt") as f:
    for line in f:
        items = line.strip()
        instr_list.append(items)

# stack1 = ['N', 'Z']
# stack2 = ['D','C','M']
# stack3 = ['P']
#
stack1 = ['Q', 'F', 'L', 'S', 'R']
stack2 = ['T', 'P', 'G', 'Q', 'Z', 'N']
stack3 = ['B', 'Q', 'M', 'S']
stack4 = ['Q', 'B', 'C', 'H', 'J', 'Z', 'G', 'T']
stack5 = ['S', 'F', 'N', 'B', 'M', 'H', 'P']
stack6 = ['G', 'V', 'L', 'S', 'N', 'Q', 'C', 'P']
stack7 = ['F', 'C', 'W']
stack8 = ['M', 'P', 'V', 'W', 'Z', 'G', 'H', 'Q']
stack9 = ['R', 'N', 'C', 'L', 'D', 'Z', 'G']

# stack_list = [stack1, stack2, stack3]
stack_list = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

for instr in instr_list:
    instr_num = int(instr[5:7])
    instr_pair = instr[-6:].split(' to ')
    idx_stack_pop = int(instr_pair[0])
    idx_stack_insert = int(instr_pair[1])
    load = []
    for i in range(instr_num):
        temp = stack_list[idx_stack_pop - 1].pop(0)
        load.append(temp)
    load.reverse()
    for j in load:
        stack_list[idx_stack_insert - 1].insert(0, j)

for stack in stack_list:
    print(stack[0])
