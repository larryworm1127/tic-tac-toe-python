# general imports
from unittest import TestCase

from ttt_board import *
from ttt_computer import *


class TestTTTBoard(TestCase):
    def test_clone(self):
        game_board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        clone_board = board.clone()

        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                self.assertEqual(EMPTY, board.get_square(row, col))
                self.assertEqual(EMPTY, clone_board.get_square(row, col))

        board.move(1, 2, PLAYERX)
        self.assertEqual(EMPTY, clone_board.get_square(1, 2))

    def test_switch_player(self):
        player = PLAYERX
        other_player = switch_player(player)
        self.assertEqual(PLAYERO, other_player)

        player = PLAYERO
        other_player = switch_player(player)
        self.assertEqual(PLAYERX, other_player)

    def test_check_win_human(self):
        """
        x x x | x o   | x o
          o   | x   o | o x
        o     | x   o |   o x

        Check if check win method recognizes win situations for human
        """
        game_board = [[PLAYERX, PLAYERX, PLAYERX], [EMPTY, PLAYERO, EMPTY], [PLAYERO, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(PLAYERX, state)

        game_board = [[PLAYERX, PLAYERO, EMPTY], [PLAYERX, EMPTY, PLAYERO], [PLAYERX, EMPTY, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(PLAYERX, state)

        game_board = [[PLAYERX, PLAYERO, EMPTY], [PLAYERO, PLAYERX, EMPTY], [EMPTY, PLAYERO, PLAYERX]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(PLAYERX, state)

    def test_check_win_computer(self):
        """
        o o o | o x   | o x
          x   | o   x | x o
        x     | o   x |   x o

        Check if check win method recognizes win situations for computer
        """
        game_board = [[PLAYERO, PLAYERO, PLAYERO], [EMPTY, PLAYERX, EMPTY], [PLAYERX, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(PLAYERO, state)

        game_board = [[PLAYERO, PLAYERX, EMPTY], [PLAYERO, EMPTY, PLAYERX], [PLAYERO, EMPTY, PLAYERX]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(PLAYERO, state)

        game_board = [[PLAYERO, PLAYERX, EMPTY], [PLAYERX, PLAYERO, EMPTY], [EMPTY, PLAYERX, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(PLAYERO, state)

    def test_check_win_draw(self):
        """
        x o x | x o x
        o o x | x o x
        x x o | o x o

        Check if check win method recognize draw situations
        """
        game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERO, PLAYERO, PLAYERX], [PLAYERX, PLAYERX, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(DRAW, state)

        game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERX, PLAYERO, PLAYERX], [PLAYERO, PLAYERX, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(DRAW, state)

    def test_check_win_playing(self):
        """
        x o   | x o x
        o   x | o x
        o     | o   o

        Check if check win method recognize that the game is still playing
        """
        game_board = [[PLAYERX, PLAYERO, EMPTY], [PLAYERO, EMPTY, PLAYERX], [PLAYERO, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(None, state)

        game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERO, PLAYERX, EMPTY], [PLAYERO, EMPTY, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        state = board.check_win()
        self.assertEqual(None, state)


class TestTTTComputer(TestCase):
    def test_minimax_win_row(self):
        """
        x x o | x o x | o o        o o x | o x o | x x
          x x |   o o | x x o        o o |   x x | o o x
        o   o | x   x | x          x   x | o   o | o

        Check if computer knows how to win the game with win case on a row of the board
        """
        game_board = [[PLAYERX, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERX], [PLAYERO, EMPTY, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 2, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 1, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERX, PLAYERO, PLAYERX], [EMPTY, PLAYERO, PLAYERO], [PLAYERX, EMPTY, PLAYERX]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 1, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 0, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERO, PLAYERO, EMPTY], [PLAYERX, PLAYERX, PLAYERO], [PLAYERX, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 0, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERO, PLAYERO, PLAYERX], [EMPTY, PLAYERO, PLAYERO], [PLAYERX, EMPTY, PLAYERX]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERX)[1]
        self.assertEqual(move[0], 2, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 1, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERO, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERX], [PLAYERO, EMPTY, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERX)[1]
        self.assertEqual(move[0], 1, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 0, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERX, PLAYERX, EMPTY], [PLAYERO, PLAYERO, PLAYERX], [PLAYERO, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERX)[1]
        self.assertEqual(move[0], 0, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

    def test_minimax_win_col(self):
        """
        x     | x o o | o o x      o     | o x x | x x o
        o o x |     o |   o x      x x o |     x |   x o
        x o x | x o x | x          o x o | o   o | o

        Check if computer knows how to win the game with win case on a column of the board
        """
        game_board = [[PLAYERX, EMPTY, EMPTY], [PLAYERO, PLAYERO, PLAYERX], [PLAYERX, PLAYERO, PLAYERX]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERX)[1]
        self.assertEqual(move[0], 0, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERX, PLAYERO, PLAYERO], [EMPTY, EMPTY, PLAYERO], [PLAYERX, PLAYERO, PLAYERX]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERX)[1]
        self.assertEqual(move[0], 1, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 0, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERO, PLAYERO, PLAYERX], [EMPTY, PLAYERO, PLAYERX], [PLAYERX, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERX)[1]
        self.assertEqual(move[0], 2, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERO, EMPTY, EMPTY], [PLAYERX, PLAYERX, PLAYERO], [PLAYERO, PLAYERX, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 0, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERO, PLAYERX, PLAYERX], [EMPTY, EMPTY, PLAYERX], [PLAYERO, EMPTY, PLAYERO]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 1, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 0, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERX, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERO], [PLAYERO, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 2, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

    def test_minimax_win_diag(self):
        """
        x x   | o x x      o o   | x o o
        o o x | x o        x x o | o x
        o     | o          x     | x

        Check if computer knows how to win the game with win case on a diagonal of the board
        """
        game_board = [[PLAYERX, PLAYERX, EMPTY], [PLAYERO, PLAYERO, PLAYERX], [PLAYERO, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 0, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERO, PLAYERX, PLAYERX], [PLAYERX, PLAYERO, EMPTY], [PLAYERO, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 2, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERO, PLAYERO, EMPTY], [PLAYERX, PLAYERX, PLAYERO], [PLAYERX, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 0, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))

        game_board = [[PLAYERX, PLAYERO, PLAYERO], [PLAYERO, PLAYERX, EMPTY], [PLAYERX, EMPTY, EMPTY]]
        board = TTTBoard(3, board=game_board)
        move = get_move(board, PLAYERO)[1]
        self.assertEqual(move[0], 2, "Bad Move X: " + str(move[0]))
        self.assertEqual(move[1], 2, "Bad Move Y: " + str(move[1]))
