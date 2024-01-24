from time import sleep
from random import randint
import os
import keyboard

# cursor = ['.','.','.','.','.','.','.','.','o','.','.','.','.','.','.','.','.',]

ship = input('you ready to play? choose your ship character: ')[0]

cursor = [
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.',ship,'.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
]

grid_y_max = len(cursor)
grid_x_max = len(cursor[0])
# print(len(cursor))

def currentPosition(cursor):
    for i, row in enumerate(cursor):
        for j, element in enumerate(row):
            if element == ship:
                return {'y':i, 'x':j}
    return None



def movePosition(cursor_list, direction):
    o_pos = currentPosition(cursor_list)

    if direction == 'left' and o_pos.get('x') != 0:
        cursor_list[o_pos.get('y')][o_pos.get('x') - 1] = ship
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'right' and o_pos.get('x') != (grid_x_max - 1):
        cursor_list[o_pos.get('y')][o_pos.get('x') + 1] = ship
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'up' and o_pos.get('y') != 0:
        cursor_list[o_pos.get('y')-1][o_pos.get('x')] = ship
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'down' and o_pos.get('y') != (grid_y_max - 1):
        cursor_list[o_pos.get('y')+1][o_pos.get('x')] = ship
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'

    return cursor_list


#explosion function that takes in the position of the bomb and works out the indeses

def explosion(y_index,bomb_pos):
    site_x = bomb_pos.get('x')
    site_y = y_index

    cursor[site_y][site_x] = '\x1b[31m' + '*' + '\x1b[0m'
    cursor[site_y][site_x -1 ] = '\x1b[33m' + '(' + '\x1b[0m'
    cursor[site_y][site_x +1 ] = '\x1b[33m' + ')' + '\x1b[0m'

    print('|'+''.join(cursor[0]) + '|'+'\n' +
          '|'+''.join(cursor[1]) + '|'+'\n' +
          '|'+''.join(cursor[2]) + '|'+'\n' +
          '|'+''.join(cursor[3]) + '|'+'\n' +
          '|'+''.join(cursor[4]) + '|'+'\n' +
          '|'+''.join(cursor[5]) + '|'+'\n' +
          '|'+''.join(cursor[6]) + '|'+'\n' +
          '|'+''.join(cursor[7]) + '|')
    sleep(0.5)
    print('\n', f'You got hit! You managed to avoid {player_score} bombs')





def createBomb():
    grid_width_index = grid_x_max - 1
    bomb_pos_x = randint(0,grid_width_index)
    return {"x":bomb_pos_x,"y":0}



bomb = createBomb()
y_index = 0
delay = 0
player_score = 0

os.system('stty -echo')

while True:
    
    cursor[y_index][bomb.get('x')] = 'O'
    cursor[y_index - 1][bomb.get('x')] = '.'
    if delay % 5 == 0:
        y_index += 1
    if y_index == grid_y_max:
        cursor[grid_y_max-1][bomb.get('x')] = '.'
        y_index = 0
        player_score += 1
        bomb = createBomb()
    delay += 1


    ship_pos = currentPosition(cursor)

    if not ship_pos:
        explosion(y_index, bomb)
        break


    print('|'+''.join(cursor[0]) + '|'+'\n' +
          '|'+''.join(cursor[1]) + '|'+'\n' +
          '|'+''.join(cursor[2]) + '|'+'\n' +
          '|'+''.join(cursor[3]) + '|'+'\n' +
          '|'+''.join(cursor[4]) + '|'+'\n' +
          '|'+''.join(cursor[5]) + '|'+'\n' +
          '|'+''.join(cursor[6]) + '|'+'\n' +
          '|'+''.join(cursor[7]) + '|')
    
    sleep(0.1)
    os.system('clear')

    if keyboard.is_pressed('left'):
        cursor = movePosition(cursor, 'left')
    elif keyboard.is_pressed('right'):
        cursor = movePosition(cursor, 'right')
    elif keyboard.is_pressed('up'):
        cursor = movePosition(cursor, 'up')
    elif keyboard.is_pressed('down'):
        cursor = movePosition(cursor, 'down')
    elif keyboard.is_pressed('q'):
        break
    

os.system('stty echo')


