import math
import random
from Button import Button
from Monster import Monster
from Score import Score
from Monster_Boss import Level1Boss, Level2Boss, Level3Boss
from Bonus import Bonus
from Constants import *

class Game:
    def __init__(self):
        original_spaceship_img = pygame.image.load(SPACESHIP_IMAGE).convert_alpha()
        self.spaceship_img = pygame.transform.scale(original_spaceship_img, (SHIP_WIDTH, SHIP_HEIGHT))
        original_bullet_img = pygame.image.load(BULLET_IMAGE).convert_alpha()
        self.bullet_img = pygame.transform.scale(original_bullet_img, (BULLET_WIDTH, BULLET_HEIGHT))
        self.score = Score(None, 35, "#ffc20a")

    def play_level_1(self):
        pygame.init()
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Galaxy Battle - Level 1")
        clock = pygame.time.Clock()

        ship_x = WIDTH // 2 - self.spaceship_img.get_width() // 2
        ship_y = HEIGHT - 300

        last_shot = pygame.time.get_ticks()
        bullets = []

        monsters = []

        rows = [3, 4]
        y_start_offset = 50

        for row_idx, count in enumerate(rows):
            y_pos = y_start_offset + row_idx * (MONSTER_HEIGHT + MONSTER_ROW_SPACING)
            x_start = (WIDTH - (count * MONSTER_WIDTH + (count - 1) * MONSTER_COL_SPACING)) // 2
            for i in range(count):
                x_pos = x_start + i * (MONSTER_WIDTH + MONSTER_COL_SPACING)
                monsters.append(Monster(x_pos, y_pos))

        boss = None

        back_button_2 = Button(image=None, pos=(45, 20), text_input="BACK", font=pygame.font.Font(None, 35), base_color="#ffc20a",
               hovering_color="#131112")

        bg_y = 0
        bg_height = BG.get_height()

        game_over = False
        game_won = False

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_2.checkForInput(pygame.mouse.get_pos()):
                        return


            for button in [back_button_2]:
                button.changeColor(pygame.mouse.get_pos())


            if not (game_over or game_won):
                keys = pygame.key.get_pressed()
                current_ship_speed = SHIP_SPEED_FAST if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else SHIP_SPEED
                if keys[pygame.K_a] and ship_x > -55:  # Влево
                    ship_speed_x = -current_ship_speed
                elif keys[pygame.K_d] and ship_x < WIDTH - self.spaceship_img.get_width() + 50:  # Вправо
                    ship_speed_x = current_ship_speed
                else:
                    ship_speed_x = 0

                if keys[pygame.K_w] and ship_y > -35:  # Вверх
                    ship_speed_y = -current_ship_speed
                elif keys[pygame.K_s] and ship_y < HEIGHT - self.spaceship_img.get_height() + 35:  # Вниз
                    ship_speed_y = current_ship_speed
                else:
                    ship_speed_y = 0

                current_time = pygame.time.get_ticks()
                if keys[pygame.K_SPACE] and current_time - last_shot > FIRE_RATE:
                    bullet_x = ship_x + self.spaceship_img.get_width() // 2 - self.bullet_img.get_width() // 2
                    bullet_y = ship_y
                    bullets.append([bullet_x, bullet_y])
                    last_shot = current_time

                # Обновление позиции корабля
                ship_x += ship_speed_x
                ship_y += ship_speed_y

                bg_y += BG_SCROLL_SPEED
                if bg_y >= bg_height:
                    bg_y = 0

                WINDOW.blit(BG, (0, bg_y - bg_height))
                WINDOW.blit(BG, (0, bg_y))

                ship_rect = pygame.Rect(ship_x, ship_y, SHIP_WIDTH, SHIP_HEIGHT)
                WINDOW.blit(self.spaceship_img, (ship_x, ship_y))


                for bullet in bullets:
                    WINDOW.blit(self.bullet_img, (bullet[0], bullet[1]))
                    bullet[1] -= BULLET_SPEED
                    if bullet[1] < 0:
                        bullets.remove(bullet)

                if monsters:
                    for monster in monsters:
                        monster.draw(WINDOW)
                        if monster.is_hit(bullets):
                            monsters.remove(monster)
                            self.score.add_points(POINTS_PER_MONSTER)
                        if ship_rect.colliderect(monster.rect):
                            game_over = True
                            break

                else:
                    if boss is None:
                        boss = Level1Boss()
                    boss.move()
                    boss.draw(WINDOW)
                    if boss is not None and boss.is_hit(bullets):
                        if boss.health <= 0:
                            self.score.add_points(POINTS_PER_BOSS)
                            boss = None
                            game_won = True
                    if boss is not None and ship_rect.colliderect(boss.rect):
                        game_over = True

                self.score.render(WINDOW, WIDTH - 10, 10)

            else:
                if game_over:
                    game_over_font = pygame.font.Font(None, 74)
                    game_over_text = game_over_font.render("GAME OVER", True, "#ffc20a")
                    WINDOW.blit(game_over_text, (
                    WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

                elif game_won:
                    game_won_font = pygame.font.Font(None, 74)
                    game_won_text = game_won_font.render("YOU WIN!", True, "#ffc20a")
                    WINDOW.blit(game_won_text, (
                    WIDTH // 2 - game_won_text.get_width() // 2, HEIGHT // 2 - game_won_text.get_height() // 2))


            back_button_2.update(WINDOW)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()

    def play_level_2(self):
        pygame.init()
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Galaxy Battle - Level 2")
        clock = pygame.time.Clock()

        ship_x = WIDTH // 2 - self.spaceship_img.get_width() // 2
        ship_y = HEIGHT - 300

        last_shot = pygame.time.get_ticks()
        bullets = []

        monsters = []
        num_monsters = 8
        radius = 100
        center_x = WIDTH // 2
        center_y = 200
        angle_step = 2 * math.pi / num_monsters

        for i in range(num_monsters):
            angle = i * angle_step
            x_pos = center_x + radius * math.cos(angle) - MONSTER_WIDTH // 2
            y_pos = center_y + radius * math.sin(angle) - MONSTER_HEIGHT // 2
            monsters.append(Monster(x_pos, y_pos))

        boss = None
        bonus = None

        back_button_2 = Button(image=None, pos=(45, 20), text_input="BACK", font=pygame.font.Font(None, 35),
                               base_color="#ffc20a",
                               hovering_color="#131112")

        bg_y = 0
        bg_height = BG.get_height()

        game_over = False
        game_won = False
        bonus_active = False

        bonus_monster_index = random.randint(0, num_monsters - 1)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_2.checkForInput(pygame.mouse.get_pos()):
                        return

            for button in [back_button_2]:
                button.changeColor(pygame.mouse.get_pos())

            if not (game_over or game_won):
                keys = pygame.key.get_pressed()
                current_ship_speed = SHIP_SPEED_FAST if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else SHIP_SPEED

                if keys[pygame.K_a] and ship_x > -55:  # Влево
                    ship_speed_x = -current_ship_speed
                elif keys[pygame.K_d] and ship_x < WIDTH - self.spaceship_img.get_width() + 50:  # Вправо
                    ship_speed_x = current_ship_speed
                else:
                    ship_speed_x = 0

                if keys[pygame.K_w] and ship_y > -35:  # Вверх
                    ship_speed_y = -current_ship_speed
                elif keys[pygame.K_s] and ship_y < HEIGHT - self.spaceship_img.get_height() + 35:  # Вниз
                    ship_speed_y = current_ship_speed
                else:
                    ship_speed_y = 0

                current_time = pygame.time.get_ticks()
                if keys[pygame.K_SPACE] and current_time - last_shot > FIRE_RATE:
                    bullet_x = ship_x + self.spaceship_img.get_width() // 2 - self.bullet_img.get_width() // 2
                    bullet_y = ship_y

                    if bonus_active:
                        bullets.append([bullet_x - 40, bullet_y])  # Левая пуля
                        bullets.append([bullet_x + 40, bullet_y])  # Правая пуля
                    else:
                        bullets.append([bullet_x, bullet_y])

                    last_shot = current_time

                ship_x += ship_speed_x
                ship_y += ship_speed_y

                bg_y += BG_SCROLL_SPEED
                if bg_y >= bg_height:
                    bg_y = 0

                WINDOW.blit(BG, (0, bg_y - bg_height))
                WINDOW.blit(BG, (0, bg_y))

                ship_rect = pygame.Rect(ship_x, ship_y, SHIP_WIDTH, SHIP_HEIGHT)
                WINDOW.blit(self.spaceship_img, (ship_x, ship_y))

                for bullet in bullets:
                    WINDOW.blit(self.bullet_img, (bullet[0], bullet[1]))
                    bullet[1] -= BULLET_SPEED
                    if bullet[1] < 0:
                        bullets.remove(bullet)

                if monsters:
                    for index, monster in enumerate(monsters):
                        monster.draw(WINDOW)
                        if monster.is_hit(bullets):
                            if index == bonus_monster_index and not bonus:
                                bonus_position = (monster.rect.x, monster.rect.y)
                                bonus = Bonus(*bonus_position)
                                bonus_monster_index = None
                            monsters.remove(monster)
                            self.score.add_points(POINTS_PER_MONSTER)
                        if ship_rect.colliderect(monster.rect):
                            game_over = True
                            break


                else:
                    if boss is None:
                        boss = Level2Boss()
                    boss.move()
                    boss.update_bullets()
                    boss.draw(WINDOW)
                    if boss is not None and boss.is_hit(bullets):
                        if boss.health <= 0:
                            self.score.add_points(POINTS_PER_BOSS)
                            boss = None
                            game_won = True
                    if boss is not None and ship_rect.colliderect(boss.rect):
                        game_over = True
                    if boss is not None:
                        for boss_bullet in boss.bullets:
                            if ship_rect.colliderect(pygame.Rect(boss_bullet[0], boss_bullet[1], BULLET_WIDTH, BULLET_HEIGHT)):
                                game_over = True

                # Обновляем и отображаем бонус
                if bonus:
                    bonus.move()
                    bonus.draw(WINDOW)
                    if bonus.is_collected(ship_rect):
                        bonus_active = True
                        bonus = None

                self.score.render(WINDOW, WIDTH - 10, 10)

            else:
                if game_over:
                    game_over_font = pygame.font.Font(None, 74)
                    game_over_text = game_over_font.render("GAME OVER", True, "#ffc20a")
                    WINDOW.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

                elif game_won:
                    game_won_font = pygame.font.Font(None, 74)
                    game_won_text = game_won_font.render("YOU WIN!", True, "#ffc20a")
                    WINDOW.blit(game_won_text, (WIDTH // 2 - game_won_text.get_width() // 2, HEIGHT // 2 - game_won_text.get_height() // 2))

            back_button_2.update(WINDOW)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()

    def play_level_3(self):
        pygame.init()
        WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Galaxy Battle - Level 3")
        clock = pygame.time.Clock()

        ship_x = WIDTH // 2 - self.spaceship_img.get_width() // 2
        ship_y = HEIGHT - 300

        last_shot = pygame.time.get_ticks()
        bullets = []

        monsters = []
        num_monsters = 9
        positions = [
            (WIDTH // 2 - 250, 100), (WIDTH // 2 + 150, 100),  # Вершины X
            (WIDTH // 2 - 150, 200), (WIDTH // 2 + 50, 200),  # Верхние диагональные части
            (WIDTH // 2 - 50, 300),  # Центр X
            (WIDTH // 2 - 150, 400), (WIDTH // 2 + 50, 400),  # Нижние диагональные части
            (WIDTH // 2 - 250, 500), (WIDTH // 2 + 150, 500)  # Основания X
        ]

        for pos in positions:
            monsters.append(Monster(pos[0], pos[1]))

        boss = None
        bonus = None

        back_button_3 = Button(image=None, pos=(45, 20), text_input="BACK", font=pygame.font.Font(None, 35),
                               base_color="#ffc20a",
                               hovering_color="#131112")

        bg_y = 0
        bg_height = BG.get_height()

        game_over = False
        game_won = False
        bonus_active = False

        bonus_monster_index = random.randint(0, num_monsters - 1)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_3.checkForInput(pygame.mouse.get_pos()):
                        return

            for button in [back_button_3]:
                button.changeColor(pygame.mouse.get_pos())

            if not (game_over or game_won):
                keys = pygame.key.get_pressed()
                current_ship_speed = SHIP_SPEED_FAST if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else SHIP_SPEED

                if keys[pygame.K_a] and ship_x > -55:  # Влево
                    ship_speed_x = -current_ship_speed
                elif keys[pygame.K_d] and ship_x < WIDTH - self.spaceship_img.get_width() + 50:  # Вправо
                    ship_speed_x = current_ship_speed
                else:
                    ship_speed_x = 0

                if keys[pygame.K_w] and ship_y > -35:  # Вверх
                    ship_speed_y = -current_ship_speed
                elif keys[pygame.K_s] and ship_y < HEIGHT - self.spaceship_img.get_height() + 35:  # Вниз
                    ship_speed_y = current_ship_speed
                else:
                    ship_speed_y = 0

                current_time = pygame.time.get_ticks()
                if keys[pygame.K_SPACE] and current_time - last_shot > FIRE_RATE:
                    bullet_x = ship_x + self.spaceship_img.get_width() // 2 - self.bullet_img.get_width() // 2
                    bullet_y = ship_y

                    if bonus_active:
                        bullets.append([bullet_x - 40, bullet_y])  # Левая пуля
                        bullets.append([bullet_x + 40, bullet_y])  # Правая пуля
                    else:
                        bullets.append([bullet_x, bullet_y])

                    last_shot = current_time

                # Обновление позиции корабля
                ship_x += ship_speed_x
                ship_y += ship_speed_y

                bg_y += BG_SCROLL_SPEED
                if bg_y >= bg_height:
                    bg_y = 0

                WINDOW.blit(BG, (0, bg_y - bg_height))
                WINDOW.blit(BG, (0, bg_y))

                ship_rect = pygame.Rect(ship_x, ship_y, SHIP_WIDTH, SHIP_HEIGHT)
                WINDOW.blit(self.spaceship_img, (ship_x, ship_y))

                for bullet in bullets:
                    WINDOW.blit(self.bullet_img, (bullet[0], bullet[1]))
                    bullet[1] -= BULLET_SPEED
                    if bullet[1] < 0:
                        bullets.remove(bullet)

                if monsters:
                    for index, monster in enumerate(monsters):
                        monster.draw(WINDOW)
                        if monster.is_hit(bullets):
                            if index == bonus_monster_index and not bonus:
                                bonus_position = (monster.rect.x, monster.rect.y)
                                bonus = Bonus(*bonus_position)
                                bonus_monster_index = None
                            monsters.remove(monster)
                            self.score.add_points(POINTS_PER_MONSTER)
                        if ship_rect.colliderect(monster.rect):
                            game_over = True
                            break

                else:
                    if boss is None:
                        boss = Level3Boss()
                    boss.move()
                    boss.update_bullets()
                    boss.draw(WINDOW)
                    if boss is not None and boss.is_hit(bullets):
                        if boss.health <= 0:
                            self.score.add_points(POINTS_PER_BOSS)
                            boss = None
                            game_won = True
                    if boss is not None and ship_rect.colliderect(boss.rect):
                        game_over = True
                    if boss is not None:
                        for boss_bullet in boss.bullets:
                            if ship_rect.colliderect(
                                    pygame.Rect(boss_bullet[0], boss_bullet[1], BULLET_WIDTH, BULLET_HEIGHT)):
                                game_over = True

                if bonus:
                    bonus.move()
                    bonus.draw(WINDOW)
                    if bonus.is_collected(ship_rect):
                        bonus_active = True
                        bonus = None

                self.score.render(WINDOW, WIDTH - 10, 10)

            else:
                if game_over:
                    game_over_font = pygame.font.Font(None, 74)
                    game_over_text = game_over_font.render("GAME OVER", True, "#ffc20a")
                    WINDOW.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

                elif game_won:
                    game_won_font = pygame.font.Font(None, 74)
                    game_won_text = game_won_font.render("YOU WIN!", True, "#ffc20a")
                    WINDOW.blit(game_won_text, (WIDTH // 2 - game_won_text.get_width() // 2, HEIGHT // 2 - game_won_text.get_height() // 2))

            for button in [back_button_3]:
                button.update(WINDOW)

            pygame.display.update()
            clock.tick(60)

        pygame.quit()
