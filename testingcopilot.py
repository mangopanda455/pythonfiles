import pygame
pygame.init()
running = True
screen = pygame.display.set_mode((600, 600))
rect1 = pygame.Rect(0, 0, 100, 100)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    color = (0, 255, 0)
    rect1.center = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (color), rect1, 5)
    pygame.display.update()
    pygame.display.flip()