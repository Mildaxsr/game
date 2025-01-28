from config import *


class Brick:
    def __init__(self, x, y, color='green', strength=1):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color
        self.strength = strength

    def draw(self):
        """Отрисовка кирпича с заданным цветом и прочностью"""
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

    def hit(self):
        """Обработка удара по кирпичу (уменьшение прочности)"""
        self.strength -= 1
        if self.strength <= 0:
            return True  # Уничтожить кирпич
        return False


# Функции для создания уровней с различными кирпичами

def create_bricks_level_1():
    """Создание кирпичей для уровня 1 (стандартные синие кирпичи)"""
    bricks = []
    for i in range(1, BRICK_ROWS):
        for j in range(BRICK_COLS):
            x = j * (BRICK_WIDTH + 5) + 20
            y = i * (BRICK_HEIGHT + 5) + 20
            bricks.append(Brick(x, y, color='blue'))
    return bricks

def create_bricks_level_2():
    """Создание кирпичей для уровня 2 (чередующиеся красные и зеленые кирпичи)"""
    bricks = []
    for i in range(1, BRICK_ROWS):
        for j in range(BRICK_COLS):
            x = j * (BRICK_WIDTH + 5) + 20
            y = i * (BRICK_HEIGHT + 5) + 20
            color = RED if (i + j) % 2 == 0 else GREEN
            bricks.append(Brick(x, y, color=color))
    return bricks

def create_bricks_level_3():
    """Создание кирпичей для уровня 3 (укрепленные кирпичи с разной прочностью)"""
    bricks = []
    for i in range(1, BRICK_ROWS):
        for j in range(BRICK_COLS):
            x = j * (BRICK_WIDTH + 5) + 20
            y = i * (BRICK_HEIGHT + 5) + 20
            strength = 2 if (i + j) % 2 == 0 else 1
            bricks.append(Brick(x, y, color='yellow', strength=strength))
    return bricks
