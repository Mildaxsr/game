import pygame
import sys
import sqlite3
from menu import main_menu
from config import *
from paddle import Paddle
from ball import Ball
from brick import *
from database import *
from levels import *


# Главный игровой цикл
def main():
    while True:
        main_menu()

        player_name = get_player_name()

        level = level_select_screen()

        # Инициализация объектов игры
        paddle = Paddle()
        ball = Ball()
        if level == 1:
            bricks = create_bricks_level_1()
        elif level == 2:
            bricks = create_bricks_level_2()
        else:
            bricks = create_bricks_level_3()

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
                    save_score(player_name, score)  # Сохранение результата
                    restart = game_over_screen("Game Over", score)
                    if restart:
                        break  # Перезапуск игры

            # Если все кирпичи уничтожены
            if not bricks:
                running = False
                save_score(player_name, score)  # Сохранение результата
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
    conn.close()
