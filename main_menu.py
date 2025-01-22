from config import *
import sys


def game_over_screen():
    running = True
    font = pygame.font.SysFont("Colibri", 48)
    pygame.mixer.init()
    background = pygame.image.load("assets/game_over.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    sound = pygame.mixer.Sound("assets/sound_lose.mp3")

    sound.play()

    while running:
        screen.blit(background, (0, 0))

        title_text = font.render("Game Over", True, WHITE)
        main_menu_text = font.render("Main Menu", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        screen.blit(main_menu_text, (WIDTH // 2 - main_menu_text.get_width() // 2, HEIGHT // 2))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 60))

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Обработка нажатий
        main_menu_button = pygame.Rect(WIDTH // 2 - main_menu_text.get_width() // 2, HEIGHT // 2,
                                       main_menu_text.get_width(), main_menu_text.get_height())
        quit_button = pygame.Rect(WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 60,
                                  quit_text.get_width(), quit_text.get_height())

        if main_menu_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GREEN, main_menu_button, 2)
            if mouse_click[0]:
                return  # Переход в главное меню

        if quit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GREEN, quit_button, 2)
            if mouse_click[0]:  # ЛКМ
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

def game_loop():
    for _ in range(300):
        pass
    game_over_screen()


def main_menu():
    running = True
    font = pygame.font.SysFont("Colibri", 48)
    pygame.mixer.init()
    background = pygame.image.load("assets/background.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    pygame.mixer.music.load("assets/background_music.mp3")
    pygame.mixer.music.play(-1)
    sound = pygame.mixer.Sound("assets/sound_button.wav")
    while running:
        screen.blit(background, (0, 0))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Отображение текста меню
        title_text = font.render("Главное меню", True, WHITE)
        play_text = font.render("Играть", True, WHITE)
        quit_text = font.render("Выход", True, WHITE)

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
                pygame.mixer.music.stop()
                sound.play()
                pygame.time.wait(int(sound.get_length() * 1000))
                return  # Переход в игру

        if quit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, GREEN, quit_button, 2)  # Подсветка кнопки
            if mouse_click[0]:  # ЛКМ
                sound.play()
                pygame.time.wait(int(sound.get_length() * 1000))
                pygame.quit()
                sys.exit()

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)