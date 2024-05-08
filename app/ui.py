import flet as ft
from ui_utils import *

GREEN = "green"
WHITE = "white"
BLACK = "black"

board = ft.GridView(width=500, runs_count=8,  expand=1)
page = None

def set_page(p):
    global page
    page = p

def create_white_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(2), ft.BorderSide(2), ft.BorderSide(2), ft.BorderSide(2)), bgcolor=WHITE, margin=5)

def create_black_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE)), bgcolor=BLACK, margin=5)

def create_square_click_handler(index, page):
    def click(e):
        print("clicked index:", get_index_2d(index))
        board.controls[index].content = create_black_disk()
        page.update()
    return click

def update_board(index, color):
    if color == BLACK:
        board.controls[index].content = create_black_disk()
    else:
        board.controls[index].content = create_white_disk()
    page.update()

def create_board():
    for i in range(0, 64):
        click_handler = create_square_click_handler(i, page)
        board.controls.append(ft.Container(bgcolor=GREEN, on_click=click_handler))
    
    page.add(board)
    page.update()
