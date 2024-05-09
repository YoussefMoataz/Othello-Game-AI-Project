import flet as ft
from ui import *

def Game(page: ft.Page, params, basket):

    set_page(page)
    create_board()

    return ft.View("/game", controls=[board])
