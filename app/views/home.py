import flet as ft
from ui import set_othello
from othello import Othello
from utils import *

def Home(page: ft.Page, params, basket):

    def easy_clicked(e):
        set_othello(Othello(DIFF_EASY))
        page.go("/game")

    def medium_clicked(e):
        set_othello(Othello(DIFF_MEDIUM))
        page.go("/game")

    def hard_clicked(e):
        set_othello(Othello(DIFF_HARD))
        page.go("/game")

    return ft.View("/", 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[ft.Column(
            spacing=40,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.FilledButton("Easy", on_click=easy_clicked), 
                ft.FilledButton("Medium", on_click=medium_clicked), 
                ft.FilledButton("Hard", on_click=hard_clicked)
            ])
        ])
