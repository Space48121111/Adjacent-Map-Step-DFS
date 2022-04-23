'''
Generator: big datasheet/data stream for small functions
'lazy' iterator ()-parentheses list[]-brackets but don't store vals, separate into columns
yield each row/flow, capture/send back/remember the initial state
suspend/state/local var/instruction pointer/internal stack/exception handling saved instead of returning/terminate the program
next(gen) sanity check one at a time
palindrome read the same backwards as forwards

'''

from __future__ import annotations
from typing import Generator
import collections

input = '''\
2199943210
3987894921
9856789892
8767896789
9899965678
'''

'''
output: lowest 1 0 5 5 15 sum(1 + height)
[3, 9, 14, 9]
1134 product of paths
'''
def adjacent(x: int, y: int) ->Generator[tuple(int, int), None, None]:
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

coords = collections.defaultdict(lambda: 9)

for y, line in enumerate(input.splitlines()):
    for x, val in enumerate(line):
        coords[(x, y)]= int(val)

total = 0
min = []
for (x, y), grid_val in coords.items():
    if all(coords.get(pt, 9) > grid_val for pt in adjacent(x, y)):
        total += grid_val + 1
        min.append((x, y))

print({total})

'''
DFS stack
'''

basins = []
for x, y in min:
    print(x, y)
    todo = [(x, y)]
    seen = set()

    while todo:
        x, y = todo.pop()
        print('1 ', x, y)
        seen.add((x, y))
        print(seen)

        for pt in adjacent(x, y):
            if not pt in seen and coords[pt] != 9:
                todo.append(pt)

    basins.append(len(seen))

# print('Basins ', basins)
basins.sort()
print({basins[-1] * basins[-2] * basins[-3]})







# end
