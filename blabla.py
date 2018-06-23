import pygame
import math


pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_blue = True
x0 = 30
y0 = 30
x1 = 420
y1 = 560
x2 = 750
y2 = 150
clock = pygame.time.Clock()
n = 0

speed = 3


x = x0
y = y0
targetX = x1
targetY = y1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: speed += 1
    if pressed[pygame.K_DOWN]: speed -= 1


    dx = targetX - x
    dy = targetY - y
    dz = math.sqrt(dx ** 2 + dy ** 2)
    speedx = dx / dz * speed
    speedy = dy / dz * speed



    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 20, 20))


    x += speedx
    y += speedy
    print(x, y)
    if (x1-2) < x < (x1 + 2) and (y1-2) < y < (y1 + 2):
        print("we came")
        x = x1
        y = y1
        targetX = x2
        targetY = y2

    elif (x2-2) < x < (x2 + 2) and  (y2 - 2) < y < y2 + 2:
        print("we came")
        x = x2
        y = y2
        targetX = x0
        targetY = x0

    elif x0-2 < x < (x0 + 2) and y0-2 < y < (y0 + 2):
        print("we came")
        x = x0
        y = y0
        targetX = x1
        targetY = y1



    pygame.display.flip()
    clock.tick(40)