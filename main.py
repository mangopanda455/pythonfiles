import pygame
ellipseRectX = 250
ellipseRectY = 100
flipRectX = 100
flipRectY = 250
ellipseRectPosX = (300 - ellipseRectX)/2
ellipseRectPosY = (300 - ellipseRectY)/2
flipRectPosX = (300 - flipRectX)/2
flipRectPosY = (300 - flipRectY)/2
print(ellipseRectPosX, ellipseRectPosY, "\n", flipRectPosX, flipRectPosY)
triPoints = [(100, 200), (200, 200), (150, 100)]
hexPoints = [(100, 125), (100, 175), (125, 200), (175, 200), (200, 175), (200, 125), (175, 100), (125, 100)]
background_colour = (224, 176, 255)
screen = pygame.display.set_mode([300, 300])

# For alpha testing
"""
s = pygame.Surface((300, 300))  # the size of your rect
s.set_alpha(128)                # alpha level
s.fill((255,255,255))           # this fills the entire surface
"""
# s.blit(s, (0, 0))  # (0,0) are the top-left coordinates <====== Put in main loop when ready

pygame.display.set_caption("When the")
screen.fill(background_colour)
running = True
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 100, 100), 2)
pygame.draw.circle(screen, (0, 255, 0), (150, 150), 50, 2)
pygame.draw.polygon(screen, (0, 0, 255), triPoints, 2)
pygame.draw.polygon(screen, (0, 0, 0), hexPoints, 2)
pygame.draw.ellipse(screen, (0, 255, 255), pygame.Rect(ellipseRectPosX, ellipseRectPosY, ellipseRectX, ellipseRectY), 2)
pygame.draw.ellipse(screen, (255, 255, 0,), pygame.Rect(flipRectPosX, flipRectPosY, flipRectX, flipRectY), 2)
while running:
    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
