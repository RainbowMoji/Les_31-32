import random

import pygame

pygame.init()

cloud_speed = 0.75
cactus_speed = 0.5

WIDTH = 600
HEIGHT = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 300

dino_img = pygame.image.load("dino.png")
cactus_img = pygame.image.load("cactus.png")
cloud_img = pygame.image.load("cloud.png")
gameover_img = pygame.image.load("gameover.png")

dino_x = 20
dino_y = HEIGHT - 50
velocity = 0
dino_jumping = False

cloud_list = []
cactus_list = []

next_cactus_time = 1
next_cloud_time = 1


def jump():
    global velocity, dino_jumping
    if not dino_jumping:
        velocity = -1
        dino_jumping = True


def create_cactus():
    cactus_x = WIDTH
    cactus_y = HEIGHT - 50
    cactus_list.append((cactus_x, cactus_y))


create_cactus()

def create_cloud():
    cloud_x = WIDTH
    cloud_y = random.randint(10, HEIGHT // 2)
    cloud_list.append((cloud_x, cloud_y))
create_cloud()

button_height = gameover_img.get_height()
button_width = gameover_img.get_height()

button_x = WIDTH // 2 - button_width // 2
button_y = HEIGHT // 2 - button_height // 2

button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
button_show = False
paused = False


def press_button():
    global button_show, paused
    while len(cactus_list) != 0:
        cactus_list.pop(0)
    paused = False
    button_show = False
    create_cactus()


def draw_button():
    if button_show == True:
        global paused
        paused = True
        screen.blit(gameover_img, button_rect)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and button_show == True:
                press_button()

    if not paused:
        for i in range(len(cactus_list)):
            cactus_x, cactus_y = cactus_list[i]
            cactus_x -= cactus_speed
            if cactus_x + cactus_img.get_width() < 0:
                cactus_list.pop(i)
                break
            cactus_list[i] = (cactus_x, cactus_y)

    if cactus_list[-1][0] < WIDTH - random.randint(125, 225):
        next_cactus_time -= 0.1
        if next_cactus_time <= 0:
            create_cactus()
            next_cactus_time = random.randint(1, 40)

    dino_y += velocity
    velocity += 0.01
    if dino_y >= HEIGHT - 50:
        dino_y = HEIGHT - 50
        velocity = 0
        dino_jumping = False

    for cactus_x, cactus_y in cactus_list:
        if dino_x + dino_img.get_width() > cactus_x and \
                dino_x < cactus_x + cactus_img.get_width() and \
                dino_y + dino_img.get_height() > cactus_y and \
                dino_y < cactus_y + cactus_img.get_height():
            button_show = True

    if not paused:
        for o in range(len(cloud_list)):
            cloud_x, cloud_y = cloud_list[o]
            cloud_x -= cloud_speed
            if cloud_x + cloud_img.get_width() < 0:
                cloud_list.pop(o)
                break
            cloud_list[o] = (cloud_x, cloud_y)

    if cloud_list[-1][0] < WIDTH - 15:
        next_cloud_time -= 0.1
        if next_cloud_time <= 0:
            create_cloud()
            next_cloud_time = random.randint(1, 40)


    screen.fill((255, 255, 255))
    screen.blit(dino_img, (dino_x, dino_y))
    for cactus_x, cactus_y in cactus_list:
        screen.blit(cactus_img, (cactus_x, cactus_y))
    for cloud_x, cloud_y in cloud_list:
        screen.blit(cloud_img, (cloud_x, cloud_y))

    draw_button()
    pygame.display.update()
    clock.tick(FPS)
