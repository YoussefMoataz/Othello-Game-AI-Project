import flet as ft
from app.ui_utils import *
from app.utils import *
from app.othello import *
import time

class Controller:
    def __init__(self, difficulty, page):
        self.board = ft.GridView(width=500, runs_count=8, expand=1)
        self.game_state = ft.Text(size=18)
        self.game_score = ft.Text(size=25)
        self.page = page
        self.othello = Othello(difficulty)
        self.create_board()

    def create_white_disk(self):
        return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH), ft.BorderSide(BORDER_WIDTH)), bgcolor=WHITE, margin=5)

    def create_black_disk(self):
        return ft.Container(border_radius=100, border=ft.Border(ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE), ft.BorderSide(BORDER_WIDTH, WHITE)), bgcolor=BLACK, margin=5)

    def create_available_square(self):
        return ft.Container(border=ft.Border(ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE), ft.BorderSide(2, WHITE)))

    def create_square_click_handler(self, index):
        def click(e):
            i, j = get_index_2d(index)
            # print("clicked index:", i, j)
            if(self.othello.player_clicked(i, j)):
                self.refresh_board()
                self.refresh_state()
                self.refresh_score()
                time.sleep(1)
                self.othello.apply_best_move()
                self.refresh_board()
                self.refresh_state()
                self.refresh_score()
        return click

    def create_board(self):

        for i in range(0, 64):
            click_handler = self.create_square_click_handler(i)
            self.board.controls.append(ft.Container(bgcolor=GREEN, on_click=click_handler))
        
        self.refresh_board()
        self.refresh_state()
        self.refresh_score()

    def refresh_board(self):
        board_orthello = self.othello.get_board_1d()

        for i in range(0, 64):
            self.board.controls[i].border = None
            if board_orthello[i] == AVAILABLE:
                self.board.controls[i].content = self.create_available_square()
            elif board_orthello[i] == WHITE_DISK:
                self.board.controls[i].content = self.create_white_disk()
            elif board_orthello[i] == BLACK_DISK:
                self.board.controls[i].content = self.create_black_disk()
            else:
                self.board.controls[i].content = None
        
        if not self.othello.last_played == -1:
            self.board.controls[self.othello.last_played].border = ft.Border(ft.BorderSide(2, "red"), ft.BorderSide(2, "red"), ft.BorderSide(2, "red"), ft.BorderSide(2, "red"))

        self.page.update()

    def refresh_state(self):
        if self.othello.state == STATE_PLAYER_TURN:
            self.game_state.value = "Player's turn"
        elif self.othello.state == STATE_AI_TURN:
            self.game_state.value = "AI making move ..."
        elif self.othello.state == STATE_NO_MORE_MOVES:
            self.game_state.value = "No more moves."
        elif self.othello.state == STATE_BLACK_WON:
            self.game_state.value = "You won!"
        elif self.othello.state == STATE_WHITE_WON:
            self.game_state.value = "AI won!"
        elif self.othello.state == STATE_DRAW:
            self.game_state.value = "Draw!"

        self.page.update()

    def refresh_score(self):
        player, computer = self.othello.evaluate_both()
        self.game_score.value = "(You) " + str(player) + " - " + str(computer) + " (AI)"
        self.page.update()