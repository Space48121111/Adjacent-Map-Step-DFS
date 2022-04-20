from __future__ import annotations
from typing import Generator

txt = open('adjacent_map_dfs.txt', 'r')
input1 = txt.read()

input = '''\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

'''
energy level
-- += 1 once per step
-- >9 -> flash 0
== adjacent(diagonally) += 1
output: 10 phrases -> 204 100 steps -> 1656 flashes
output1: 195 val = 0 flash all simultaneously

11111
19991
19191
19991
11111 ->

34543
40004
50005
40004
34543

algorithm/pseudo code:
time complexity: O(V + E)
space complexity: O(d)
adjacent: (x_a, y_a)
(-1, 0, 1) (x + x_a, y + y_a)
coords[x, y] = int(val)
flashes = 0
todo = []
for _ in range(100):
    for k, v in coords.values():
        coords[k] += 1
        if > 9:
            todo.append(k)
while todo:
    pt = todo.pop()
    if coords[pt] == 0:
        continue
    flashes += 1
    coords[pt] = 0
for rest in adjacent(pt):
    if rest in coords and != 0:
        coords[pt] += 1
    if > 9:
        todo.append(pt)

'''

def adjacent(x: int, y: int) -> Generator(tuple[x, y], None, None):
    for x_a in (-1, 0, 1):
        for y_a in (-1, 0, 1):
            if x_a == y_a == 0:
                continue
            else:
                yield x + x_a, y + y_a
def map_dfs():
    coords = {}
    flashes = 0
    todo = []
    steps = 0
    for y, line in enumerate(input.splitlines()):
        for x, val in enumerate(line):
            coords[x, y]= int(val)

    for _ in range(100):
        for k, v in coords.items():
            coords[k] += 1
            if coords[k] > 9:
                todo.append(k)

        while todo:
            pt = todo.pop()
            if coords[pt] == 0:
                continue
            coords[pt] = 0
            flashes += 1
            for rest in adjacent(*pt):
                if rest in coords and coords[rest] != 0:
                    coords[rest] += 1
                    if coords[rest] > 9:
                        todo.append(rest)

    return flashes

print(map_dfs())

def map_dfs_steps():
    coords = {}
    flashes = 0
    todo = []
    steps = 0
    for y, line in enumerate(input.splitlines()):
        for x, val in enumerate(line):
            coords[x, y]= int(val)

    while True:
        steps += 1
        for k, v in coords.items():
            coords[k] += 1
            if coords[k] > 9:
                todo.append(k)

        while todo:
            pt = todo.pop()
            if coords[pt] == 0:
                continue
            coords[pt] = 0
            flashes += 1
            for rest in adjacent(*pt):
                if rest in coords and coords[rest] != 0:
                    coords[rest] += 1
                    if coords[rest] > 9:
                        todo.append(rest)

        if all(val == 0 for val in coords.values()):
            break

    return steps

print(map_dfs_steps())


# end
