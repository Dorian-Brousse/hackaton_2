import flet as ft 
import numpy as np
from flet import app, icons
from flet import MainAxisAlignment
from flet import (
    Card,
    Column,
    Container,
    Divider,
    FilledButton,
    IconButton,
    Markdown,
    Row,
    Text,
    TextField,
)

def init():
    global board 
    board = []
    list = [1,2,3,4,5,6,7,8,0]
    i=0
    while list != []:
        n = np.random.randint(0,9-i)
        board.append(list[n])
        del(list[n])
        i = i+1
    print (board)

def graph(page : ft.Page):
    init()
    global board
    init_board = board
    page.title = 'Puzzle 8'
    page.window_width = 320
    page.window_height = 450
    page.add(
        Column(
            [
            ft.Row([ft.TextField(label = "Think using the help button")]),
            ft.GridView([
                ft.FilledTonalButton(board[0]),
                ft.FilledTonalButton(board[1]),
                ft.FilledTonalButton(board[2]),
                ft.FilledTonalButton(board[3]),
                ft.FilledTonalButton(board[4]),
                ft.FilledTonalButton(board[5]),
                ft.FilledTonalButton(board[6]),
                ft.FilledTonalButton(board[7]),
                ft.FilledTonalButton(board[8]),
                ],
                runs_count= 3,
            ),
            ft.Row(
                alignment= MainAxisAlignment.CENTER,
                controls =[
                    ft.IconButton
                    (
                        icon = ft.icons.SHUFFLE_SHARP, 
                        icon_color = ft.colors.RED, 
                        tooltip='Reshuffle',
                        ),
                    ft.IconButton
                    (
                        icon = ft.icons.ARROW_FORWARD_SHARP, 
                        icon_color = ft.colors.GREEN, 
                        tooltip='Help (1 move)'
                        ),
                    ft.IconButton
                    (
                        icon = ft.icons.COMPUTER    , 
                        icon_color = ft.colors.BLUE, 
                        tooltip='Finish puzzle' 
                        ),
                    ft.IconButton
                    (
                        icon = ft.icons.RESTART_ALT, 
                        icon_color = ft.colors.RED, 
                        tooltip='Restart',
                        )
                    ]
                    )
        ])
    )

app(target=graph)