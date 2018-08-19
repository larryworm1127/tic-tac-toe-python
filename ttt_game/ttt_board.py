"""
Virtual Tic-Tac-Toe Board
"""

# General imports
from dataclasses import dataclass, field

__all__ = ['TTTBoard', 'EMPTY', 'PLAYERX', 'PLAYERO', 'DRAW', 'STRMAP', 'switch_player']

# Constants
EMPTY = 0
PLAYERX = 1
PLAYERO = 2
DRAW = 3

# Map player constants to letters for printing
STRMAP = {PLAYERX: 'X',
          PLAYERO: 'O',
          EMPTY: ' '}


@dataclass
class TTTBoard:
    """
    A class representing TTT board
    """

    _dim: int
    _reverse: bool = False
    _custom_board: list = None
    _board: list = field(init=False)

    def __post_init__(self):
        """
        Initialize any variables that requires other var to be initialized
        """
        if self._custom_board is None:
            # Create empty board
            self._board = [[EMPTY for _ in range(self._dim)]
                           for _ in range(self._dim)]
        else:
            # Copy board grid
            self._board = [[self._custom_board[row][col] for col in range(self._dim)]
                           for row in range(self._dim)]

    def __str__(self):
        """
        Human readable representation of the board.
        """
        rep = ""
        for row in range(self._dim):
            for col in range(self._dim):
                rep += STRMAP[self._board[row][col]]
                if col == self._dim - 1:
                    rep += "\n"
                else:
                    rep += " | "
            if row != self._dim - 1:
                rep += "-" * (4 * self._dim - 3)
                rep += "\n"
        return rep

    def get_dim(self):
        """
        Return the dimension of the board
        """
        return self._dim

    def get_square(self, row, col):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO
        that correspond to the contents of the board at position (row, col).
        """
        return self._board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        empty = []
        for row in range(self._dim):
            for col in range(self._dim):
                if self._board[row][col] == EMPTY:
                    empty.append((row, col))

        return empty

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        if self._board[row][col] == EMPTY:
            self._board[row][col] = player

    def check_win(self):
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """
        board = self._board
        dim = self._dim
        lines = []

        # rows
        lines.extend(board)

        # columns
        cols = [[board[row][col] for row in range(dim)]
                for col in range(dim)]
        lines.extend(cols)

        # diagonals
        diag1 = [board[idx][idx] for idx in range(dim)]
        diag2 = [board[idx][dim - idx - 1]
                 for idx in range(dim)]
        lines.append(diag1)
        lines.append(diag2)

        # check all lines
        for line in lines:
            if len(set(line)) == 1 and line[0] != EMPTY:
                if self._reverse:
                    return switch_player(line[0])
                else:
                    return line[0]

        # no winner, check for draw
        if len(self.get_empty_squares()) == 0:
            return DRAW

        # game is still in progress
        return None

    def clone(self):
        """
        Return a copy of the board
        """
        return TTTBoard(self._dim, self._reverse, self._board)


def switch_player(player):
    """
    Convenience function to switch players.

    Returns other player.
    """
    if player == PLAYERX:
        return PLAYERO
    else:
        return PLAYERX
