from constants import *
from board import Board
import copy
import random

class AI:
    def __init__(self, algorithm = "minimax"):
        self.algorithm = algorithm  # "random" or "minimax"
        self.player1 = 1
        self.player2 = 2
        self.eval_count = 0

    def get_ai_move(self, main_board):
        if self.algorithm == "random":
            # random choice
            score = "random"
            best_move = self.get_random_empty_square(main_board)
        else:
            # minimax choice
            self.eval_count = 0
            # AI player2 is_maximizing = False
            score, best_move = self.minimax(main_board, False)   
            print(f"{self.eval_count = }")

        print(f"AI has chosen square at position = {best_move} and eval = {score}")
        return best_move   # (row, col)

    def minimax(self, board, is_maximizing):
        game_state = board.get_game_state(board)
        # game_state = 0 --> no winner; 1 --> player 1 is winner; 2 --> player 2 is winner

        if game_state == 1: # player1 is_maximizing = True, therefore return 1
            self.eval_count += 1
            return 1, None   # score, move
        
        elif game_state == 2: # player2 is_minimizing = False, therefore return -1
            self.eval_count += 1
            return -1, None
        
        elif board.board_is_full():  # no winner and board full --> DRAW --> return 0
            self.eval_count += 1
            return 0, None
        
        if is_maximizing:
            # player1 turn
            max_score = -1000  # intialize with a value < 0
            best_move = None
            empty_squares = board.get_empty_squares()  # [ (row, col), (row, col), ... ]

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player1)
                # NEXT: player2 turn -->  is_maximizing = False
                score = self.minimax(temp_board, False)[0]  # returns: score, move

                if score > max_score:
                    max_score = score
                    best_move = (row, col)

            return max_score, best_move

        elif not is_maximizing:
            # player2 turn
            min_score = 1000  # intialize with a value > 1
            best_move = None
            empty_squares = board.get_empty_squares()

            for (row, col) in empty_squares:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player2)
                # NEXT: player1 turn -->  is_maximizing = True
                score = self.minimax(temp_board, True)[0]   # returns: score, move

                if score < min_score:
                    min_score = score
                    best_move = (row, col)

            return min_score, best_move

    def get_random_empty_square(self, board):
        """returns a random empty square"""
        empty_squares = board.get_empty_squares()  # [(row,col), (row,col), ...] of empty squares
        return random.choice(empty_squares)


