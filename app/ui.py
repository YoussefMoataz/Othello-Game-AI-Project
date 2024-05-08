import flet as ft
from ui_utils import *
from utils import *
from orthello import Orthello

GREEN = "green"
WHITE = "white"
BLACK = "black"

board = ft.GridView(width=500, runs_count=8,  expand=1)
page = None
orthello = None

def set_page(p):
    global page
    page = p

def create_white_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(2), ft.BorderSide(2), ft.BorderSide(2), ft.BorderSide(2)), bgcolor=WHITE, margin=5)

def create_black_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE)), bgcolor=BLACK, margin=5)

def create_available_square():
    return ft.Container(border=ft.Border(ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE)))

def create_square_click_handler(index):
    def click(e):
        print("clicked index:", get_index_2d(index))
        set_available(index) # todo: add player movement to orthello and let it calculate the move
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
    orthello.set_available(i, j)

def create_board():
    global orthello
    orthello = Orthello()

    for i in range(0, 64):
        click_handler = create_square_click_handler(i)
        board.controls.append(ft.Container(bgcolor=GREEN, on_click=click_handler))
    
    page.add(board)
    page.update()

def refresh_board():
    board_orthello = orthello.get_board_1d()

    for i in range(0, 64):
        if board_orthello[i] == AVAILABLE:
            board.controls[i].content = create_available_square()

    page.update()
