import pygame

screen_height = 480
screen_width = 640

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

x = 30
y = 30
height = 60
width = 60

moveX = 1
moveY = 1

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, height, width))

    if x + width >= screen_width and moveX > 0 or x <= 0 and moveX < 0:
        moveX *= -1

    if y + height >= screen_height and moveY > 0 or y <= 0 and moveY < 0:
        moveY *= -1

    x += moveX
    y += moveY

    pygame.display.flip()