import flet as ft
from app.controller import *

def Game(page: ft.Page, params, basket):

    diff = params.get("diff")
    controller = Controller(diff, page)

    return ft.View("/game/:diff", horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                   controls=[controller.game_score, controller.board, controller.game_state])
