import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls=[]

def new_ball():
    global x, y, r
    x = randint(100,400)
    y = randint(100,400)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    #circle(screen, color, (x, y), r)
    xmove = randint(-5, 5)
    ymove = randint(-5, 5)
    return [x, y, r, color, xmove, ymove]

def move(ball):
    ball[0]+=ball[4]
    ball[1]+=ball[5]
    if ball[0] - ball[2] <= 0 or ball[0] + ball[2] >= 400:
        ball[4]= -ball[4]
    if ball[1] - ball[2] <= 0 or ball[1] + ball[2] >= 400:
        ball[5]= -ball[5]


popal=0
def click(event,ball):
    global popal
    global distanse
    #print(x, y, r)
    #print('xmouse and ymouse:',get.pos[0],get.pos[1])
    distance=(((event.pos[0]-ball[0])**2)+((event.pos[1]-ball[1])**2))**0.5#расстояние от точки касания до центра
    if (distance<r):
        popal+=1
        print('tap',popal)
        balls.remove(ball)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

for i in range(5):
    balls.append(new_ball())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!',event.pos)
            click(event,ball)

    #new_ball()
    for ball in balls:
        circle(screen, ball[3], (ball[0], ball[1]), ball[2])
        move(ball)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
