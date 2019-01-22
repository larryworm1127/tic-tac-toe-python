"""
Module that runs the entire game
"""
from ttt_game.ttt_gui import game_loop
from ttt_game.ttt_computer import get_move
from ttt_game.ttt_board import PLAYERO

if __name__ == '__main__':
    game_loop(3, PLAYERO, get_move)
