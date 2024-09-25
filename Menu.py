import pygame
import sys
from Button import Button
from Constants import WIDTH, HEIGHT, BG
from Game import Game
from Music import Music

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Battle")


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

music_play = Music(gameplay_music='assets/gameplay_music.mp3')

def main_menu():
    while True:
        WINDOW.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("MAIN MENU", True, "#ffc20a")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH / 2, HEIGHT * 0.15))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.4),
                             text_input="PLAY", font=get_font(75), base_color="#ffc20a", hovering_color="#131112")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.6375),
                             text_input="QUIT", font=get_font(75), base_color="#ffc20a", hovering_color="#131112")

        WINDOW.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    level_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def level_menu():
    music_play.play_gameplay_music()
    while True:
        WINDOW.blit(BG, (0, 0))

        LEVEL_MOUSE_POS = pygame.mouse.get_pos()

        LEVEL_TEXT = get_font(60).render("SELECT LEVEL", True, "#ffc20a")
        LEVEL_RECT = LEVEL_TEXT.get_rect(center=(WIDTH / 2, HEIGHT * 0.15))

        BUTTON_HEIGHT = HEIGHT * 0.2
        LEVEL_1_BUTTON = Button(image=pygame.image.load("assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.35),
                                text_input="1 LEVEL", font=get_font(50), base_color="#ffc20a", hovering_color="#131112")
        LEVEL_2_BUTTON = Button(image=pygame.image.load("assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.35 + BUTTON_HEIGHT),
                                text_input="2 LEVEL", font=get_font(50), base_color="#ffc20a", hovering_color="#131112")
        LEVEL_3_BUTTON = Button(image=pygame.image.load("assets/Rect1.png"), pos=(WIDTH / 2, HEIGHT * 0.35 + 2 * BUTTON_HEIGHT),
                                text_input="3 LEVEL", font=get_font(50), base_color="#ffc20a", hovering_color="#131112")

        BACK_BUTTON = Button(image=None, pos=(WIDTH / 2, HEIGHT * 0.9), text_input="BACK", font=get_font(35), base_color="#ffc20a", hovering_color="#131112")

        WINDOW.blit(LEVEL_TEXT, LEVEL_RECT)

        for button in [LEVEL_1_BUTTON, LEVEL_2_BUTTON, LEVEL_3_BUTTON, BACK_BUTTON]:
            button.changeColor(LEVEL_MOUSE_POS)
            button.update(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_1_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    game = Game()
                    game.play_level_1()
                if LEVEL_2_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    game = Game()
                    game.play_level_2()
                if LEVEL_3_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    game = Game()
                    game.play_level_3()
                if BACK_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    main_menu()

        pygame.display.update()

if __name__ == '__main__':
    main_menu()
