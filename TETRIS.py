import pygame
pygame.init()
running = True
screen = pygame.display.set_mode((600, 600))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    #draw text in the middle of the screen at font size 40 with color white that says "Hello World!"
    font = pygame.font.Font(None, 40)
    text = font.render("Hello World!", 1, (255, 255, 255))
    textpos = text.get_rect()
    textpos.center = screen.get_rect().center
    screen.blit(text, textpos)
    pygame.display.update()
    pygame.display.flip()