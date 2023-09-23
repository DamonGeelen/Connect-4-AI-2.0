# Global Libraries
import pygame
import logging
import sys

# Constants
FONT_NAME = "VT323-Regular.ttf"
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
WINDOW_WIDTH = COLUMN_COUNT * SQUARE_SIZE
WINDOW_HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE  # Extra row for displaying the current player

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 71, 171)
RED = (215, 0, 64)
RED_2 = (108, 0, 32)
YELLOW = (253, 218, 13)

# Initialize PyGame
pygame.init()

# Initialize PyGame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Connect 4")