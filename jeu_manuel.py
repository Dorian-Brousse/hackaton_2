import flet as ft
import keyboard as kb
import sys
import numpy as np

list = [1,2,3,4,5,6,7,0,8]
aim = [1,2,3,4,5,6,7,8,0]
board = np.array(list).reshape(3,3)
aim_board = np.array(aim).reshape(3,3)

pressed_arrows = {'up': False, 'down': False, 'left': False, 'right': False}

def UP():
    n=0
    if 0 in board[2]:
        pass
    else:
        if 0 in board[1]:
            for i in board[1]:
                if i == 0:
                    board[1][n] = board[2][n]
                    board[2][n] = 0
                else:
                    n+=1
        else:
            for i in board[0]:
                if i == 0:
                    board[0][n] = board[1][n]
                    board[1][n] = 0
                else:
                    n+=1

    print('UP !')
def DOWN():
    n=0
    if 0 in board[0]:
        pass
    else:
        if 0 in board[1]:
            for i in board[1]:
                if i == 0:
                    board[1][n] = board[0][n]
                    board[0][n] = 0
                else:
                    n+=1
        else:
            for i in board[2]:
                if i == 0:
                    board[2][n] = board[1][n]
                    board[1][n] = 0
                else:
                    n+=1
def LEFT():
    n=0
    if 0 in board[:,2]:
        pass
    else:
        if 0 in board[:,1]:
            for i in board[:,1]:
                if i == 0:
                    board[n,1] = board[n,2]
                    board[n,2] = 0
                else:
                    n+=1
        
        else:
            for i in board[:,0]:
                if i == 0:
                    board[n,0] = board[n,1]
                    board[n,1] = 0
                else:
                    n+=1
def RIGHT():
    n=0
    if 0 in board[:,0]:
        pass
    else:
        if 0 in board[:,1]:
            for i in board[:,1]:
                if i == 0:
                    board[n,1] = board[n,0]
                    board[n,0] = 0
                else:
                    n+=1
        
        else:
            for i in board[:,2]:
                if i == 0:
                    board[n,2] = board[n,1]
                    board[n,1] = 0
                else:
                    n+=1

def manually():
    if kb.is_pressed('q') == True:
        sys.exit()

    for arrow in pressed_arrows:
        if kb.is_pressed(arrow) and not pressed_arrows[arrow]:
            print(f"Flèche {arrow} pressée")
            pressed_arrows[arrow] = True
            
            if arrow == 'up':
                UP()
            elif arrow == 'down':
                DOWN()
            elif arrow == 'left':
                LEFT()
            elif arrow == 'right':
                RIGHT()
            print(board)

        elif not kb.is_pressed(arrow):
            pressed_arrows[arrow] = False


print(board)
print(aim_board)

while np.any(board != aim_board):
    manually()

print('YOU WON!')
