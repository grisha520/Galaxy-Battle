from Constants import *

class Level1Boss:
    def __init__(self):
        self.image = pygame.image.load(BOSS_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (BOSS_WIDTH, BOSS_HEIGHT))
        self.rect = self.image.get_rect(midtop=(WIDTH // 2, -BOSS_HEIGHT))
        self.health = BOSS_HEALTH
        self.speed = BOSS_SPEED

    def move(self):
        if self.rect.top < 0:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def is_hit(self, bullets):
        for bullet in bullets:
            if self.rect.colliderect(pygame.Rect(bullet[0], bullet[1], BULLET_WIDTH, BULLET_HEIGHT)):
                bullets.remove(bullet)
                self.health -= 1
                return self.health <= 0
        return False


class Level2Boss(Level1Boss):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(BOSS_IMAGE_2).convert_alpha(),
                                            (self.rect.width, self.rect.height))
        self.bullet_img = pygame.transform.scale(pygame.image.load(BOSS_BULLET_IMAGE).convert_alpha(),
                                                 (BULLET_WIDTH, BULLET_HEIGHT))
        self.bullets = []
        self.shoot_cooldown = 2000  # Время между выстрелами в мс
        self.last_shot_time = pygame.time.get_ticks()

    def move(self):
        super().move()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time

    def shoot(self):
        bullet_x = self.rect.centerx - self.bullet_img.get_width() // 2
        bullet_y = self.rect.bottom
        self.bullets.append([bullet_x, bullet_y])

    def update_bullets(self):
        for bullet in self.bullets:
            bullet[1] += BULLET_SPEED
            if bullet[1] > HEIGHT:
                self.bullets.remove(bullet)

    def draw(self, window):
        super().draw(window)
        for bullet in self.bullets:
            window.blit(self.bullet_img, (bullet[0], bullet[1]))



class Level3Boss(Level1Boss):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(BOSS_IMAGE_3).convert_alpha(),
                                            (BOSS_WIDTH_3, BOSS_HEIGHT_3))
        self.bullet_img = pygame.transform.scale(pygame.image.load(BOSS_BULLET_IMAGE).convert_alpha(),
                                                 (BULLET_WIDTH, BULLET_HEIGHT))
        self.bullets = []
        self.shoot_cooldown = 800  # Время между выстрелами в мс
        self.last_shot_time = pygame.time.get_ticks()

    def move(self):
        super().move()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time

    def shoot(self):
        bullet_x = self.rect.centerx - self.bullet_img.get_width() // 2
        bullet_y = self.rect.bottom
        self.bullets.append([bullet_x, bullet_y])

    def update_bullets(self):
        for bullet in self.bullets:
            bullet[1] += BULLET_SPEED
            if bullet[1] > HEIGHT:
                self.bullets.remove(bullet)

    def draw(self, window):
        super().draw(window)
        for bullet in self.bullets:
            window.blit(self.bullet_img, (bullet[0], bullet[1]))