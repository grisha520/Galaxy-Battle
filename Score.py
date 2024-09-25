import pygame

class Score:
    def __init__(self, font, size, color):
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.score = 0

    def add_points(self, points):
        self.score += points

    def reset(self):
        self.score = 0

    def render(self, screen, x, y):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, (x - score_text.get_width(), y))