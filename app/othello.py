from utils import *

class Othello:
    def __init__(self):
        self.board = [[EMPTY for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = WHITE_DISK
        self.board[3][4] = self.board[4][3] = BLACK_DISK
        self.calculate_available_for(BLACK_DISK)

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()

    def set_available_around(self, i, j):
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        for c in range(4):
            currenti = i + di[c]
            currentj = j + dj[c]
            if currenti < 0 or currentj < 0 or currenti > 7 or currentj > 7:
                continue
            if self.board[currenti][currentj] == EMPTY:
                self.board[currenti][currentj] = AVAILABLE


    def get_board_1d(self):
        board_1d = []
        for i in range(8):
            for j in range(8):
                board_1d.append(self.board[i][j])
        return board_1d
    
    def calculate_available_for(self, player):
        opponent = 0
        if player == BLACK_DISK:
            opponent = WHITE_DISK
        else:
            opponent = BLACK_DISK
        
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == opponent:
                    self.set_available_around(i, j)
    
    def player_clicked(self, i, j):
        if self.board[i][j] == AVAILABLE:
            self.board[i][j] = BLACK_DISK
            # todo: calculate avilable for white, do white move, then calculate avilable for black
            self.calculate_available_for(BLACK_DISK)

if __name__ == "__main__":
    othello = Othello()
    othello.print_board()
