from config import *
from main import *


def level_select_screen():
    font = pygame.font.SysFont("Arial", 32)
    small_font = pygame.font.SysFont("Arial", 24)
    level_text = font.render("Выберите уровень", True, WHITE)
    level_1_text = small_font.render("1 - Стандартный уровень", True, WHITE)
    level_2_text = small_font.render("2 - Уровень с цветными кирпичами", True, WHITE)
    level_3_text = small_font.render("3 - Уровень с укрепленными кирпичами", True, WHITE)
    running = True

    while running:
        screen.fill(BLACK)
        screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 4))
        screen.blit(level_1_text, (WIDTH // 2 - level_1_text.get_width() // 2, HEIGHT // 2))
        screen.blit(level_2_text, (WIDTH // 2 - level_2_text.get_width() // 2, HEIGHT // 1.5))
        screen.blit(level_3_text, (WIDTH // 2 - level_3_text.get_width() // 2, HEIGHT // 1.25))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            return 1  # Выбор уровня 1
        if keys[pygame.K_2]:
            return 2  # Выбор уровня 2
        if keys[pygame.K_3]:
            return 3  # Выбор уровня 3

        pygame.display.flip()
        clock.tick(FPS)


# Экран окончания игры
def game_over_screen(message, score):
    font = pygame.font.SysFont("Arial", 48)
    small_font = pygame.font.SysFont("Arial", 24)
    running = True

    best_player, best_score = get_best_score()

    while running:
        screen.fill(BLACK)

        # Отображение текста
        game_over_text = font.render(message, True, WHITE)
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        best_score_text = small_font.render(f"Best: {best_player} - {best_score}", True, 'gold')
        restart_text1 = small_font.render("R - Выйти в главное меню", True, WHITE)
        restart_text2 = small_font.render("Q - Выйти из игры", True, WHITE)

        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 4))
        screen.blit(score_text, ((WIDTH - score_text.get_width()) // 2, HEIGHT // 2))
        screen.blit(best_score_text, ((WIDTH - best_score_text.get_width()) // 2, HEIGHT // 2 + 40))
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
