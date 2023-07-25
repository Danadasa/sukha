from constants import *
from board import Board
from ai import AI
import pygame

pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT + STATUS_BAR_HEIGHT) )
pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(BG_COLOR)

class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1  # player1 = X, player2 = O
        self.game_mode = "ai"   # "pvp" or "ai"
        self.status = "Turn: Player X"
        self.playing = True
        self.draw_status_bar()
        self.draw_lines()

    def draw_status_bar(self):
        """Draws a status bar at the bottom of the win."""
        pygame.draw.rect(screen, LINE_COLOR, (0, HEIGHT, WIDTH, STATUS_BAR_HEIGHT))
        font = pygame.font.Font(None, STATUS_BAR_FONT_SIZE)
        text_surface = font.render(self.status, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.right = WIDTH - STATUS_BAR_TEXT_PADDING
        text_rect.top = HEIGHT + STATUS_BAR_TEXT_PADDING
        screen.blit(text_surface, text_rect) 

    def draw_lines(self):
        """draws lines to divide board into 9 squares"""
        pygame.draw.line(screen, LINE_COLOR, (SQ_SIZE,0), (SQ_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQ_SIZE,0), (WIDTH - SQ_SIZE, HEIGHT), LINE_WIDTH)
       
        pygame.draw.line(screen, LINE_COLOR, (0, SQ_SIZE), (WIDTH, SQ_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQ_SIZE), (WIDTH, HEIGHT - SQ_SIZE), LINE_WIDTH)

    def draw_player_symbol(self, row, col):
        """draws X for player1 and O for player2"""
        if self.player == 1:
            # draw X
            start_top_left = (col * SQ_SIZE + SQ_SIZE // 4, row * SQ_SIZE + SQ_SIZE // 4)
            end_bottom_right = (col * SQ_SIZE + int(SQ_SIZE * 3/4), row * SQ_SIZE + int(SQ_SIZE * 3/4))

            start_bottom_left = (col * SQ_SIZE + SQ_SIZE // 4, row * SQ_SIZE + int(SQ_SIZE * 3/4))
            end_top_right = (col * SQ_SIZE + int(SQ_SIZE * 3/4), row * SQ_SIZE + SQ_SIZE // 4)

            pygame.draw.line(screen, CROSS_LINE_COLOR, start_top_left, end_bottom_right, CROSS_LINE_WIDTH)
            pygame.draw.line(screen, CROSS_LINE_COLOR, start_bottom_left, end_top_right, CROSS_LINE_WIDTH)
        
        elif self.player == 2:
            # draw O
            center = (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2)
            pygame.draw.circle(screen, CIRCLE_LINE_COLOR, center, RADIUS, CIRCLE_LINE_WIDTH)

    def draw_strike_thru(self, winning_line_type, winning_line_number):
        """draws a strike thru line thru the winning line"""
        if winning_line_type == "row":
            winning_row = winning_line_number
            start = (0, winning_row * SQ_SIZE + SQ_SIZE // 2)
            end =   (WIDTH, winning_row * SQ_SIZE + SQ_SIZE // 2)
            pygame.draw.line(screen, STRIKE_THRU_COLOR, start, end, STRIKE_THRU_WIDTH)

        if winning_line_type == "col":
            winning_col = winning_line_number
            start = (winning_col * SQ_SIZE + SQ_SIZE // 2, 0)
            end =   (winning_col * SQ_SIZE + SQ_SIZE // 2, HEIGHT)
            pygame.draw.line(screen, STRIKE_THRU_COLOR, start, end, STRIKE_THRU_WIDTH)
            
        if winning_line_type == "diag_top_bottom":
            start = (0, 0)
            end =   (WIDTH, HEIGHT)
            pygame.draw.line(screen, STRIKE_THRU_COLOR, start, end, STRIKE_THRU_WIDTH)

        if winning_line_type == "diag_bottom_top":
            start = (0, HEIGHT)
            end =   (WIDTH, 0)
            pygame.draw.line(screen, STRIKE_THRU_COLOR, start, end, STRIKE_THRU_WIDTH)

    def play_turn(self, board, row, col):
        """marks board, draws symbol, and checks game_state"""
        board.mark_square(row, col, self.player)
        self.draw_player_symbol(row, col)

        game_state = board.get_game_state(board)
        # game_state: 0 = no winner, 1 = player1 winner, 2 = player2 winner

        if game_state == 0 and board.board_is_full():
            self.playing = False
            self.status = "DRAW!"
            self.draw_status_bar()
        elif game_state != 0:
            self.playing = False
            self.draw_strike_thru(board.winning_line_type, board.winning_line_number)
            symbol = "X" if self.player == 1 else "O"
            self.status = (f"WINNER!: player {symbol}")
            self.draw_status_bar()
        else:
            self.change_turn()
            self.status = "Turn: Player X" if self.player == 1 else "Turn: Player O"
            self.draw_status_bar()

    def change_turn(self):
        """changes turn and updates status bar"""
        self.player = self.player % 2 + 1
