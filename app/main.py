from ui import *
import flet as ft
from views.home import Home
from views.game import Game
from flet_route import Routing, path

def main(page: ft.Page):
    page.title = "Orthello Game"
    page.window_width = 500
    page.window_height = 530
    page.window_center()

    app_routes = [
        path("/", clear=True, view=Home),
        path("/game", clear=True, view=Game),
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

ft.app(main)
