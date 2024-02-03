from random import randint
import os
from time import sleep



rows = 50
cols = 10

def createGrid():
    grid = []
    for y in range(cols):
        row = []
        for x in range(rows):
            row.append('.')
        grid.append(row) 
    return grid


grid = createGrid()
for i in range(len(grid)):
    print(f'{"".join(grid[i])}\n')


