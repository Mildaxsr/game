from main import *
import sys
import sqlite3

conn = sqlite3.connect("game_scores.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, player_name TEXT, score INTEGER)")
conn.commit()


def save_score(player_name, score):
    cursor.execute("INSERT INTO scores (player_name, score) VALUES (?, ?)", (player_name, score))
    conn.commit()


# Функция для получения лучшего рекорда
def get_best_score():
    cursor.execute("SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 1")
    result = cursor.fetchone()
    return result if result else ("None", 0)


# Экран ввода имени игрока
def get_player_name():
    font = pygame.font.SysFont("Arial", 32)
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BLACK)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        prompt_text = font.render("Введите ваше имя и нажмите Enter:", True, WHITE)
        screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 2 - 60))

        pygame.display.flip()
        clock.tick(FPS)

    return text
