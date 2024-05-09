import flet as ft
from ui import *

def Game(page: ft.Page, params, basket):

    set_page(page)
    create_board()

    return ft.View("/game", horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                   controls=[game_score, board, game_state])
