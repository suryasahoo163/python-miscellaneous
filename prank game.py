import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,400))
screen.fill((225,155,0))
img=pygame.image.load("donkey.png")
img=pygame.transform.scale(img,((200,130)))
choice=0
##### functions
def changeImage(choice):
    global screen 
    if choice==0:
        screen.blit(img,(200,60))
    else:
        
        screen.blit(img,(200,60))



running=True
while running: 
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
    changeImage(choice)
    pygame.display.update()
pygame.quit()


