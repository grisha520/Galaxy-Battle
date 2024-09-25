import pygame

class Music:
    def __init__(self, gameplay_music):
        pygame.mixer.init()
        self.gameplay_music = gameplay_music

    def play_gameplay_music(self):
        pygame.mixer.music.load(self.gameplay_music)
        pygame.mixer.music.play(-1)