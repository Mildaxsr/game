import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

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
BRICK_ROWS = 10
BRICK_COLS = 11

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()


class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - 50
        self.speed = PADDLE_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)


class Ball:
    def __init__(self):
        self.radius = BALL_RADIUS
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-1, 1]) * BALL_SPEED
        self.dy = -BALL_SPEED

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Отражение от стен
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx *= -1
        if self.y - self.radius <= 0:
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

    def check_collision_with_paddle(self, paddle):
        if paddle.rect.collidepoint(self.x, self.y + self.radius):
            self.dy *= -1

    def check_collision_with_bricks(self, bricks):
        for brick in bricks:
            if brick.rect.collidepoint(self.x, self.y - self.radius) or \
                    brick.rect.collidepoint(self.x, self.y + self.radius):
                self.dy *= -1
                bricks.remove(brick)
                return True
        return False


class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)


def create_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            x = col * (BRICK_WIDTH + 5) + 20
            y = row * (BRICK_HEIGHT + 5) + 20
            bricks.append(Brick(x, y))
    return bricks


def main():
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()
    lives = 3
    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Логика игры
        paddle.move(keys)
        ball.move()

        # Проверка столкновений
        ball.check_collision_with_paddle(paddle)
        if ball.check_collision_with_bricks(bricks):
            score += 10

        # Если мяч упал за платформу
        if ball.y - ball.radius > HEIGHT:
            lives -= 1
            ball = Ball()  # Новый мяч
            if lives == 0:
                print("Game Over!")
                running = False

        # Если все кирпичи уничтожены
        if not bricks:
            print("You Win!")
            running = False

        # Отрисовка объектов
        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()

        # Отображение счета и жизней
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 100, 10))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
