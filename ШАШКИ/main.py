# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, SIZE_DELTA, WIDTH_FOR_PIECES, WHITE, BG, BLUE, text_rules
from checkers.game import Game
from minimax.algorithm import minimax
from checkers.button import Button
import sys

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
pygame.font.init()


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y-SIZE_DELTA) // SQUARE_SIZE
    col = (x-SIZE_DELTA) // SQUARE_SIZE
    return row, col


def main_menu():
    while True:
        WIN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("MAIN MENU", True, "#ffc20a")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH / 2, HEIGHT * 0.15))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.35),
                             text_input="PLAY", font=get_font(75), base_color="#ffc20a", hovering_color="#131112")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.75),
                             text_input="QUIT", font=get_font(75), base_color="#ffc20a", hovering_color="#131112")

        RULES_BUTTON = Button(image=pygame.image.load("assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.55),
                             text_input="RULES", font=get_font(75), base_color="#ffc20a", hovering_color="#131112")

        WIN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON, RULES_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    color_selection()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rules()

        pygame.display.update()


def rules():
    while True:
        WIN.fill((255, 255, 255))

        RULES_MOUSE_POS = pygame.mouse.get_pos()
        r, c = 60, 50
        for i in range(len(text_rules)):
            RULES_TEXT = get_font(15).render(text_rules[i], True, "#42AAFF")
            RULES_RECT = RULES_TEXT.get_rect(topleft=(60, c + i*35))
            WIN.blit(RULES_TEXT, RULES_RECT)

        RULES_BACK = Button(image=None, pos=(WIDTH / 2, HEIGHT * 0.9),
                               text_input="BACK", font=get_font(20), base_color="#ffc20a", hovering_color="#131112")


        RULES_BACK.changeColor(RULES_MOUSE_POS)
        RULES_BACK.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def color_selection():
    while True:
        WIN.blit(BG, (0, 0))
        SELECTION_MOUSE_POS = pygame.mouse.get_pos()
        SELECTION_TEXT = get_font(60).render("SELECT COLOR", True, "#ffc20a")
        SELECTION_RECT = SELECTION_TEXT.get_rect(center=(WIDTH / 2, HEIGHT * 0.25))
        WIN.blit(SELECTION_TEXT, SELECTION_RECT)

        SELECTION_BACK = Button(image=None, pos=(WIDTH / 2, HEIGHT * 0.75),
                              text_input="BACK", font=get_font(45), base_color="#ffc20a", hovering_color="#131112")

        SELECTION_WHITE_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT * 0.417),
                                text_input="БОТ ХОДИТ ПЕРВЫМ", font=get_font(30), base_color="#ffc20a", hovering_color="#131112")

        SELECTION_BLACK_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT * 0.583),
                                 text_input="БОТ ХОДИТ ВТОРЫМ", font=get_font(30), base_color="#ffc20a", hovering_color="#131112")

        for button in [SELECTION_BLACK_BUTTON, SELECTION_WHITE_BUTTON, SELECTION_BACK]:
            button.changeColor(SELECTION_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SELECTION_BACK.checkForInput(SELECTION_MOUSE_POS):
                    main_menu()
                if SELECTION_BLACK_BUTTON.checkForInput(SELECTION_MOUSE_POS):
                    main(BLUE)
                if SELECTION_WHITE_BUTTON.checkForInput(SELECTION_MOUSE_POS):
                    main(WHITE)
        pygame.display.update()


def main(player_color):
    selected_color = player_color

    run = True
    clock = pygame.time.Clock()

    game = Game(WIN)

    if selected_color == BLUE:
        game.turn = BLUE
    else:
        game.turn = WHITE



    while run:
        clock.tick(FPS)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(7, 7),
                                text_input="BACK", font=get_font(20), base_color="#ffc20a", hovering_color="#131112")


        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 6, WHITE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            winner_menu(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        PLAY_BACK.update(WIN)

        game.update()

    pygame.quit()


def winner_menu(winner_color):
    while True:
        WIN.blit(BG, (0, 0))
        WINNER_MOUSE_POS = pygame.mouse.get_pos()
        if winner_color == WHITE:
            winner_color_text = "WHITE"
        else:
            winner_color_text = "BLACK"
        WINNER_TEXT = get_font(60).render(f"{winner_color_text} WINS!", True, "#ffc20a")
        WINNER_RECT = WINNER_TEXT.get_rect(center=(WIDTH / 2, HEIGHT * 0.15))

        PLAY_BUTTON = Button(image=pygame.image.load("../ШАШКИ/assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.4),
                             text_input="PLAY", font=get_font(75), base_color="#ffc20a", hovering_color="#131112")
        QUIT_BUTTON = Button(image=pygame.image.load("../ШАШКИ/assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.6375),
                             text_input="QUIT", font=get_font(75), base_color="#ffc20a", hovering_color="#131112")

        WIN.blit(WINNER_TEXT, WINNER_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(WINNER_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(WINNER_MOUSE_POS):
                    color_selection()
                if QUIT_BUTTON.checkForInput(WINNER_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()