import pygame,random,math
from pygame.locals import *
pygame.init()
import tkinter.messagebox
tkinter.Tk().wm_withdraw()#hidding main window
#### game objects
size=(700,400)
fimg=""
gameo=False
bodylst=[]
screen=pygame.display.set_mode((700,420))
food=False
foodx,foody=0,0
head_size=(10,10)
headx,heady=350,200
direction="up"
fps=15
running=True
clock=pygame.time.Clock()
score=0
snk_length=1
bg=pygame.image.load("grass.jpg")
bg=pygame.transform.scale(bg,(700,420))
try:
    with open("snkgame_score.txt","r") as data:
        high_score=data.read()
except:
    high_score=0
#### function sector
def add_food():
    global food,foodx,foody
    foodx=random.randrange(10,size[0],5)
    foody=random.randrange(25,size[1],5)
    food=True

def show_score(msg,size,col=(255,255,0),x=0,y=0):
    global screen,fimg
    font=pygame.font.SysFont(None,size)
    fimg=font.render("score:"+str(msg),True,col)
    screen.blit(fimg,(x,y))
    return fimg
def high_show_score(msg,size,col=(255,255,0),x=0,y=0):
    global screen,fimg
    font=pygame.font.SysFont(None,size)
    fimg=font.render("High Score:"+str(msg),True,col)
    screen.blit(fimg,(x,y))
    return fimg

def plot_snake_body():#increasing body size of snake :)
    bodylst.extend([[headx,heady]])
    for i in range(snk_length-1,0,-1):
        pygame.draw.rect(screen,(120,120,120),(bodylst[i+1][0],bodylst[i+1][1],10,10))
    for k in range(len(bodylst)-snk_length-1):
        bodylst.pop(k)
    

def check_body_colide():
    global gameo
    for i in range(0,len(bodylst)-1):
        if len(bodylst)>0:
            if headx==bodylst[i][0] and heady==bodylst[i][1]:
                gameo=True
                




    


#### main loop
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and direction!="down":
                direction="up"
            if event.key==pygame.K_DOWN and direction!="up":
                direction="down"
            if event.key==pygame.K_LEFT and direction!="right":
                direction="left"
            if event.key==pygame.K_RIGHT and direction!="left":
                direction="right"
    distance=math.sqrt(((headx+5)-foodx)**2+((heady+5)-foody)**2)
    if direction=="up":
        heady-=10
    elif direction=="down":
        heady+=10
    elif direction=="left":
        headx-=10
    elif direction=="right":
        headx+=10
    if heady>400 or heady<20 or headx>690 or headx<0:
        gameo=True
    
    if distance<10:
        food=False
        score+=10
        snk_length+=1
    
    if food==False:
        add_food()
        food=True
    
       
    screen.fill((225,0,0))

    screen.blit(bg,(0,20))
    if gameo==True:
                running=False
    show_score(score,30)
    high_show_score(high_score,30,x=540,y=0)
    pygame.draw.circle(screen,(255,255,255),(foodx,foody),5)
    pygame.draw.rect(screen,(0,0,0),(headx,heady,10,10))
    plot_snake_body()
    check_body_colide()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
if score>int(high_score):
    with open("snkgame_score.txt","w") as data:
        data.writelines(f"{score}")
tkinter.messagebox.showinfo("Game Over",f"Oops you crashed..\nYour score is {score}")
