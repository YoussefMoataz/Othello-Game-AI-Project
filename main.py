from app.ui import *
import flet as ft
from app.views.home import Home
from app.views.game import Game
from flet_route import Routing, path

def main(page: ft.Page):
    page.title = "Othello Game"
    page.window_width = 500
    page.window_height = 620
    page.window_center()

    app_routes = [
        path("/", clear=True, view=Home),
        path("/game", clear=True, view=Game),
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

ft.app(main)
