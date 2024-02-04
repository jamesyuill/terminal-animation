from random import randint
import os
from time import sleep
import math



rows = 60
cols = 30
grid_items_total = 60 * 30

def createGrid():
    grid = []
    for y in range(cols):
        row = []
        for x in range(rows):
            row.append('.')
        grid.append(row) 
    return grid


grid = createGrid()



while True:

    for y in range(cols):
        for x in range(rows):
            if grid[y][x] == '.':
                grid[y][x] = '/'
            elif grid[y][x] == '/':
                grid[y][x] = '|'
            elif grid[y][x] == '|':
                grid[y][x] = '\\'
            elif grid[y][x] == '\\':
                grid[y][x] = '-'
            elif grid[y][x] == '-':
                grid[y][x] = '.'
            
            


#print the grid
    for i in range(len(grid)):
        print(f'{"".join(grid[i])}')

    
    

    sleep(0.2)
    os.system('clear')