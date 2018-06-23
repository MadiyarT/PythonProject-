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
speed = 0
a = True
b = False
c = False

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

    if x0<=x<(x0+x1)/2 and y0<=y<(y0+y1)/2 and a:
        speed+=0.2
    elif (x0+x1)/2<=x<x1 and (y0+y1)/2<=y<y1 and a:
        speed-=0.2
        not is_blue
    if x1<=x<(x2+x1)/2 and y1>=y>(y2+y1)/2 and b:
        speed+=0.2
        is_blue
    elif (x2+x1)/2<=x<x2 and (y2+y1)/2>=y>y2 and b:
        speed-=0.2
        not is_blue
    if x2>=x>(x0+x2)/2 and y2>=y>(y0+y2)/2 and c:
        speed+=0.2
        is_blue
    elif (x0+x2)/2>x>=x0 and (y0+y2)/2>y>=y0 and c:
        speed-=0.2
        not is_blue


    x += speedx
    y += speedy
    print(x, y, dz)

    if (x1 - 0.6) < x < (x1 + 0.6) and (y1 - 0.6) < y < (y1 + 0.6):
        print("we came")
        print(speed)
        speed = 1
        x = x1
        y = y1
        targetX = x2
        targetY = y2
        a = False
        b = True
        c = False

    elif (x2 - 0.5) < x < (x2 + 0.5) and (y2 - 0.5) < y < y2 + 0.5:
        print("we came")
        print(speed)
        speed = 1
        x = x2
        y = y2
        targetX = x0
        targetY = x0
        a = False
        b = False
        c = True


    elif x0 - 0.5 < x < (x0 + 0.5) and y0 - 0.5 < y < (y0 + 0.5):
        print("we came")
        print(speed)
        speed = 1
        x = x0
        y = y0
        targetX = x1
        targetY = y1
        a =True
        b = False
        c = False

    pygame.display.flip()
    clock.tick(40)