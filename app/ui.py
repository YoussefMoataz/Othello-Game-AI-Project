import flet as ft
from app.ui_utils import *
from app.utils import *
from app.othello import *
import time

GREEN = "green"
WHITE = "white"
BLACK = "black"
BORDER_WIDTH = 1

board = ft.GridView(width=500, runs_count=8, expand=1)
game_state = ft.Text(size=18)
game_score = ft.Text(size=25)
page = None
othello = None

def set_page(p):
    global page
    page = p
    
def set_othello(o):
    global othello
    othello = o

def create_white_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH)), bgcolor=WHITE, margin=5)

def create_black_disk():
    return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE)), bgcolor=BLACK, margin=5)

def create_available_square():
    return ft.Container(border=ft.Border(ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE)))

def create_square_click_handler(index):
    def click(e):
        i, j = get_index_2d(index)
        # print("clicked index:", i, j)
        if(othello.player_clicked(i, j)):
            refresh_board()
            refresh_state()
            refresh_score()
            time.sleep(1)
            othello.apply_best_move()
            refresh_board()
            refresh_state()
            refresh_score()
    return click

def create_board():

    for i in range(0, 64):
        click_handler = create_square_click_handler(i)
        board.controls.append(ft.Container(bgcolor=GREEN, on_click=click_handler))
    
    refresh_board()
    refresh_state()
    refresh_score()

def refresh_board():
    board_orthello = othello.get_board_1d()

    for i in range(0, 64):
        board.controls[i].border = None
        if board_orthello[i] == AVAILABLE:
            board.controls[i].content = create_available_square()
        elif board_orthello[i] == WHITE_DISK:
            board.controls[i].content = create_white_disk()
        elif board_orthello[i] == BLACK_DISK:
            board.controls[i].content = create_black_disk()
        else:
            board.controls[i].content = None
    
    if not othello.last_played == -1:
        board.controls[othello.last_played].border = ft.Border(ft.BorderSide(2, "red"), ft.BorderSide(2, "red"), ft.BorderSide(2, "red"), ft.BorderSide(2, "red"))

    page.update()

def refresh_state():
    if othello.state == STATE_PLAYER_TURN:
        game_state.value = "Player's turn"
    elif othello.state == STATE_AI_TURN:
        game_state.value = "AI making move ..."
    elif othello.state == STATE_NO_MORE_MOVES:
        game_state.value = "No more moves."
    elif othello.state == STATE_BLACK_WON:
        game_state.value = "You won!"
    elif othello.state == STATE_WHITE_WON:
        game_state.value = "AI won!"
    elif othello.state == STATE_DRAW:
        game_state.value = "Draw!"

    page.update()

def refresh_score():
    player, computer = othello.evaluate_both()
    game_score.value = "(You) " + str(player) + " - " + str(computer) + " (AI)"
    page.update()