"""
GUI module for Tic Tac Toe game
"""

# general imports
import pygame
import math

from dataclasses import dataclass, field
from typing import Any

from ttt_game.ttt_board import *

# init pygame
pygame.init()

# GUI constants
GUI_WIDTH = 400
GUI_HEIGHT = 500
BAR_WIDTH = 5

# Colour constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)


@dataclass
class TTTGUI:
    """
    GUI for Tic Tac Toe game.
    """

    # variables with passed in values
    size: int
    ai_player: int
    human_player: int
    ai_function: Any
    screen: pygame.Surface

    # default game variables
    reverse: bool = False
    bar_spacing: int = field(init=False)

    # start new game
    board: TTTBoard = field(init=False)
    in_progress: bool = True
    wait: bool = False
    turn: int = PLAYERX
    message: str = "X Turn!"

    def __post_init__(self):
        """
        Initialize any variables that requires other var to be initialized
        """
        self.bar_spacing = GUI_WIDTH // self.size
        self.board = TTTBoard(self.size, self.reverse)

    def new_game(self):
        """
        Run game loop and start new game
        """
        self.screen.fill(black)
        game_loop(self.size, self.ai_player, self.ai_function, self.reverse)

    def click(self):
        """
        Make human move.
        """
        # get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # change status message
        if self.message == "X Turn!":
            self.message = "O Turn!"

        # draw player icon and check win
        if self.in_progress and (self.turn == self.human_player):
            row, col = self.get_grid_from_coords((mouse_pos[0], mouse_pos[1] - 100))

            # only move if the square is empty
            if self.board.get_square(row, col) == EMPTY:
                self.board.move(row, col, self.human_player)
                self.turn = self.ai_player

                # check winner
                winner = self.board.check_win()
                if winner is not None:
                    self.game_over(winner)
                self.wait = True

    def aimove(self):
        """
        Make AI move.
        """
        # change message
        if self.message == "O Turn!":
            self.message = "X Turn!"

        # draw computer icon and check win
        if self.in_progress and (self.turn == self.ai_player):
            row, col = self.ai_function(self.board, self.ai_player)

            # only move if the square is empty
            if self.board.get_square(row, col) == EMPTY:
                self.board.move(row, col, self.ai_player)
            self.turn = self.human_player

            # check winner
            winner = self.board.check_win()
            if winner is not None:
                self.game_over(winner)

    def game_over(self, winner):
        """
        Game over
        """
        # Display winner
        if winner == DRAW:
            self.message = "It's a tie!"
        elif winner == PLAYERX:
            self.message = "X Wins!"
        elif winner == PLAYERO:
            self.message = "O Wins!"

        # Game is no longer in progress
        self.in_progress = False

    def get_message(self):
        """
        Return the in-game message
        """
        return self.message

    def get_coords_from_grid(self, row, col):
        """
        Given a grid position in the form (row, col), returns
        the coordinates on the canvas of the center of the grid.
        """
        # X coordinate = (bar spacing) * (col + 1/2)
        # Y coordinate = height - (bar spacing) * (row + 1/2)
        return (self.bar_spacing * (col + 1.0 / 2.0),  # x
                self.bar_spacing * (row + 1.0 / 2.0))  # y

    def get_grid_from_coords(self, position):
        """
        Given coordinates on a canvas, gets the indices of
        the grid.
        """
        pos_x, pos_y = position
        return (pos_y // self.bar_spacing,  # row
                pos_x // self.bar_spacing)  # col

    def drawx(self, pos):
        """
        Draw an X on the given canvas at the given position.
        """
        half_size = .4 * self.bar_spacing
        pygame.draw.line(self.screen, black, (pos[0] - half_size, pos[1] - half_size),
                         (pos[0] + half_size, pos[1] + half_size), BAR_WIDTH)
        pygame.draw.line(self.screen, black, (pos[0] + half_size, pos[1] - half_size),
                         (pos[0] - half_size, pos[1] + half_size), BAR_WIDTH)

    def drawo(self, pos):
        """
        Draw an O on the given canvas at the given position.
        """
        half_size = .4 * self.bar_spacing
        pygame.draw.circle(self.screen, black, (math.ceil(pos[0]), math.ceil(pos[1])), math.ceil(half_size), BAR_WIDTH)

    def draw(self):
        """
        Updates the tic-tac-toe GUI.
        """
        # Draw in new game button
        self.button_object("New Game", 250, 20, 120, 50, green, bright_green, self.new_game)

        # Draw in bar lines
        for bar_start in range(0, GUI_WIDTH - 1, self.bar_spacing):
            pygame.draw.line(self.screen, black, (bar_start, 100), (bar_start, GUI_HEIGHT), BAR_WIDTH)
            pygame.draw.line(self.screen, black, (0, bar_start + 100), (GUI_WIDTH, bar_start + 100), BAR_WIDTH)

        # Draw the current players' moves
        for row in range(self.size):
            for col in range(self.size):
                symbol = self.board.get_square(row, col)
                coords = self.get_coords_from_grid(row, col)
                if symbol == PLAYERX:
                    self.drawx((coords[0], coords[1] + 100))
                elif symbol == PLAYERO:
                    self.drawo((coords[0], coords[1] + 100))

        # Run AI, if necessary
        if not self.wait:
            self.aimove()
        else:
            self.wait = False

    def message_display(self):
        """
        Displays message onto the screen
        """
        # set font and draw message onto screen
        font = pygame.font.Font('freesansbold.ttf', 30)
        text_surf, text_rect = text_objects(self.message, font)
        text_rect.center = (100, 50)
        self.screen.blit(text_surf, text_rect)

        # update display
        pygame.display.update()

    def button_object(self, text, x, y, width, height, init_color, active_color, action=None):
        """
        New game button handler
        """
        # get mouse state
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # change button color when hovered
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.screen, active_color, (x, y, width, height))

            # check whether the button is clicked or not
            if click[0] == 1 and action is not None:
                action()

        # switch button color to original
        else:
            pygame.draw.rect(self.screen, init_color, (x, y, width, height))

        # set font for button
        font = pygame.font.Font('freesansbold.ttf', 18)
        text_surf, text_rect = text_objects(text, font)
        text_rect.center = (310, 45)
        self.screen.blit(text_surf, text_rect)


def text_objects(text, font):
    """
    Create a text object given a message and a font
    """
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def game_loop(size, ai_player, ai_function, reverse=False):
    """
    Main game loop
    """
    # init pygame variables
    screen = pygame.display.set_mode((GUI_WIDTH, GUI_HEIGHT))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Tic Tac Toe")
    gui_class = TTTGUI(size, ai_player, switch_player(ai_player), ai_function, screen, reverse)

    # main game loop
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                quit()

        # set screen background
        screen.fill(white)
        gui_class.draw()

        # set mouse handler
        mouse_press = pygame.mouse.get_pressed()
        if mouse_press[0] == 1:
            gui_class.click()

        # display message
        gui_class.message_display()

        # update screen and clock
        pygame.display.update()
        clock.tick(60)
