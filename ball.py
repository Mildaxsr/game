from config import *
import random, pygame



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
