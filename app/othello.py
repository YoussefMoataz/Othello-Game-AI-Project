from utils import *

class Othello:
    def __init__(self):
        self.board = [[EMPTY for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = WHITE_DISK
        self.board[3][4] = self.board[4][3] = BLACK_DISK
        self.calculate_available_for(BLACK_DISK)

        self.current_player = BLACK_DISK

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()

    def is_in_board(self, i, j):
        return 0 <= i < 8 and 0 <= j < 8

    def set_available_around(self, i, j):
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        for c in range(4):
            currenti = i + di[c]
            currentj = j + dj[c]
            if not self.is_in_board(currenti, currentj):
                continue
            if self.board[currenti][currentj] == EMPTY:
                self.board[currenti][currentj] = AVAILABLE

    def get_board_1d(self):
        board_1d = []
        for i in range(8):
            for j in range(8):
                board_1d.append(self.board[i][j])
        return board_1d
    
    def get_opponent(self, player):
        opponent = 0
        if player == BLACK_DISK:
            opponent = WHITE_DISK
        else:
            opponent = BLACK_DISK
        return opponent
    
    def calculate_available_for(self, player):
        opponent = self.get_opponent(player)
        
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == opponent:
                    self.set_available_around(i, j)
    
    def clear_available(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == AVAILABLE:
                    self.board[i][j] = EMPTY
        
    def outflank(self, i, j, player):
        self.outflank_right(i, j, player)
        self.outflank_left(i, j, player)
        self.outflank_up(i, j, player)
        self.outflank_down(i, j, player)
        self.clear_available()
            
    def outflank_right(self, i, j, player):
        last_i, last_j = i, j

        opponent = self.get_opponent(player)

        flag = False
        for c in range(1, 8):
            last_j = j + c
            if not self.is_in_board(last_i, last_j):
                break

            if self.board[last_i][last_j] == opponent:
                continue
            
            if self.board[last_i][last_j] == player:
                flag = True
                break

        # print(i, j, last_i, last_j)

        if flag:
            for c in range(j, last_j):
                self.board[last_i][c] = player
                
    def outflank_left(self, i, j, player):
        last_i, last_j = i, j

        opponent = self.get_opponent(player)

        flag = False
        for c in range(1, 8):
            last_j = j - c
            if not self.is_in_board(last_i, last_j):
                break

            if self.board[last_i][last_j] == opponent:
                continue
            
            if self.board[last_i][last_j] == player:
                flag = True
                break

        # print(i, j, last_i, last_j)

        if flag:
            for c in range(last_j, j):
                self.board[last_i][c] = player
    
    def outflank_up(self, i, j, player):
        last_i, last_j = i, j

        opponent = self.get_opponent(player)

        flag = False
        for c in range(1, 8):
            last_i = i - c
            if not self.is_in_board(last_i, last_j):
                break

            if self.board[last_i][last_j] == opponent:
                continue
            
            if self.board[last_i][last_j] == player:
                flag = True
                break

        # print(i, j, last_i, last_j)

        if flag:
            for c in range(last_i, i):
                self.board[c][last_j] = player
    
    def outflank_down(self, i, j, player):
        last_i, last_j = i, j

        opponent = self.get_opponent(player)

        flag = False
        for c in range(1, 8):
            last_i = i + c
            if not self.is_in_board(last_i, last_j):
                break

            if self.board[last_i][last_j] == opponent:
                continue
            
            if self.board[last_i][last_j] == player:
                flag = True
                break

        # print(i, j, last_i, last_j)

        if flag:
            for c in range(i, last_i):
                self.board[c][last_j] = player

    def player_clicked(self, i, j):
        if self.board[i][j] == AVAILABLE:
            self.board[i][j] = BLACK_DISK
            self.outflank(i, j, BLACK_DISK)
            # todo: calculate avilable for white, do white move, then calculate avilable for black
            self.calculate_available_for(BLACK_DISK)

if __name__ == "__main__":
    othello = Othello()
    othello.print_board()
