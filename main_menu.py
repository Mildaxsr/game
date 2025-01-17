from config import *
import sys
from config import *
import sys


def main_menu():
    running = True
    font = pygame.font.SysFont("Colibri", 48)

    background = pygame.image.load("assets/background.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    while running:
        screen.blit(background, (0, 0))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Отображение текста меню
        title_text = font.render("Main Menu", True, WHITE)
        play_text = font.render("Play", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)

        # Рисуем текст на экране
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        screen.blit(play_text, (WIDTH // 2 - play_text.get_width() // 2, HEIGHT // 2))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 60))

        # Получение позиции мыши и событий
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Обработка нажатий
        play_button = pygame.Rect(WIDTH // 2 - play_text.get_width() // 2, HEIGHT // 2, play_text.get_width(),
                                  play_text.get_height())
        quit_button = pygame.Rect(WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 60, quit_text.get_width(),
                                  quit_text.get_height())

        if play_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GREEN, play_button, 2)  # Подсветка кнопки
            if mouse_click[0]:  # ЛКМ
                return  # Переход в игру

        if quit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GREEN, quit_button, 2)  # Подсветка кнопки
            if mouse_click[0]:  # ЛКМ
                pygame.quit()
                sys.exit()

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)
