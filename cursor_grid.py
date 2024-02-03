from time import sleep
from random import randint
import os
import keyboard

# cursor = ['.','.','.','.','.','.','.','.','o','.','.','.','.','.','.','.','.',]

ship = '\x1b[44m' + 'A' + '\x1b[0m'
spacer = '\x1b[8m'+ '.' + '\x1b[0m'
speed = 5
edge_icon = '\x1b[35m' + '|'+ '\x1b[0m'
# ship = input('Choose your ship character or hit enter to use our default: ') or 'A'
# speed = int(input('Difficulty level? (1-5): ')) or 1

cursor = [
    [spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,],
    [spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,],
    [spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,],
    [spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,],
    [spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,],
    [spacer,spacer,spacer,spacer,ship,spacer,spacer,spacer,spacer,],
    [spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,],
    [spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,spacer,],
]

def displayGrid(cursor):
    print(edge_icon+''.join(cursor[0]) + edge_icon +'\n' +
          edge_icon+''.join(cursor[1]) + edge_icon +'\n' +
          edge_icon+''.join(cursor[2]) + edge_icon +'\n' +
          edge_icon+''.join(cursor[3]) + edge_icon +'\n' +
          edge_icon+''.join(cursor[4]) + edge_icon +'\n' +
          edge_icon+''.join(cursor[5]) + edge_icon +'\n' +
          edge_icon+''.join(cursor[6]) + edge_icon +'\n' +
          edge_icon+''.join(cursor[7]) + edge_icon)


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
        cursor_list[o_pos.get('y')][o_pos.get('x')] = spacer
    elif direction == 'right' and o_pos.get('x') != (grid_x_max - 1):
        cursor_list[o_pos.get('y')][o_pos.get('x') + 1] = ship
        cursor_list[o_pos.get('y')][o_pos.get('x')] = spacer
    elif direction == 'up' and o_pos.get('y') != 0:
        cursor_list[o_pos.get('y')-1][o_pos.get('x')] = ship
        cursor_list[o_pos.get('y')][o_pos.get('x')] = spacer
    elif direction == 'down' and o_pos.get('y') != (grid_y_max - 1):
        cursor_list[o_pos.get('y')+1][o_pos.get('x')] = ship
        cursor_list[o_pos.get('y')][o_pos.get('x')] = spacer

    return cursor_list


#explosion function that takes in the position of the bomb and works out the indeses

def explosion(y_index,bomb_pos):
    site_x = bomb_pos.get('x')
    site_y = y_index -1

    cursor[site_y][site_x] = '\x1b[31m' + '*' + '\x1b[0m'
    cursor[site_y][site_x -1 ] = '\x1b[33m' + '(' + '\x1b[0m'
    cursor[site_y][site_x +1 ] = '\x1b[33m' + ')' + '\x1b[0m'

    displayGrid(cursor)

    sleep(0.5)
    if player_score == 1:
        print('\n', f'You got hit! You managed to avoid {player_score} bomb')
    else:
        print('\n', f'You got hit! You managed to avoid {player_score} bombs')





def createBomb():
    grid_width_index = grid_x_max - 1
    bomb_pos_x = randint(0,grid_width_index)
    return {"x":bomb_pos_x,"y":0}



bomb = createBomb()
y_index = 0
delay = 0
player_score = 0
bomb_trail1 = '\x1b[37m' + '.' + '\x1b[0m'
bomb_trail2 = '\x1b[90m' + '.' + '\x1b[0m'
bomb_icon = '\x1b[31m' + '*' + '\x1b[0m'
os.system('stty -echo')

while True:


    
    
    cursor[bomb.get('y')][bomb.get('x')] = bomb_icon
    cursor[bomb.get('y') -1 ][bomb.get('x')] = bomb_trail1
    cursor[bomb.get('y') -2 ][bomb.get('x')] = spacer

    if delay % 5 == 0:
        bomb['y'] += 1

    if bomb.get('y') == grid_y_max:
        cursor[bomb.get('y') -1 ][bomb.get('x')] = bomb_trail1
        cursor[bomb.get('y') -2 ][bomb.get('x')] = spacer
        cursor[bomb.get('y') -1 ][bomb.get('x')] = spacer
        player_score += 1
        bomb = createBomb()

        

        # y_index = 0
    delay += speed


    ship_pos = currentPosition(cursor)

    if not ship_pos:
        explosion(y_index, bomb)
        break


    displayGrid(cursor)

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


