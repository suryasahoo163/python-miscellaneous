import pygame,random
from pygame.locals import*
pygame.font.init()
# from pygame import mixer

# mixer.music.load("Sharp Punch-SoundBible.com-1947392621.mp3")
# mixer.music.set_volume(1)

f=open("flappy bird score.txt",'a+')
data=f.read()
    # if len(data)==0:
    #     f.write("0")
f.close()
d=data
######## variables
cor_list=[]
playerx_center,playerx_center=0,0
scr=0
clicked=False
dec=3
placex=50
placey=180
FPS=20
clock=pygame.time.Clock()
barx=300
bary=-200
cor_list.append([barx,bary])

screen=pygame.display.set_mode((300,400))
##### function group
def score_operation():
    global scr,data
    if str(scr)>data:
        data=str(scr)
    return data
        

def inc_score():
    global scr,cor_list,playerx_center,data
    
    for i in cor_list:
        if i[0]==playerx_center:
            scr+=1
    score_operation()        
def render_text(msg,x,y,size):
    font=pygame.font.Font(None,size)
    img=font.render(msg,True,(225,128,0))
    screen.blit(img,(x,y))
def is_colided():
    global placey,placex,cor_list,playerx_center,playerx_center
    playery_center=placey+10
    playerx_center=placex+15
    for i in cor_list:
        if i[0]<playerx_center<i[0]+30 and not(i[1]+300<playery_center<i[1]+450):
            
            return True
def game_over():
    
    global running
    
    print("you crashed")
    running=False
def render_player():
    global placex,placey
    player=pygame.draw.rect(screen,(0,225,0),(placex,placey,30,20))
    return player

def inc_speed():
    global placey,clicked,dec
    
    acc=1
    dec+=acc
    placey+=dec
    if clicked==True:
        dec=2
        clicked=False

def render_bar():
    global barx,bary,cor_list
    
    for i in range(3-(len(cor_list))):
        bary=random.randint(-350,0)
        barx=cor_list[-1][0]+200
        cor_list.append([barx,bary])
    for i in cor_list:
        pygame.draw.rect(screen,(225,128,225),(i[0],i[1],30,300))
        pygame.draw.rect(screen,(225,128,225),(i[0],i[1]+450,30,300))
        i[0]-=5
        if i[0]< -30:
            cor_list.remove(i)
    

running=True
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type==KEYDOWN:
            if event.key==pygame.K_SPACE:
                
                placey-=80
                clicked=True
    if placey>400 or placey<-3 or is_colided():
        # mixer.music.play(1)
        
        game_over()
    
    inc_speed()
    screen.fill((0,128,128))
    render_player()
    inc_score()
    render_bar()
    render_text(f"score:{scr}",10,10,35)
    render_text(f"high score:{data}",150,10,35)
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()

 
if data>d:
    f=open("flappy bird score.txt",'w')

    data=f.write(data)
    # if len(data)==0:
    #     f.write("0")
    print("score saved")
    f.flush()
    f.close()