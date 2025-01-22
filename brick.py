from config import *


class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)


def create_bricks():
    bricks = []
    for row in range(1, BRICK_ROWS):
        for col in range(BRICK_COLS):
            x = col * (BRICK_WIDTH + 5) + 20
            y = row * (BRICK_HEIGHT + 5) + 20
            bricks.append(Brick(x, y))
    return bricks
