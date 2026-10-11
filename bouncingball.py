import pygame
from pygame.mixer import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("1417.mp3")
pygame.mixer.music.set_volume(1)
x,y=300,400
screen=pygame.display.set_mode((x,y))
pygame.display.set_caption("Bouncing Ball")
ballx,bally=150,30
fps=60
clock=pygame.time.Clock()
speed=-1
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if bally<=30:
        speed=1
    if bally>=340:
        speed=-1
        pygame.mixer.music.play()
    bally+=speed*(bally//20)
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(0,0,225),(ballx,bally),20)
    pygame.draw.rect(screen,(225,0,0),(0,370,300,400))
    clock.tick(fps)
    pygame.display.update()
pygame.quit()
