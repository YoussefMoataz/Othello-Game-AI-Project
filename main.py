from ui import *
import flet as ft

def main(page: ft.Page):
    page.title = "Orthello Game"
    page.window_width = 500
    page.window_height = 530
    page.window_center()

    create_board(page)

ft.app(main)
