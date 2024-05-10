from app.utils import *

class Othello:
    def __init__(self, difficulty = DIFF_MEDIUM):
        self.di = [0, 1, 0, -1]
        self.dj = [1, 0, -1, 0]

        self.depth = 0

        if difficulty == DIFF_EASY:
            self.depth = DEPTH_EASY
        elif difficulty == DIFF_MEDIUM:
            self.depth = DEPTH_MEDIUM
        elif difficulty == DIFF_HARD:
            self.depth = DEPTH_HARD

        self.board = [[EMPTY for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = WHITE_DISK
        self.board[3][4] = self.board[4][3] = BLACK_DISK

        self.last_played = -1

        self.calculate_available_for(BLACK_DISK, self.board)

        self.state = STATE_PLAYER_TURN

    def print_board(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()

    def is_in_board(self, i, j):
        return 0 <= i < 8 and 0 <= j < 8

    def set_available_around(self, i, j, player, board):
        for c in range(4):
            currenti = i + self.di[c]
            currentj = j + self.dj[c]
            if not self.is_in_board(currenti, currentj):
                continue
            if board[currenti][currentj] == EMPTY:
                if(self.can_outflank(currenti, currentj, -self.di[c], -self.dj[c], player, board)):
                    board[currenti][currentj] = AVAILABLE

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
    
    def calculate_available_for(self, player, board):
        opponent = self.get_opponent(player)
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == opponent:
                    self.set_available_around(i, j, player, board)

    def get_available_moves(self, board):
        avail = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == AVAILABLE:
                    avail.append((i, j))
        return avail
                    
    def clear_available(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == AVAILABLE:
                    board[i][j] = EMPTY
        
    def outflank(self, i, j, player, board):
        for c in range(4):
            self.outflank_direction(i, j, self.di[c], self.dj[c], player, board)
        self.clear_available(board)
                
    def outflank_direction(self, i, j, di, dj, player, board):
        last_i, last_j = i, j
        opponent = self.get_opponent(player)
        flag = False
        
        for _ in range(8):
            last_i += di
            last_j += dj
            
            if not self.is_in_board(last_i, last_j):
                break

            if board[last_i][last_j] == EMPTY or board[last_i][last_j] == AVAILABLE:
                break
            
            if board[last_i][last_j] == opponent:
                continue
            
            if board[last_i][last_j] == player:
                flag = True
                break

        if flag:
            while (i, j) != (last_i, last_j):
                board[i][j] = player
                i += di
                j += dj
    
    def can_outflank(self, i, j, di, dj, player, board):
        last_i, last_j = i, j
        opponent = self.get_opponent(player)
        flag = False
        
        for _ in range(8):
            last_i += di
            last_j += dj
            
            if not self.is_in_board(last_i, last_j):
                break

            if board[last_i][last_j] == EMPTY or board[last_i][last_j] == AVAILABLE:
                break
            
            if board[last_i][last_j] == opponent:
                continue
            
            if board[last_i][last_j] == player:
                flag = True
                break

        return flag
    
    def is_moves_left(self):
        for i in range(8) : 
            for j in range(8) : 
                if (self.board[i][j] == EMPTY) : 
                    return True 
        return False
    
    def evaluate_both(self):
        player, computer = 0, 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == BLACK_DISK:
                    player += 1
                elif self.board[i][j] == WHITE_DISK:
                    computer += 1
        return player, computer

    def evaluate(self, board, player):
        opponent = self.get_opponent(player)
        score = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == player:
                    score += 1
                elif board[i][j] == opponent:
                    score -= 1
        return score
    
    def minimax(self, board, depth, alpha, beta, player):

        if depth == self.depth or self.get_available_moves(board) == []:
            return self.evaluate(board, self.get_opponent(player))
        
        best = 0
        if player == BLACK_DISK:
            best = float("-inf")

            avail = self.get_available_moves(board)

            for (i, j) in avail:
                board[i][j] = BLACK_DISK
                state = [row[:] for row in board]
                self.outflank(i, j, BLACK_DISK, state)
                self.calculate_available_for(WHITE_DISK, state)

                best = max(best, self.minimax(state, depth+1, alpha, beta, WHITE_DISK))
                alpha = max(alpha, best)

                board[i][j] = AVAILABLE

                if beta <= alpha:
                    break

        else:
            best = float("inf")

            avail = self.get_available_moves(board)

            for (i, j) in avail:
                board[i][j] = WHITE_DISK
                state = [row[:] for row in board]
                self.outflank(i, j, WHITE_DISK, state)
                self.calculate_available_for(BLACK_DISK, state)

                best = min(best, self.minimax(state, depth+1, alpha, beta, BLACK_DISK))
                beta = min(beta, best)

                board[i][j] = AVAILABLE

                if beta <= alpha:
                    break

        return best
    
    def get_best_move(self):

        self.calculate_available_for(WHITE_DISK, self.board)

        x, y = -1, -1

        avail = self.get_available_moves(self.board)
        if avail == []:
            return x, y
        
        # print(avail)

        state = [[EMPTY for _ in range(8)] for _ in range(8)]

        for i in range(8):
            for j in range(8):
                state[i][j] = self.board[i][j]

        score = float("-inf")

        for (i, j) in avail:
            res = self.minimax(state, 0, MIN, MAX, WHITE_DISK)

            if res > score:
                score = res
                x, y = i, j

        # print(score, x, y)

        return x, y
    
    def is_terminal_state(self):

        self.calculate_available_for(BLACK_DISK, self.board)
        avail_black = self.get_available_moves(self.board)
        self.clear_available(self.board)

        self.calculate_available_for(WHITE_DISK, self.board)
        avail_white = self.get_available_moves(self.board)
        self.clear_available(self.board)

        return avail_black == avail_white == []


    def apply_best_move(self):
        avail = []
        while avail == []:
            x, y = self.get_best_move()
            if x > -1 and y > -1:
                self.board[x][y] = WHITE_DISK
                self.outflank(x, y, WHITE_DISK, self.board)
                self.last_played = x * 8 + y
                # print(x, y)
            self.clear_available(self.board)
            self.calculate_available_for(BLACK_DISK, self.board)
            avail = self.get_available_moves(self.board)
            if not avail == []:
                self.state = STATE_PLAYER_TURN
                return
            
            if self.is_terminal_state():
                p, c = self.evaluate_both()
                if p > c:
                    self.state = STATE_BLACK_WON
                elif p < c:
                    self.state = STATE_WHITE_WON
                else:
                    self.state = STATE_DRAW
                break
            
    def player_clicked(self, i, j):
        if self.board[i][j] == AVAILABLE:
            self.board[i][j] = BLACK_DISK
            self.outflank(i, j, BLACK_DISK, self.board)
            self.last_played = i * 8 + j
            self.state = STATE_AI_TURN
