import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 36)

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('img/Shooter.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 0.5  # скорость по горизонтали
target_speed_y = 0.5  # скорость по вертикали
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def display_score(score):
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

running = True
score = 0

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and \
               target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1

    # Обновление позиции цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка границ экрана и изменение направления движения
    if target_x <= 0 or target_x + target_width >= SCREEN_WIDTH:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
        target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))
    display_score(score)
    pygame.display.flip()

pygame.quit()