"""
Mini-max Tic-Tac-Toe Player
"""

# general imports
import ttt_board

# SCORING VALUES
SCORES = {ttt_board.PLAYERX: 1,
          ttt_board.DRAW: 0,
          ttt_board.PLAYERO: -1}


def get_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    return alpha_beta_pruning_move(board, player, -2, 2)


def alpha_beta_pruning_move(board, player, alpha, beta):
    """
    A helper function for mm_move that uses alpha beta pruning to find
    the best move

    Returns the score and best move for the current state of the board
    """
    # initialize local variables
    other_player = ttt_board.switch_player(player)
    best_move = (-1, -1)
    best_score = -2

    # base case
    if board.check_win() is not None:
        return SCORES[board.check_win()], best_move

    for move in board.get_empty_squares():
        trial = board.clone()
        trial.move(move[0], move[1], player)
        score = alpha_beta_pruning_move(trial, other_player, -beta, -max(alpha, best_score))[0]
        alpha = score * SCORES[player]

        if alpha == 1:
            return score, move
        elif alpha > best_score:
            best_score = alpha
            best_move = move

        if best_score >= beta:
            break

    return best_score * SCORES[player], best_move


def move_wrapper(board, player):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = get_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]
