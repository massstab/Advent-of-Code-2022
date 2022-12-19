#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      massstab
   Date:      07.12.22
   Kurs:      Advent of Code
   Topic:     No Space Left On Device b
"""


class File:
    def __init__(self):
        self.size = None
        self.path = None
        self.name = None

    def size(self):
        pass


class Directory:
    def __init__(self, is_root=False):
        self.files = []
        self.directories = []
        self.is_root = is_root
        self.path = '/'
        self.parent_path = None
        self.name = 'home'
        self.foldersize = None
        self.recursive_size = None

    def calc_size(self):
        size_tot = 0
        for f in self.files:
            size_tot += f.size
        self.foldersize = size_tot


def execution(dir, op, dirs):
    if op[0] == '$':
        if op[1] == 'cd':
            if op[2] == '..':
                for d in dirs:
                    if d.path == dir.parent_path:
                        dir = d
                        break
                    else:
                        continue
                    print(f'No parent path for {dir.name} found!')
            elif op[2] == '/':
                for d in dirs:
                    if d.is_root:
                        dir = d
                        break
            else:
                changedir = op[2]
                for d in dir.directories:
                    if d.name == changedir:
                        dir = d
                        break
                    else:
                        continue
                    print(f'No {changedir} directory found')
    else:
        if op[0] == 'dir':
            new_dir = Directory()
            new_dir.name = op[1]
            new_dir.path = dir.path + new_dir.name + '/'
            new_dir.parent_path = dir.path
            dir.directories.append(new_dir)
            dirs.append(new_dir)
        else:
            filesize = op[0]
            filename = op[1]
            new_file = File()
            new_file.size = int(filesize)
            new_file.name = filename
            new_file.path = dir.path
            dir.files.append(new_file)
    return dir


def calc_foldersize(dir):
    dir.calc_size()
    # print('-----')
    # print(f'Size dir {dir.name}: {dir.foldersize}')
    # print('Files:')
    # for file in dir.files:
    #     print(f'{file.size} {file.name} ')
    # print('-----')

    for d in dir.directories:
        calc_foldersize(d)


def calc_foldersize_recursive(dir, size):
    size = dir.foldersize
    for d in dir.directories:
        size += calc_foldersize_recursive(d, size)
    dir.recursive_size = size
    return size


def parse(data_path):
    data_listed = []
    with open(data_path) as f:
        for line in f:
            items = line.strip()
            data_listed.append(items)
    return data_listed


def solve(input_list, root_dir):
    dir_list = [root_dir]
    current_dir = root_dir
    for line in input_list:
        op = line.split()
        current_dir = execution(current_dir, op, dirs=dir_list)

    calc_foldersize(root_dir)
    calc_foldersize_recursive(root_dir, 0)

    space_used = root_dir.recursive_size
    free = 70_000_000 - space_used
    need = 30_000_000 - free

    for folder in sorted(dir_list, key=lambda d: d.recursive_size):
        if folder.recursive_size > need:
            ans = folder.recursive_size
            break

    return ans


def print_structure(dir):
    print(f'{dir.path} dirsize: {dir.foldersize} recursive size: {dir.recursive_size}')
    for d in dir.directories:
        print(f'dir {d.name}')
    for f in dir.files:
        print(f'{f.name}, {f.size}')
    for d in dir.directories:
        print_structure(d)


if __name__ == '__main__':
    input_list = parse(data_path="data/input.txt")
    root_dir = Directory(is_root=True)
    answer = solve(input_list, root_dir)
    # print_structure(root_dir)
    print('Result', answer)

# Too low: 216592
# Too high: 11285770
