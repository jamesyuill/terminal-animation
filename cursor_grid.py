from time import sleep
import os
import keyboard

# cursor = ['.','.','.','.','.','.','.','.','o','.','.','.','.','.','.','.','.',]

cursor = [
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','o','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.',],
]

grid_y_max = len(cursor)
grid_x_max = len(cursor[0])
# print(len(cursor))

def currentPosition(cursor):
    for i, row in enumerate(cursor):
        for j, element in enumerate(row):
            if element == 'o':
                return {'y':i, 'x':j}
    return None



def movePosition(cursor_list, direction):
    o_pos = currentPosition(cursor_list)

    if direction == 'left' and o_pos.get('x') != 0:
        cursor_list[o_pos.get('y')][o_pos.get('x') - 1] = 'o'
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'right' and o_pos.get('x') != (grid_x_max - 1):
        cursor_list[o_pos.get('y')][o_pos.get('x') + 1] = 'o'
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'up' and o_pos.get('y') != 0:
        cursor_list[o_pos.get('y')-1][o_pos.get('x')] = 'o'
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'
    elif direction == 'down' and o_pos.get('y') != (grid_y_max - 1):
        cursor_list[o_pos.get('y')+1][o_pos.get('x')] = 'o'
        cursor_list[o_pos.get('y')][o_pos.get('x')] = '.'

    return cursor_list


os.system('stty -echo')


while True:

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


