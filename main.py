import pygame
import sys
from main_menu import main_menu
from config import *
from paddle import Paddle
from ball import Ball
from brick import create_bricks


# Экран окончания игры
def game_over_screen(message, score):
    font = pygame.font.SysFont("Arial", 48)
    small_font = pygame.font.SysFont("Arial", 24)
    running = True

    while running:
        screen.fill(BLACK)

        # Отображение текста
        game_over_text = font.render(message, True, WHITE)
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        restart_text1 = small_font.render("R - перезапуск уровня", True, WHITE)
        restart_text2 = small_font.render("Q - выйти в главное меню", True, WHITE)

        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 4))
        screen.blit(score_text, ((WIDTH - score_text.get_width()) // 2, HEIGHT // 2))
        screen.blit(restart_text1, ((WIDTH - restart_text1.get_width()) // 2, HEIGHT // 1.5))
        screen.blit(restart_text2, ((WIDTH - restart_text1.get_width()) // 2, HEIGHT // 1.5 + 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Обработка клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:  # Перезапуск
            return True
        if keys[pygame.K_q]:  # Выход
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(FPS)


# Главный игровой цикл
def main():
    while True:
        main_menu()

        # Инициализация объектов игры
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
                    pygame.quit()
                    sys.exit()

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
                    running = False
                    restart = game_over_screen("Game Over", score)
                    if restart:
                        break  # Перезапуск игры

            # Если все кирпичи уничтожены
            if not bricks:
                running = False
                restart = game_over_screen("You Win!", score)
                if restart:
                    break  # Перезапуск игры

            # Отрисовка объектов
            paddle.draw()
            ball.draw()
            for brick in bricks:
                brick.draw()

            # Отображение счета и жизней
            font = pygame.font.SysFont("Arial", 24)
            score_text = font.render(f"Очки: {score}", True, 'green')
            lives_text = font.render(f"Жизни: {lives}", True, 'red')
            screen.blit(score_text, (10, 10))
            screen.blit(lives_text, (WIDTH - 100, 10))

            pygame.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    pygame.init()
    main()
