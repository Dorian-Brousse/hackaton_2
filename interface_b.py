import flet as ft 
import keyboard as kb
import sys
import numpy as np


list = [1,2,3,4,5,6,7,0,8]
aim = [1,2,3,4,5,6,7,8,0]
board = np.array(list).reshape(3,3)
aim_board = np.array(aim).reshape(3,3)


def circle(number):
    return ft.CircleAvatar(
        content=ft.Text(number),
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE
    )

def main(page):
    page.title = "Puzzle Game"
    page.window_width = 200
    page.window_height = 270
    page.bgcolor=ft.colors.BLACK
    page.add(
        ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row([
                    circle(board[0,0]),
                    circle(board[0,1]),
                    circle(board[0,2])
                ],
                alignment=ft.MainAxisAlignment.CENTER),

                ft.Row([
                    circle(board[1,0]),
                    circle(board[1,1]),
                    circle(board[1,2])
                ],
                alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    circle(board[2,0]),
                    circle(board[2,1]),
                    circle(board[2,2])
                ],
                alignment=ft.MainAxisAlignment.CENTER)
            ]
        ),
        ft.Divider(
            color=ft.colors.BLUE
        ),
        ft.Row([
            ft.IconButton(
            icon=ft.icons.AUTORENEW,
            icon_color=ft.colors.BLUE,
            icon_size=20,
            tooltip="New game",
                ),
            ft.IconButton(
            icon=ft.icons.COMPUTER,
            icon_color="blue400",
            icon_size=20,
            tooltip="Automate",
                ),
            ft.IconButton(
            icon=ft.icons.EXIT_TO_APP,
            icon_color="blue400",
            icon_size=20,
            tooltip="Exit",
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    )


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
        
        main(page)

    while np.any(board != aim_board):
        manually()
        page.update()
    print('YOU WON!')

print(board)
print(aim_board)
    

ft.app(target=main)