#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     Bla a
"""

import re

input_list = []

with open("data/input_test.txt") as f:
    for line in f:
        items = line.strip()
        input_list.append(items)
print(input_list)

def treebuild(dir, command):
    if dir.is_leaf:
        return
    if re.match('\$ cd \w+', command):  # Matches $ cd blabli
        newdir = Directory()
        newdir.name = str(re.findall('[^$ cd ]', command))
        print(newdir.name)
        newdir.path = dir.path + newdir.name
        print(command)
    elif re.match('\$ cd \.\.', command):  # Matches $ cd ..
        print(command)
    elif re.match('\$ cd /', command):  # Matches $ cd /
        print(command)
    elif re.match('\$ ls', command):  # Matches $ ls
        print(command)

class file:
    def __init__(self):
        self.size = None
        self.path = None

    def size(self):
        pass

class Directory:
    def __init__(self, is_root=False):
        self.files = []
        self.is_leaf = None
        self.is_root = None
        self.path = '/'
        self.parent_path = None
        self.name = 'home'
    def size(self):
        pass

root_dir = Directory(is_root=True)
for i in input_list:
    if re.match('\$.+', i):
        treebuild(root_dir, command=i)
    elif re.match('dir.+', i):
        print('dir: ', i)
    else:
        print('file: ', i)
