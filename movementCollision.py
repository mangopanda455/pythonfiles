import pygame
pygame.init()
running = True
screen = pygame.display.set_mode((600, 600))
rect1 = pygame.Rect(0, 0, 75, 75)
color = (255, 0, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill(0)
    rect1.center = pygame.mouse.get_pos()
    pygame.draw.rect(screen, color, rect1, 6, 1)
    pygame.display.update()
    pygame.display.flip()
