"""
Test module for ttt_board.py
"""

# general imports
from ttt_game.ttt_board import *


def test_clone():
    """Test if the clone method works and if the cloned does not get affect by
    its original board.
    """
    game_board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY],
                  [EMPTY, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    clone_board = board.clone()

    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            assert EMPTY == board.get_square(row, col)
            assert EMPTY == clone_board.get_square(row, col)

    board.move(1, 2, PLAYERX)
    assert EMPTY == clone_board.get_square(1, 2)


def test_switch_player():
    """Test if the switch player function works or not.
    """
    player = PLAYERX
    other_player = switch_player(player)
    assert PLAYERO == other_player

    player = PLAYERO
    other_player = switch_player(player)
    assert PLAYERX == other_player


def test_check_win_human():
    """
    x x x | x o   | x o
      o   | x   o | o x
    o     | x   o |   o x

    Test if check win method recognizes win situations for human.
    """
    game_board = [[PLAYERX, PLAYERX, PLAYERX], [EMPTY, PLAYERO, EMPTY],
                  [PLAYERO, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert PLAYERX == state

    game_board = [[PLAYERX, PLAYERO, EMPTY], [PLAYERX, EMPTY, PLAYERO],
                  [PLAYERX, EMPTY, PLAYERO]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert PLAYERX == state

    game_board = [[PLAYERX, PLAYERO, EMPTY], [PLAYERO, PLAYERX, EMPTY],
                  [EMPTY, PLAYERO, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert PLAYERX == state


def test_check_win_computer():
    """
    o o o | o x   | o x
      x   | o   x | x o
    x     | o   x |   x o

    Test if check win method recognizes win situations for computer.
    """
    game_board = [[PLAYERO, PLAYERO, PLAYERO], [EMPTY, PLAYERX, EMPTY],
                  [PLAYERX, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert PLAYERO == state

    game_board = [[PLAYERO, PLAYERX, EMPTY], [PLAYERO, EMPTY, PLAYERX],
                  [PLAYERO, EMPTY, PLAYERX]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert PLAYERO == state

    game_board = [[PLAYERO, PLAYERX, EMPTY], [PLAYERX, PLAYERO, EMPTY],
                  [EMPTY, PLAYERX, PLAYERO]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert PLAYERO == state


def test_check_win_draw():
    """
    x o x | x o x
    o o x | x o x
    x x o | o x o

    Test if check win method recognize draw situations.
    """
    game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERO, PLAYERO, PLAYERX],
                  [PLAYERX, PLAYERX, PLAYERO]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert DRAW == state

    game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERX, PLAYERO, PLAYERX],
                  [PLAYERO, PLAYERX, PLAYERO]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert DRAW == state


def test_check_win_playing():
    """
    x o   | x o x
    o   x | o x
    o     | o   o

    Test if check win method recognize that the game is still playing.
    """
    game_board = [[PLAYERX, PLAYERO, EMPTY], [PLAYERO, EMPTY, PLAYERX],
                  [PLAYERO, EMPTY, EMPTY]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert None is state

    game_board = [[PLAYERX, PLAYERO, PLAYERX], [PLAYERO, PLAYERX, EMPTY],
                  [PLAYERO, EMPTY, PLAYERO]]
    board = TTTBoard(3, _custom_board=game_board)
    state = board.check_win()
    assert None is state
