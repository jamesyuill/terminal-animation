from time import sleep
import os
import keyboard

cursor = ['.','.','.','.','.','.','.','.','o','.','.','.','.','.','.','.','.',]

os.system('stty -echo')

def moveTheO(cursor_list, direction):
    o_index = cursor_list.index('o')
    cursor_list.remove('o')
    if direction == 'left':
        cursor_list.insert((o_index - 1),'o')
    elif direction == 'right':
        cursor_list.insert((o_index + 1),'o')
    
    return cursor_list



while True:
    print(''.join(cursor))
    sleep(0.1)
    os.system('clear')
    if keyboard.is_pressed('left'):
        cursor = moveTheO(cursor, 'left')
    elif keyboard.is_pressed('right'):
        cursor = moveTheO(cursor, 'right')
    elif keyboard.is_pressed('q'):
        break
    

os.system('stty echo')


