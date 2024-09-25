import pygame
from Constants import MONSTER_IMAGE, BULLET_WIDTH, BULLET_HEIGHT, MONSTER_WIDTH, MONSTER_HEIGHT, MONSTER_HEALTH


class Monster:
    def __init__(self, x, y):
        original_monster_img = pygame.image.load(MONSTER_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(original_monster_img, (MONSTER_WIDTH, MONSTER_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = MONSTER_HEALTH

    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def is_hit(self, bullets):
        for bullet in bullets:
            if self.rect.colliderect(pygame.Rect(bullet[0], bullet[1], BULLET_WIDTH, BULLET_HEIGHT)):
                bullets.remove(bullet)
                self.health -= 1
                return self.health <= 0
        return False