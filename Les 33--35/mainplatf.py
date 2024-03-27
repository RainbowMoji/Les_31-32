import pygame
from level1 import start_level1
from level2 import start_level2

pygame.init()
pygame.mixer.init()
music_sound = pygame.mixer.Sound("pukan.mp3")

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

WIDTH = 420
HEIGHT = 250

BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

button_image = pygame.image.load("button.png")
button_image = pygame.transform.scale(button_image, ((BUTTON_WIDTH, BUTTON_HEIGHT)))
dark_button_image = pygame.image.load("dark_button.png")
dark_button_image = pygame.transform.scale(dark_button_image, ((BUTTON_WIDTH, BUTTON_HEIGHT)))

buttons_list = []

for i in range(1, 7):
    x = (i - 1) % 3 * (BUTTON_WIDTH + 10) + 50
    y = (i - 1) // 3 * (BUTTON_HEIGHT + 10) + 50
    button = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
    buttons_list.append(button)

font = pygame.font.SysFont(None, 30)

background = pygame.image.load("dark_button.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, button in enumerate(buttons_list):
                    if button.collidepoint(event.pos):
                        music_sound.play()
                        level = i + 1
                        exec(f"start_level{str(level)}()")
            if event.button == 2:
                for i, button in enumerate(buttons_list):
                    if button.collidepoint(event.pos):
                        music_sound.play()
                        level = i + 2
                        exec(f"start_level{str(level)}()")


    screen.blit(background, (0, 0))

    for i, button in enumerate(buttons_list):
        if button.collidepoint(pygame.mouse.get_pos()):
            screen.blit(dark_button_image, button)
        else:
            screen.blit(button_image, button)

        text = font.render(str(i + 1), True, BLACK)
        text_rect = text.get_rect(center=button.center)
        screen.blit(text, text_rect)

    pygame.display.flip()