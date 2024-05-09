import flet as ft
from ui_utils import *
from utils import *
from othello import Othello

GREEN = "green"
WHITE = "white"
BLACK = "black"
BORDER_WIDTH = 1

board = ft.GridView(width=500, runs_count=8, expand=1)
page = None
othello = None

def set_page(p):
    global page
    page = p
    
def set_othello(o):
    global othello
    othello = o

def create_white_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH)), bgcolor=WHITE, margin=5)

def create_black_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE)), bgcolor=BLACK, margin=5)

def create_available_square():
    return ft.Container(border=ft.Border(ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE)))

def create_square_click_handler(index):
    def click(e):
        i, j = get_index_2d(index)
        # print("clicked index:", i, j)
        othello.player_clicked(i, j)
        refresh_board()
    return click

def update_board(index, color):
    if color == BLACK:
        board.controls[index].content = create_black_disk()
    else:
        board.controls[index].content = create_white_disk()
    page.update()

def set_available(index):
    i, j = get_index_2d(index)
    othello.set_available(i, j)

def create_board():

    for i in range(0, 64):
        click_handler = create_square_click_handler(i)
        board.controls.append(ft.Container(bgcolor=GREEN, on_click=click_handler))
    
    # page.add(board)
    refresh_board()

def refresh_board():
    board_orthello = othello.get_board_1d()

    for i in range(0, 64):
        board.controls[i].border = None
        if board_orthello[i] == AVAILABLE:
            board.controls[i].content = create_available_square()
        elif board_orthello[i] == WHITE_DISK:
            board.controls[i].content = create_white_disk()
        elif board_orthello[i] == BLACK_DISK:
            board.controls[i].content = create_black_disk()
        else:
            board.controls[i].content = None
    
    if not othello.last_played == -1:
        board.controls[othello.last_played].border = ft.Border(ft.BorderSide(2, "red"), ft.BorderSide(2, "red"), ft.BorderSide(2, "red"), ft.BorderSide(2, "red"))

    page.update()
