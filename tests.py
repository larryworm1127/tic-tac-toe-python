# general imports
from unittest import TestCase

from ttt_board import *


class TestTTTBoard(TestCase):
    def test_clone(self):
        game_board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        clone_board = board.clone()

        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                self.assertEqual(EMPTY, board.get_square(row, col))
                self.assertEqual(EMPTY, clone_board.get_square(row, col))

        board.move(1, 2, HUMAN)
        self.assertEqual(EMPTY, clone_board.get_square(1, 2))

    def test_switch_player(self):
        player = HUMAN
        other_player = switch_player(player)
        self.assertEqual(COMPUTER, other_player)

        player = COMPUTER
        other_player = switch_player(player)
        self.assertEqual(HUMAN, other_player)

    def test_check_win_human(self):
        """
        x x x | x o   | x o
          o   | x   o | o x
        o     | x   o |   o x

        Check if check win method recognizes win situations for human
        """
        game_board = [[HUMAN, HUMAN, HUMAN], [EMPTY, COMPUTER, EMPTY], [COMPUTER, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(HUMAN, state)

        game_board = [[HUMAN, COMPUTER, EMPTY], [HUMAN, EMPTY, COMPUTER], [HUMAN, EMPTY, COMPUTER]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(HUMAN, state)

        game_board = [[HUMAN, COMPUTER, EMPTY], [COMPUTER, HUMAN, EMPTY], [EMPTY, COMPUTER, HUMAN]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(HUMAN, state)

    def test_check_win_computer(self):
        """
        o o o | o x   | o x
          x   | o   x | x o
        x     | o   x |   x o

        Check if check win method recognizes win situations for computer
        """
        game_board = [[COMPUTER, COMPUTER, COMPUTER], [EMPTY, HUMAN, EMPTY], [HUMAN, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(COMPUTER, state)

        game_board = [[COMPUTER, HUMAN, EMPTY], [COMPUTER, EMPTY, HUMAN], [COMPUTER, EMPTY, HUMAN]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(COMPUTER, state)

        game_board = [[COMPUTER, HUMAN, EMPTY], [HUMAN, COMPUTER, EMPTY], [EMPTY, HUMAN, COMPUTER]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(COMPUTER, state)

    def test_check_win_draw(self):
        """
        x o x
        o o x
        x x o

        Check if check win method recognize draw situations
        """
        game_board = [[HUMAN, COMPUTER, HUMAN], [COMPUTER, COMPUTER, HUMAN], [HUMAN, HUMAN, COMPUTER]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(DRAW, state)

    def test_check_win_playing(self):
        """
        x o
        o   x
        o

        Check if check win method recognize that the game is still playing
        """
        game_board = [[HUMAN, COMPUTER, EMPTY], [COMPUTER, EMPTY, HUMAN], [COMPUTER, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(None, state)


class TestTTTComputer(TestCase):
    pass
