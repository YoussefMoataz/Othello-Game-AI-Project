from utils import *

class Orthello:
    def __init__(self):
        self.board = [[EMPTY for _ in range(8)] for _ in range(8)]

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end="")
            print()

if __name__ == "__main__":
    orthello = Orthello()
    orthello.print_board()
