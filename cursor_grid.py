from time import sleep
from random import randint
import os
import keyboard

# cursor = ['.','.','.','.','.','.','.','.','o','.','.','.','.','.','.','.','.',]

cursor = [
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','A','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
]

grid_y_max = len(cursor)
grid_x_max = len(cursor[0])
# print(len(cursor))

def currentPosition(cursor):
    for i, row in enumerate(cursor):
        for j, element in enumerate(row):
            if element == 'A':
                return {'y':i, 'x':j}
    return None



def movePosition(cursor_list, direction):
    o_pos = currentPosition(cursor_list)

    if direction == 'left' and o_pos.get('x') != 0:
        cursor_list[o_pos.get('y')][o_pos.get('x') - 1] = 'A'
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'right' and o_pos.get('x') != (grid_x_max - 1):
        cursor_list[o_pos.get('y')][o_pos.get('x') + 1] = 'A'
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'up' and o_pos.get('y') != 0:
        cursor_list[o_pos.get('y')-1][o_pos.get('x')] = 'A'
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'down' and o_pos.get('y') != (grid_y_max - 1):
        cursor_list[o_pos.get('y')+1][o_pos.get('x')] = 'A'
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'

    return cursor_list


# randomly insert a character in the first list of the matrix
# then remove it and replace with a dot
# move it into the next array at the same index position
# so i need the x & y position of the bomb

def createBomb():
    grid_width_index = grid_x_max - 1
    bomb_pos_x = randint(0,grid_width_index)
    return {"x":bomb_pos_x,"y":0}


os.system('stty -echo')

bomb = createBomb()
y_index = 0

delay = 0

while True:
    
    cursor[y_index][bomb.get('x')] = 'O'
    cursor[y_index - 1][bomb.get('x')] = '.'
    if delay % 5 == 0:
        y_index += 1
    if y_index == grid_y_max:
        cursor[grid_y_max-1][bomb.get('x')] = '.'
        y_index = 0
        bomb = createBomb()
    delay += 1
    print(''.join(cursor[0]) + '\n' +
          ''.join(cursor[1]) + '\n' +
          ''.join(cursor[2]) + '\n' +
          ''.join(cursor[3]) + '\n' +
          ''.join(cursor[4]) + '\n' +
          ''.join(cursor[5]) + '\n' +
          ''.join(cursor[6]) + '\n' +
          ''.join(cursor[7]))
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


