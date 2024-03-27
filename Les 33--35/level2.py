def start_level2(): #Сделать музыку которая играет в твоей кровати
    import pygame
    pygame.init()

    WHITE = (255, 255, 255)
    WIDTH, HEIGHT = 420, 250
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Platform")

    background = pygame.image.load("button.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    player = pygame.image.load("player.png")
    player = pygame.transform.scale(player, (player.get_width() * 2, player.get_height() * 2))

    player_rect = player.get_rect()
    player_rect.topleft = (150, 50)

    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height, image_path):
            super().__init__()
            self.image = image_path
            self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = self.image.get_rect()
            self.rect = (x, y)
            self.hitbox = pygame.Rect(x, y, width, height)

        def draw(self, screen):
            screen.blit(self.image, self.rect)

        def chock_collision(self, player_rect):
            return self.hitbox.colliderect(player_rect)

    clock = pygame.time.Clock()
    platforms = []

    platform_image = pygame.image.load("platform.png")

    def create_platform(x, y, width, height):
        plat = Platform(x, y, width, height, platform_image)
        platforms.append(plat)

    create_platform(10, 200, 175, 25)
    create_platform(200, 100, 175, 25)
    create_platform(200, 10, 175, 25)
    create_platform(100, 200, 175, 25)

    collide_check = False
    gravity = 5
    jump_speed = 15
    player_speed = 3
    jumping = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # reserved

        screen.blit(background, (0, 0))
        screen.blit(player, player_rect)
        for pl in platforms:
            pl.draw(screen)
        pygame.display.update()
        clock.tick(60)
