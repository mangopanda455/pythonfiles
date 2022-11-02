import pygame

pygame.mixer.init()
pygame.init()
pygame.image.load("/Users/grahamfielding/Desktop/pygame files/image1.jpeg")
pygame.mixer.music.load("/Users/grahamfielding/Desktop/pygame files/fart.mp3")
#pygame.mixer.music.play()
rectVel = 10
rectX = 100
rectY = 100
basePosX = 0
basePosY = 0
radius = 50
circleX = 50
circleY = 50
running = True

# make a 300 by 300 surface named screen:
screen = pygame.display.set_mode((700, 700))

pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and rectX > 0:
        rectX -= rectVel
    if keys[pygame.K_RIGHT] and rectX < 600:
        rectX += rectVel
    if keys[pygame.K_UP] and rectY > 0:
        rectY -= rectVel
    if keys[pygame.K_DOWN] and rectY < 600:
        rectY += rectVel

    """
    if rectX == 0:
        rectX = 100
    if rectX == 600:
        rectX = 100
    if rectY == 0:
        rectY = 100
    if rectY == 600:
        rectY = 100
    """

    if keys[pygame.K_a] and basePosX > 0:
        basePosX -= rectVel
    if keys[pygame.K_d] and basePosX < 500:
        basePosX += rectVel
    if keys[pygame.K_w] and basePosY > 0:
        basePosY -= rectVel
    if keys[pygame.K_s] and basePosY < 500:
        basePosY += rectVel

    if keys[pygame.K_i] and circleY > 50:
        circleY -= rectVel
    if keys[pygame.K_k] and circleY < 650:
        circleY += rectVel
    if keys[pygame.K_j] and circleX > 50:
        circleX -= rectVel
    if keys[pygame.K_l] and circleX < 650:
        circleX += rectVel

    # Create a variable screenColor and set it to 255,255,255:
    screenColor = (200, 200, 255)

    mousePos = pygame.mouse.get_pos()
    print(mousePos)

    # fill the background with screenColor:
    screen.fill(screenColor)
    # make a polygon called polygon:
    polygon = pygame.draw.polygon(screen, (0, 0, 0), ((basePosX, basePosY), ((basePosX + 200), (basePosY + 150)), ((basePosX + 150), (basePosY + 200))))
    # make a black 100 by 100 square at position 100 100 with line width of 2:
    square = pygame.draw.rect(
        screen, (0, 0, 0), pygame.Rect(rectX, rectY, 100, 100), 2)
    pygame.draw.circle(
        screen, (0, 0, 0), mousePos, radius,
    )
    pygame.display.update()
