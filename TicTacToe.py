# https://youtu.be/Bk9hlNZc6sE
# Coding Spot - Coding an Unbeatable Tic Tac Toe AI Using Python and the Minimax Algorithm
# adding this new comment to practice git checkin / checkout

from constants import *
from board import Board
from game import Game
from ai import AI
import sys
import pygame
import time

def main():
    game = Game()
    board = Board()
    ai = AI()

    number_of_players = 1       # 1 or 2
    
    if number_of_players == 1:
        game.game_mode = "ai"   # "two_players" or "ai"
        ai.level = "minimax"    # "random" or "minimax"
    else:
        game.game_mode = "two_players"   # "two_players" or "ai"

    while game.playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                pygame.quit()
                sys.exit()

            if ( (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.KEYDOWN) ):
                # returns (x,y) in pixels, (0,0) = upper right corner
                pos_xy_pixels = pygame.mouse.get_pos()
                row = pos_xy_pixels[1] // SQ_SIZE
                col = pos_xy_pixels[0] // SQ_SIZE

                if board.square_is_empty(row, col):
                    game.play_turn(board, row, col)

        if game.playing and game.game_mode == "ai" and game.player == ai.player2:
            pygame.display.update()
            time.sleep(0.75)  # wait time before ai player2's turn

            row, col = ai.get_ai_move(board)
            game.play_turn(board, row, col)

        pygame.display.update()

    if game.playing == False:
        time.sleep(2)
        pygame.quit()
        sys.exit()
       
if __name__=="__main__":
    main()
