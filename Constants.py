import pygame

BG = pygame.image.load("assets/background.png")

WIDTH, HEIGHT = 800, 970 # Размер экрана
SHIP_WIDTH = 100  # Ширина корабля
SHIP_HEIGHT = 100 # Высота корабля
BULLET_WIDTH = 30  # Ширина пули
BULLET_HEIGHT = 45  # Высота пули

SHIP_SPEED = 5 # Скорость корабля
BULLET_SPEED = 8 # Скорость пули
FIRE_RATE = 200 # Частота стрельбы игрока в мс
BG_SCROLL_SPEED = 10 # Скорость прокрутки фона
SHIP_SPEED_FAST = 10 # Увеличенная скорость корабля

MONSTER_HEALTH = 3 # Здоровье монстра
MONSTER_WIDTH = 70 # Ширина монстра
MONSTER_HEIGHT = 40 # Высота монстра
MONSTER_ROW_SPACING = 100  # Расстояние между рядами
MONSTER_COL_SPACING = 60  # Расстояние между колоннами

POINTS_PER_MONSTER = 15 # Количество очков за уничтожение монстра
POINTS_PER_BOSS = 120 # Количество очков за уничтожение босса

BOSS_WIDTH = 500 # Ширина босса
BOSS_HEIGHT = 300 # Высота босса
BOSS_HEALTH = 25 # Количество здоровья босса
BOSS_SPEED = 3 # Скорость движения босса

BONUS_WIDTH = 45 # Ширина бонуса
BONUS_HEIGHT = 45 # Высота бонуса

BULLET_IMAGE = "assets/bullet.png"
SPACESHIP_IMAGE = "assets/spaceship.png"
MONSTER_IMAGE = "assets/monster_1.png"
BOSS_IMAGE = "assets/boss_1.png"
BOSS_IMAGE_2 = "assets/boss_2.png"
BOSS_BULLET_IMAGE = "assets/bullet_2.png"
BOSS_IMAGE_3 = "assets/boss_3.png"

BOSS_WIDTH_3 = 500 # Ширина босса третьего уровня
BOSS_HEIGHT_3 = 400 # Высота босса третьего уровня
