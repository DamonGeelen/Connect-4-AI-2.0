from header import *
from my_ai import *
from menu_displays import *
from connect_four import *

# Initialize game
myfont = pygame.font.Font(FONT_NAME, 75)
turn = 0
old_col = 0
board = create_board()

main_menu()
difficulty = difficulty_selection()
draw_board(board)

# Main game loop
while not game_over:

    # Initalize the red piece over board at mouse position
    pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, SQUARE_SIZE))
    posx = pygame.mouse.get_pos()[0]
    pygame.draw.circle(screen, RED, (posx, SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
    col = posx // SQUARE_SIZE
    row = get_next_open_row(board, col)

    # Initialize the the 'shadow piece' that shows where the next piece will be placed upon the user's mouse click
    if row != -1:
        pygame.draw.circle(screen, RED_2, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (ROW_COUNT - row) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

    pygame.display.update()
    
    for event in pygame.event.get():

        # Enable the ability to click the 'X' button on the window to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Continually update hovering red piece as well as 'shadow piece'
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, SQUARE_SIZE))
            posx = event.pos[0]
            pygame.draw.circle(screen, RED, (posx, SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
            col = posx // SQUARE_SIZE
            row = get_next_open_row(board, col)

            if col != old_col:
                draw_board(board)
                old_col = col
            
            if row != None:
                pygame.draw.circle(screen, RED_2, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (ROW_COUNT - row) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)


        pygame.display.update()

        # Place piece on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, WINDOW_WIDTH, SQUARE_SIZE))

            # Player 1 (Red)
            posx = event.pos[0]
            col = posx // SQUARE_SIZE

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                draw_board(board)
                pygame.display.update()

                # Check for player 1 win
                if winning_move(board, 1):
                    label = myfont.render("Player 1 Wins!", 1, RED)
                    screen.blit(label, ((WINDOW_WIDTH - label.get_width())/2, 10))
                    game_over = True

                pygame.time.wait(750)

                # Player 2 (Yellow)
                # The AI finds the best move.
                if not game_over:
                    result = minimax(board, True, difficulty, -float("Inf"), float("Inf"), my_evaluate_board)
                    col = result[1]
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    draw_board(board)
                    pygame.display.update()

                    # Check for player 2 win
                    if winning_move(board, 2):
                        label = myfont.render("Player 2 Wins!", 1, YELLOW)
                        screen.blit(label, ((WINDOW_WIDTH - label.get_width())/2, 10))
                        game_over = True
            
            # Check for a draw (full board with no winner)
            if board_full(board):
                label = myfont.render("Draw!", 1, BLUE)
                screen.blit(label, ((WINDOW_WIDTH - label.get_width())/2, 10))
                game_over = True

            draw_board(board)

            # Check for game over
            if game_over:
                pygame.time.wait(3000)

                # Post game menu
                board, game_over, turn = post_game_menu()

                # Restart game (if user doesn't quit in post game menu)
                main_menu()
                difficulty = difficulty_selection()
                draw_board(board)