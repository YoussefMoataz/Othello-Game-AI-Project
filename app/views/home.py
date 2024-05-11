import flet as ft
from app.controller import *
from app.othello import Othello
from app.utils import *

def Home(page: ft.Page, params, basket):

    def easy_clicked(e):
        page.go(f"/game/{DIFF_EASY}")

    def medium_clicked(e):
        page.go(f"/game/{DIFF_MEDIUM}")

    def hard_clicked(e):
        page.go(f"/game/{DIFF_HARD}")

    button_height, button_width = 60, 140

    return ft.View("/", 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[ft.Column(
            spacing=40,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.FilledButton("Easy", on_click=easy_clicked, height=button_height, width=button_width), 
                ft.FilledButton("Medium", on_click=medium_clicked, height=button_height, width=button_width), 
                ft.FilledButton("Hard", on_click=hard_clicked, height=button_height, width=button_width)
            ])
        ])
