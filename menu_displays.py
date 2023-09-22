from header import *
from connect_four import create_board

# Main menu
def main_menu():
    # Define font and text
    title_font = pygame.font.Font(FONT_NAME, 164)
    title_text = title_font.render("CONNECT 4", True, WHITE)

    menu_font = pygame.font.Font(FONT_NAME, 24)
    menu_text = menu_font.render("Press [ENTER] to Start", True, WHITE)

    # Define text locations
    title_rect = title_text.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
    menu_rect = menu_text.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT * 5 // 6))

#   |--------------------------------- Animation frames ---------------------------------|
    def full_menu():
        screen.fill(BLACK)
        screen.blit(title_text, title_rect)
        screen.blit(menu_text, menu_rect)
        pygame.display.update()

    def title_only():
        screen.fill(BLACK)
        screen.blit(title_text, title_rect)
        pygame.display.update()
#   |------------------------------------------------------------------------------------|

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Start the game when Enter is pressed

        # Display title with flashing menu text
        full_menu()
        pygame.time.wait(1000)
        title_only()
        pygame.time.wait(500)

# Difficulty selection
def difficulty_selection():
    # Define font and text
    difficulty_font = pygame.font.Font(FONT_NAME, 48)
    difficulty_text = difficulty_font.render("Select Difficulty:", True, WHITE)

    option_font = pygame.font.Font(FONT_NAME, 36)
    easy_text = option_font.render("[1]: EASY", True, WHITE)
    medium_text = option_font.render("[2]: MEDIUM", True, WHITE)
    hard_text = option_font.render("[3]: HARD", True, WHITE)
    expert_text = option_font.render("[4]: EXPERT", True, WHITE)

    # Define text locations
    difficulty_rect = difficulty_text.get_rect(left = WINDOW_WIDTH // 10, centery = WINDOW_HEIGHT * 5 // 16)
    easy_rect = easy_text.get_rect(left = WINDOW_WIDTH // 10, centery = WINDOW_HEIGHT * 7 // 16)
    medium_rect = medium_text.get_rect(left = WINDOW_WIDTH // 10, centery = WINDOW_HEIGHT * 8 // 16)
    hard_rect = hard_text.get_rect(left = WINDOW_WIDTH // 10, centery = WINDOW_HEIGHT * 9 // 16)
    expert_rect = expert_text.get_rect(left = WINDOW_WIDTH // 10, centery = WINDOW_HEIGHT * 10 // 16)

#   |-------------------------------------------- Animation frames -------------------------------------------|
    def all_text():
        screen.fill(BLACK)
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)
        screen.blit(expert_text, expert_rect)
        pygame.display.update()

    def easy_missing():
        screen.fill(BLACK)
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)
        screen.blit(expert_text, expert_rect)
        pygame.display.update()

    def medium_missing():
        screen.fill(BLACK)
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(hard_text, hard_rect)
        screen.blit(expert_text, expert_rect)
        pygame.display.update()

    def hard_missing():
        screen.fill(BLACK)
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(expert_text, expert_rect)
        pygame.display.update()

    def expert_missing():
        screen.fill(BLACK)
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)
        pygame.display.update()
#   |---------------------------------------------------------------------------------------------------------|

    # Animation upon difficulty selection
    def animation():
        easy_missing()
        pygame.time.wait(50)
        medium_missing()
        pygame.time.wait(50)
        hard_missing()
        pygame.time.wait(50)
        expert_missing()
        pygame.time.wait(100)

    # Display menu
    all_text()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:

                    logging.debug("Selected difficulty: Easy")

                    animation()
                    animation()
                    easy_missing()
                    pygame.time.wait(100)
                    all_text()
                    pygame.time.wait(100)
                    easy_missing()
                    pygame.time.wait(100)

                    return 1 # Easy
                
                elif event.key == pygame.K_2:

                    logging.debug("Selected difficulty: Medium")

                    animation()
                    animation()
                    medium_missing()
                    pygame.time.wait(100)
                    all_text()
                    pygame.time.wait(100)
                    medium_missing()
                    pygame.time.wait(100)

                    return 2 # Medium
                
                elif event.key == pygame.K_3:

                    logging.debug("Selected difficulty: Hard")

                    animation()
                    animation()
                    hard_missing()
                    pygame.time.wait(100)
                    all_text()
                    pygame.time.wait(100)
                    hard_missing()
                    pygame.time.wait(100)

                    return 3 # Hard
                
                elif event.key == pygame.K_4:

                    logging.debug("Selected difficulty: Expert")

                    animation()
                    animation()
                    expert_missing()
                    pygame.time.wait(100)
                    all_text()
                    pygame.time.wait(100)
                    expert_missing()
                    pygame.time.wait(100)

                    return 4 # Expert




# Post game menu
def post_game_menu():
    # Define font and text
    game_over_font = pygame.font.Font(FONT_NAME, 164)
    game_over_text = game_over_font.render("GAME OVER", True, WHITE)

    option_font = pygame.font.Font(FONT_NAME, 36)
    replay_text = option_font.render("[ENTER]: Play Again", True, WHITE)
    exit_text = option_font.render("[ESC]: Exit", True, WHITE)
    
    # Define text locations
    game_over_rect = game_over_text.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT * 3 // 8))
    replay_rect = replay_text.get_rect(left = WINDOW_WIDTH // 10, centery = WINDOW_HEIGHT * 5 // 8)
    exit_rect = exit_text.get_rect(left = WINDOW_WIDTH // 10, centery = WINDOW_HEIGHT * 11 // 16)

#   |--------------------------------------- Animation frames ---------------------------------------|
    def all_text():
        screen.fill(BLACK)
        screen.blit(game_over_text, game_over_rect)
        screen.blit(replay_text, replay_rect)
        screen.blit(exit_text, exit_rect)
        pygame.display.update()
    
    def no_game_over():
        screen.fill(BLACK)
        screen.blit(replay_text, replay_rect)
        screen.blit(exit_text, exit_rect)
        pygame.display.update()

#   |------------------------------------------------------------------------------------------------|
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return create_board(), False, 0 # User wants to play again
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()  # User wants to exit
        
        # Display end game options with flashing "GAME OVER"
        all_text()
        pygame.time.wait(1000)
        no_game_over()
        pygame.time.wait(1500)