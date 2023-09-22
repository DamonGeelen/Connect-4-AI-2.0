from header import *
import numpy as np

# Gameplay functions
def create_board():
    """
    Creates a new game board with dimensions ROW_COUNT x COLUMN_COUNT.
    Each cell in the board is initialized with a value of 0.
    
    Returns:
        numpy.ndarray: The game board represented as a numpy array.
            Each cell in the board is initialized with a value of 0.
    """
    if not isinstance(ROW_COUNT, int) or not isinstance(COLUMN_COUNT, int) or ROW_COUNT <= 0 or COLUMN_COUNT <= 0:
        raise ValueError("ROW_COUNT and COLUMN_COUNT must be positive integers.")
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    """
    Drop a piece on the board at the specified location.

    Args:
        board (list): The game board.
        row (int): The row index.
        col (int): The column index.
        piece (int): The piece to be placed.

    Raises:
        ValueError: If the row or column is invalid.

    Returns:
        None
    """
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        raise ValueError("Invalid row or column")
    
    if board[row][col] == 0:
        board[row][col] = piece


def is_valid_location(board, col):
    """
    Check if the given column is a valid location on the board.
    
    Args:
        board (list): The game board.
        col (int): The column to check.
        
    Returns:
        bool: True if the column is valid, False otherwise.
    """
    return 0 <= col < len(board[0]) and board[ROW_COUNT - 1][col] == 0


def available_moves(board):
    """
    Get a list of available moves on the game board.
    
    Args:
        board (list): The game board.
        
    Returns:
        list: A list of available moves.
    """
    moves = [i for i in range(COLUMN_COUNT) if is_valid_location(board, i)]
    return moves


def get_next_open_row(board, col):
    """
    Find the next open row in the given column of the board.

    Parameters:
    - board: a 2D list representing the game board
    - col: an integer representing the column index

    Returns:
    - The row index of the next open row in the column, or -1 if no open row is found.
    """
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row
    return -1


def check_win(board, piece, row_delta, col_delta):
    """
    Helper function to check for a win in a given direction.
    """
    
    if row_delta not in {-1, 0, 1} or col_delta not in {-1, 0, 1}:
        return False
    
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            for i in range(4):
                # ------------ Protect against checking out of bounds -------------
                if row + i * row_delta < 0 or row + i * row_delta >= ROW_COUNT:
                    break

                elif col + i * col_delta < 0 or col+ i * col_delta >= COLUMN_COUNT:
                    break
                # -----------------------------------------------------------------

                elif board[row + i * row_delta][col + i * col_delta] != piece:
                    break

            else:
                return True

    return False


def winning_move(board, piece):
    """
    Check if the current move is a winning move.
    """
    if piece not in [1, 2]:
        raise ValueError("Invalid game piece")
    
    # Check horizontal
    if check_win(board, piece, 0, 1):
        return True

    # Check vertical
    if check_win(board, piece, 1, 0):
        return True

    # Check upward diagonals
    if check_win(board, piece, 1, 1):
        return True

    # Check downward diagonals
    if check_win(board, piece, -1, 1):
        return True
    
    return False


def board_full(board):
    """
    Check if the game board is full.
    
    Args:
        board (list): The game board represented as a 2D list.
    
    Returns:
        bool: True if the board is full, False otherwise.
    """
    return not np.any(board == 0)

def game_is_over(board):
  return winning_move(board, 1) or winning_move(board, 2) or board_full(board)

def draw_board(board):
    """
    Draws a Connect Four game board on the screen using the PyGame library.

    Args:
        board (list): A 2D list representing the Connect Four game board. Each element in the list can be either 0, 1, or 2, representing an empty space, a player 1 piece, or a player 2 piece, respectively.

    Returns:
        None. The function only draws the Connect Four game board on the screen.
    """
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (ROW_COUNT - row) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (ROW_COUNT - row) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

    pygame.display.update()