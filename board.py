import numpy as np
from constants import *

class Board:
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        """[[0. 0. 0.]
            [0. 0. 0.]
            [0. 0. 0.]]"""
        self.empty_squares = self.squares
        self.marked_squares = 0
        self.winning_line_type = ""         # for stirkethru line
        self.winning_line_number = None     # for stirkethru line

    def get_game_state(self, board):
        """ returns game_state
            game_state = 0 : no winner
            game_state = 1 : player 1 is winner
            game_state = 2 : player 2 is winner"""
        
        for player in range(1,3):
            for row in range(ROWS):
                if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] == player:
                    self.winning_line_type = "row"
                    self.winning_line_number = row
                    return player
                
            for col in range(COLS):
                if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] == player:
                    self.winning_line_type = "col"
                    self.winning_line_number = col
                    return player

            if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] == player:
                self.winning_line_type = "diag_top_bottom"
                return player
            
            if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] == player:
                self.winning_line_type = "diag_bottom_top"
                return player   
              
        return 0   # for no winner, return 0

    def mark_square(self, row, col, player):
        """marks selected empty square with either X or O"""
        self.squares[row][col] = player
        self.marked_squares += 1

    def board_is_full(self):
        """returns True if board is full"""
        return self.marked_squares == 9

    def square_is_empty(self, row, col):
        '''returns True if selected square is empty'''
        return self.squares[row][col] == 0
    
    def get_empty_squares(self):
        """returns a list with all empty squares = [(row, col), (row, col), ...]"""
        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.squares[row][col] == 0:
                    result.append((row, col))
        return result


