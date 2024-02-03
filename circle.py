from random import randint
import os
from time import sleep

grid_x = 40
grid_y = int(grid_x / 2)

grid = [
    ['.','.','.','.','.'],
    ['.','.','.','.','.'],
    ['.','.','.','.','.'],
    ['.','.','.','.','.'],
    ['.','.','.','.','.'],
]

while True:

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = '0'

    print(grid)
            
        
        
    sleep(0.1)
    os.system('clear')