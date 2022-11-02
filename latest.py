import pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()
    screenColor = (204, 255, 204)
    screen.fill(screenColor)
    mousePos = pygame.mouse.get_pos()
    print(mousePos)
    size = 50, 50
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(mousePos, size))
    pygame.display.update()