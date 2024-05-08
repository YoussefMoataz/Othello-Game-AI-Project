from utils import *

class Orthello:
    def __init__(self):
        self.board = [[EMPTY for _ in range(8)] for _ in range(8)]

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()

    def set_available(self, i, j):
        self.board[i][j] = AVAILABLE

    def get_board_1d(self):
        board_1d = []
        for i in range(8):
            for j in range(8):
                board_1d.append(self.board[i][j])
        return board_1d

if __name__ == "__main__":
    orthello = Orthello()
    orthello.print_board()
