from random import randint
import os
from time import sleep
import math



rows = 60
cols = 30

def createGrid():
    grid = []
    for y in range(cols):
        row = []
        for x in range(rows):
            row.append('.')
        grid.append(row) 
    return grid


grid = createGrid()

#adds shape to grid
r = 0
angle = 0



while True:

    for angle in range(2000):
        pos_x = int(r * math.cos(angle))
        pos_y = int(r * math.sin(angle) / 2)
        grid[pos_y][pos_x] = '\x1b[40m'+'o'+'\x1b[0m'

#print the grid
    for i in range(len(grid)):
        print(f'{"".join(grid[i])}')

    r += 1

    sleep(0.2)
    os.system('clear')