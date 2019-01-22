"""
Test module for ttt_computer.py
"""

# general imports
from ttt_game.ttt_computer import *
from ttt_game.ttt_board import *


def test_minimax_win_row():
    """
    x x o | x o x | o o
      x x |   o o | x x o
    o   o | x   x | x

    Test if computer can win the game with win case on a row of the board.
    """
    game_board = [[PLAYERX, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERX],
                  [PLAYERO, EMPTY, PLAYERO]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 1, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERX, PLAYERO, PLAYERX], [EMPTY, PLAYERO, PLAYERO],
                  [PLAYERX, EMPTY, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 1, "Bad Move X: " + str(move[0])
    assert move[1] == 0, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERO, PLAYERO, EMPTY], [PLAYERX, PLAYERX, PLAYERO],
                  [PLAYERX, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 0, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])


def test_minimax_win_col():
    """
    x     | x o o | o o x
    o o x |     o |   o x
    x o x | x o x | x

    Test if computer can win the game with win case on a column of the board.
    """
    game_board = [[PLAYERX, EMPTY, EMPTY], [PLAYERO, PLAYERO, PLAYERX],
                  [PLAYERX, PLAYERO, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERX)
    assert move[0] == 0, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERX, PLAYERO, PLAYERO], [EMPTY, EMPTY, PLAYERO],
                  [PLAYERX, PLAYERO, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERX)
    assert move[0] == 1, "Bad Move X: " + str(move[0])
    assert move[1] == 0, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERO, PLAYERO, PLAYERX], [EMPTY, PLAYERO, PLAYERX],
                  [PLAYERX, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERX)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])


def test_minimax_win_diag():
    """
    x x   | o x x
    o o x | x o
    o     | o

    Test if computer can win the game with win case on a diagonal of the board.
    """
    game_board = [[PLAYERX, PLAYERX, EMPTY], [PLAYERO, PLAYERO, PLAYERX],
                  [PLAYERO, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 0, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERO, PLAYERX, PLAYERX], [PLAYERX, PLAYERO, EMPTY],
                  [PLAYERO, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])


def test_minimax_def_row():
    """
    x x   | o x   | x o
    x o   | x x   | o
    o o x | o o x | x x

    Test if computer can defend with a opponent win case on a row of the board.
    """
    game_board = [[PLAYERX, PLAYERX, EMPTY], [PLAYERX, PLAYERO, EMPTY],
                  [PLAYERO, PLAYERO, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 0, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERO, PLAYERX, EMPTY], [PLAYERX, PLAYERX, EMPTY],
                  [PLAYERO, PLAYERO, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 1, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERX, PLAYERO, EMPTY], [PLAYERO, EMPTY, EMPTY],
                  [PLAYERX, PLAYERX, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])


def test_minimax_def_col():
    """
    x o x | o x o | o o x
    x x o | x x o | x o x
        o |     x |   x

    Test if computer can defend with a opponent win case on a column of the
    board.
    """
    game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERX, PLAYERX, PLAYERO],
                  [EMPTY, EMPTY, PLAYERO]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 0, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERO, PLAYERX, PLAYERO], [PLAYERX, PLAYERX, PLAYERO],
                  [EMPTY, EMPTY, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 1, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERO, PLAYERO, PLAYERX], [PLAYERX, PLAYERO, PLAYERX],
                  [EMPTY, PLAYERX, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])


def test_minimax_def_diag():
    """
    x o x | o o x
    x x o | x x o
    o     |     x

    Check if computer can defend with opponent win case on a diagonal of the
    board.
    """
    game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERX, PLAYERX, PLAYERO],
                  [PLAYERO, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 2, "Bad Move Y: " + str(move[1])

    game_board = [[PLAYERO, PLAYERO, PLAYERX], [PLAYERX, PLAYERX, PLAYERO],
                  [EMPTY, EMPTY, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    move = get_move(board, PLAYERO)
    assert move[0] == 2, "Bad Move X: " + str(move[0])
    assert move[1] == 0, "Bad Move Y: " + str(move[1])


if __name__ == '__main__':
    import pytest

    pytest.main(['test_ttt_computer.py'])
