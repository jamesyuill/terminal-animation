from random import randint
import os
from time import sleep

grid_x = 40
grid_y = 20

while True:

    for y in range(grid_y):
        rows = []
        for x in range(grid_x):
            random_digit = randint(40,47)
            rows.append(f'\x1b[{random_digit}m' + ' ')
        print(''.join(rows)+'\x1b[0m')
    
    sleep(0.2)
    os.system('clear')




