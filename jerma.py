import pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([1000, 785])
pygame.display.update()
running = True
balls = True
pygame.mixer.music.load("/Users/grahamfielding/Desktop/pygame files/fart.mp3")
pygame.mixer.music.play()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.update()
    jerma = pygame.image.load("/Users/grahamfielding/Desktop/pygame files/Jerma_Serial_Killer.png")
    pygame.Surface.blit(screen, jerma, (0, 0))
    pygame.display.update()
    pygame.time.wait(4000)
    if balls == True:
        pygame.mixer.music.unload()
        pygame.mixer.music.load("/Users/grahamfielding/Desktop/pygame files/saul.mp3")
        pygame.mixer.music.play()
        balls = False
