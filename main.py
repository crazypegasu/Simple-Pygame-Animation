import pygame as cerebro 
import sys 
import random


WHITE = (000,000,000)
BLACK = (255,255,255)
RED = (255,000,000)
GREEN = (000,255,000)
gay = (000,200,200)
BLUE = (000,000,255)


LARGURA = 800 # x em coordenada 
ALTURA = 600 # y em coordenada 

screen = cerebro.display.set_mode([LARGURA,ALTURA])

rodando = True 

vx = 25
vy = 25
x = 1
y = 1

while rodando:
    for event in cerebro.event.get():
        if event.type == cerebro.QUIT:
            rodando = False

    screen.fill((BLACK))
    COLOR = [WHITE,RED,GREEN,gay,BLUE]
    cor = ()
    cerebro.draw.circle(screen, (WHITE), (vx,vy), 25)
    vx += x
    vy += y
    if vx + 25 > LARGURA or vx - 25 < 0:
        x *= -1
        listaCor = random.choice(COLOR)
        WHITE = listaCor
        print(WHITE)

    if vy + 25 > ALTURA or vy - 25 < 0:
        y *= -1
        listaCor = random.choice(COLOR)
        WHITE = listaCor
        print(WHITE)
  
    cerebro.time.delay(5)
    cerebro.display.flip()
cerebro.quit()