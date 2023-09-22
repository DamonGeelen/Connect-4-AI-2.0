from header import *
from connect_four import *
from copy import deepcopy
import random

# Define the recursive minimax algorithm that the AI uses to determine the optimal move.

def minimax(input_board, is_maximizing, depth, alpha, beta, eval_function):
    """
    Implements the minimax algorithm for the game Connect Four.

    Args:
        input_board (list of lists): The current state of the Connect Four board.
        is_maximizing (bool): Indicates whether the AI player is the maximizing player.
        depth (int): The maximum depth to search in the game tree.
        alpha (float): The alpha value for alpha-beta pruning.
        beta (float): The beta value for alpha-beta pruning.
        eval_function (function): The evaluation function used to assign values to board states.

    Returns:
        list: A list containing the best value and best move for the AI player.

    """
    if game_is_over(input_board) or depth == 0:
        return [eval_function(input_board), ""]
    if is_maximizing:
        best_value = -float("Inf")
        moves = available_moves(input_board)
        random.shuffle(moves)
        best_move = moves[0]
        for move in moves:
            new_board = deepcopy(input_board)
            row = get_next_open_row(new_board, move)
            drop_piece(new_board, row, move, 2)
            hypothetical_value = minimax(new_board, False, depth - 1, alpha, beta, eval_function)[0]
            if hypothetical_value > best_value:
                best_value = hypothetical_value
                best_move = move
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        return [best_value, best_move]
    else:
        best_value = float("Inf")
        moves = available_moves(input_board)
        random.shuffle(moves)
        best_move = moves[0]
        for move in moves:
            new_board = deepcopy(input_board)
            row = get_next_open_row(new_board, move)
            drop_piece(new_board, row, move, 1)
            hypothetical_value = minimax(new_board, True, depth - 1, alpha, beta, eval_function)[0]
            if hypothetical_value < best_value:
                best_value = hypothetical_value
                best_move = move
            beta = min(beta, best_value)
            if alpha >= beta:
                break
        return [best_value, best_move]

# The following are a list of functions to count the streaks a given player has in any one direction.

# Note that there is no function to count the streak downwards since a piece cannot be placed
# directly below another piece.

# ------------------------------------------------------------------------------------------------------------------------
def right_streak_check(board, player):
    """
    Check for streaks of a given player moving to the right on a Connect Four board.

    Args:
    - board (list of lists): The game board represented as a 2D list.
    - player (int): The player number (1 or 2) for whom the streaks are being checked.

    Returns:
    - right_streak (int): The total number of streaks moving to the right for the given player on the game board.
    """

    # Keep track of streak
    right_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving to the right
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 1):

            # Skip checked spaces
            if [row, col] in checked:
                continue

            else:
                if board[row][col] == player:
                    i = 1
                    while col + i < COLUMN_COUNT and board[row][col + i] == player:
                        checked.append([row, col + i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col + i < COLUMN_COUNT and board[row][col + i] == 0:
                        right_streak += i - 1

    return right_streak
    return right_streak


def left_streak_check(board, player):
    """
    Check for streaks of a given player moving to the left on the game board.

    Args:
        board (list of lists): The game board represented as a 2D list.
        player (int): The player number (1 or 2) to check for streaks.

    Returns:
        int: The number of streaks of the given player moving to the left on the game board.
    """

    # Keep track of streak
    left_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving to the left
    for col in range(COLUMN_COUNT - 1, 2, -1):
        for row in range(ROW_COUNT - 1):

            # Skip checked spaces
            if [row, col] in checked:
                continue

            else:
                if board[row][col] == player:
                    i = 1
                    while col - i >= 0 and board[row][col - i] == player:
                        checked.append([row, col - i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col - i >= 0 and board[row][col - i] == 0:
                        left_streak += i - 1

    return left_streak


def up_streak_check(board, player):
    """
    Check for streaks of a given player moving upward on the game board.

    Args:
    - board (list of lists): The game board represented as a 2D list.
    - player (integer): The player number (1 or 2) for whom the streaks are checked.

    Returns:
    - up_streak (integer): The total number of upward streaks for the given player on the game board.
    """

    # Keep track of streak
    up_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving upward
    for col in range(COLUMN_COUNT - 1):
        for row in range(ROW_COUNT - 3):

            # Skip checked spaces
            if [row, col] in checked:
                continue

            else:
                if board[row][col] == player:
                    i = 1
                    while row + i < ROW_COUNT and board[row + i][col] == player:
                        checked.append([row + i, col])
                        i += 1

                    # Only count streak if it is not blocked
                    if row + i < ROW_COUNT and board[row + i][col] == 0:
                        up_streak += i - 1

    return up_streak


def up_right_streak_check(board, player):
    """
    Check for streaks of a given player moving upward and to the right on the game board.

    Args:
        board (list): The game board represented as a 2D list.
        player (int): The player number (1 or 2) to check for streaks.

    Returns:
        int: The number of streaks of the given player moving upward and to the right on the game board.
    """

    # Keep track of streak
    up_right_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving upward and to the right
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):

            # Skip checked spaces
            if [row, col] in checked:
                continue

            else:
                if board[row][col] == player:
                    i = 1
                    while col + i < COLUMN_COUNT and row + i < ROW_COUNT and board[row + i][col + i] == player:
                        checked.append([row + i, col + i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col + i < COLUMN_COUNT and row + i < ROW_COUNT and board[row + i][col + i] == 0:
                        up_right_streak += i - 1

    return up_right_streak


def down_right_streak_check(board, player):
    """
    Check for streaks of a given player moving downward and to the right on the game board.

    Args:
        board (list): The game board represented as a 2D list.
        player (int): The player number (1 or 2) to check for streaks.

    Returns:
        int: The number of streaks of the given player moving downward and to the right on the game board.
    """
    # Keep track of streak
    down_right_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving downward and to the right
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 1, 2, -1):

            # Skip checked spaces
            if [row, col] in checked:
                continue

            else:
                if board[row][col] == player:
                    i = 1
                    while col + i < COLUMN_COUNT and row - i >= 0 and board[row - i][col + i] == player:
                        checked.append([row - i, col + i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col + i < COLUMN_COUNT and row - i >= 0 and board[row - i][col + i] == 0:
                        down_right_streak += i - 1

    return down_right_streak


def up_left_streak_check(board, player):
    """
    Check for streaks of a given player moving upward and to the left on the game board.

    Args:
        board (list): The game board represented as a 2D list.
        player (int): The player number (1 or 2) to check for streaks.

    Returns:
        int: The number of streaks of the given player moving upward and to the left on the game board.
    """
    # Keep track of streak
    up_left_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving upward and to the left
    for col in range(COLUMN_COUNT - 1, 2, -1):
        for row in range(ROW_COUNT - 3):

            # Skip checked spaces
            if [row, col] in checked:
                continue

            else:
                if board[row][col] == player:
                    i = 1
                    while col - i >= 0 and row + i < ROW_COUNT and board[row + i][col - i] == player:
                        checked.append([row + i, col - i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col - i >= 0 and row + i < ROW_COUNT and board[row + i][col - i] == 0:
                        up_left_streak += i - 1

    return up_left_streak


def down_left_streak_check(board, player):
    """
    Check for streaks of a given player moving downward and to the left on the game board.

    Args:
        board (list): The game board represented as a 2D list.
        player (int): The player number (1 or 2) to check for streaks.

    Returns:
        int: The number of streaks of the given player moving downward and to the left on the game board.
    """
    # Keep track of streak
    down_left_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving downward and to the left
    for col in range(COLUMN_COUNT - 1, 2, -1):
        for row in range(ROW_COUNT - 1, 2, -1):

            # Skip checked spaces
            if [row, col] in checked:
                continue

            else:
                if board[row][col] == player:
                    i = 1
                    while col - i >= 0 and row - i < ROW_COUNT and board[row - i][col - i] == player:
                        checked.append([row - i, col - i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col - i >= 0 and row - i < ROW_COUNT and board[row - i][col - i] == 0:
                        down_left_streak += i - 1

    return down_left_streak
# ---------------------------------------------------------------------------------------------------


def total_streak_check(board, player):
    """
    Calculate the total streak of a player on the board.

    Args:
    - board: a list representing the game board
    - player: an integer representing the player number (1 or 2)

    Returns:
    - total_streak: an integer representing the total streak of the player
    """

    # Handle the case where the board is empty
    if not board.any():
        return 0

    # Handle the case where the player number is not 1 or 2
    if player not in {1, 2}:
        raise ValueError("Invalid player number. Player number must be 1 or 2.")

    # Keep track of streak
    total_streak = 0

    # Accumulate the total directly in a variable
    total_streak += right_streak_check(board, player)
    total_streak += left_streak_check(board, player)
    total_streak += up_streak_check(board, player)
    total_streak += up_right_streak_check(board, player)
    total_streak += down_right_streak_check(board, player)
    total_streak += up_left_streak_check(board, player)
    total_streak += down_right_streak_check(board, player)

    return total_streak


# Find the current advantage for each player based on their total streaks,
# then return the difference so the AI can evaluate any given board scenario
def my_evaluate_board(board):
    """
    Evaluates the current state of the game board.

    Args:
        board (list of lists): The game board represented as a 2D list.

    Returns:
        evaluation (integer): Player 2's "score" on the current game board.
    """
    # Player 1 wins
    if winning_move(board, 1):
        return -float("Inf")

    # Player 2 wins
    elif winning_move(board, 2):
        return float("Inf")

    # No win yet
    # Keep track of streaks for both players
    p1_streak = total_streak_check(board, 1)
    p2_streak = total_streak_check(board, 2)

    return p2_streak - p1_streak