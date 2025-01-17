import pygame, sys, random
from main_menu import *
from config import *
from paddle import *
from ball import *
from brick import *

# Инициализация Pygame, шрифтов
pygame.init()
pygame.font.init()


def main():
    while True:
        main_menu()
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
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
