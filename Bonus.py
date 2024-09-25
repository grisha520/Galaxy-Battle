import pygame
from Constants import BONUS_WIDTH, BONUS_HEIGHT

class Bonus:
    def __init__(self, x, y):
        original_bonus_image = pygame.image.load("assets/boost.png").convert_alpha()
        self.image = pygame.transform.scale(original_bonus_image, (BONUS_WIDTH, BONUS_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5  # Скорость падения бонуса

    def move(self):
        self.rect.y += self.speed

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def is_collected(self, ship_rect):
        return self.rect.colliderect(ship_rect)