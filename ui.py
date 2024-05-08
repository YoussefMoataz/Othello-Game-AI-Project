import flet as ft
from utils import *

board = ft.GridView(width=500, runs_count=8,  expand=1)

def create_white_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(2), ft.BorderSide(2), ft.BorderSide(2), ft.BorderSide(2)), bgcolor="white", margin=5)

def create_black_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(2, "white"), ft.BorderSide(2, "white"), ft.BorderSide(2, "white"), ft.BorderSide(2, "white")), bgcolor="black", margin=5)

def create_square_click_handler(index, page):
    def click(e):
        # print("clicked index:", get_index_2d(index))
        board.controls[index].content = create_black_disk()
        page.update()
    return click

def create_board(page):
    for i in range(0, 64):
        click_handler = create_square_click_handler(i, page)
        board.controls.append(ft.Container(bgcolor="green", on_click=click_handler))
    
    page.add(board)
    page.update()
