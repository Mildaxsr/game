import pygame

# Параметры окна
WIDTH, HEIGHT = 800, 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройки платформы
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_SPEED = 7

# Настройки мяча
BALL_RADIUS = 10
BALL_SPEED = 5

# Настройки кирпичей
BRICK_WIDTH = 75
BRICK_HEIGHT = 30
BRICK_ROWS = 8
BRICK_COLS = 11

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce & Smash")
clock = pygame.time.Clock()
