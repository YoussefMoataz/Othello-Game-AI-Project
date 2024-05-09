from utils import *

class Othello:
    def __init__(self):
        self.di = [0, 1, 0, -1]
        self.dj = [1, 0, -1, 0]

        self.board = [[EMPTY for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = WHITE_DISK
        self.board[3][4] = self.board[4][3] = BLACK_DISK

        self.current_player = BLACK_DISK
        self.calculate_available_for(BLACK_DISK)

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()

    def is_in_board(self, i, j):
        return 0 <= i < 8 and 0 <= j < 8

    def set_available_around(self, i, j):
        for c in range(4):
            currenti = i + self.di[c]
            currentj = j + self.dj[c]
            if not self.is_in_board(currenti, currentj):
                continue
            if self.board[currenti][currentj] == EMPTY:
                if(self.can_outflank(currenti, currentj, -self.di[c], -self.dj[c], self.current_player)):
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
        for c in range(4):
            self.outflank_direction(i, j, self.di[c], self.dj[c], player)
        self.clear_available()
                
    def outflank_direction(self, i, j, di, dj, player):
        last_i, last_j = i, j
        opponent = self.get_opponent(player)
        flag = False
        
        for _ in range(1, 8):
            last_i += di
            last_j += dj
            
            if not self.is_in_board(last_i, last_j):
                break
            
            if self.board[last_i][last_j] == opponent:
                continue
            
            if self.board[last_i][last_j] == player:
                flag = True
                break

        if flag:
            while (i, j) != (last_i, last_j):
                self.board[i][j] = player
                i += di
                j += dj
    
    def can_outflank(self, i, j, di, dj, player):
        last_i, last_j = i, j
        opponent = self.get_opponent(player)
        flag = False
        
        for _ in range(1, 8):
            last_i += di
            last_j += dj
            
            if not self.is_in_board(last_i, last_j):
                break
            
            if self.board[last_i][last_j] == opponent:
                continue
            
            if self.board[last_i][last_j] == player:
                flag = True
                break

        return flag

    def player_clicked(self, i, j):
        if self.board[i][j] == AVAILABLE:
            self.board[i][j] = BLACK_DISK
            self.outflank(i, j, BLACK_DISK)
            # todo: calculate avilable for white, do white move, then calculate avilable for black
            self.calculate_available_for(BLACK_DISK)

if __name__ == "__main__":
    othello = Othello()
    othello.print_board()
