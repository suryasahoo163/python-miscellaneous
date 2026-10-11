import pygame
from pygame import *
from pygame.mixer import *
import socket
import pickle,math

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=163
ip="192.168.50.158"
skt.connect((ip,port))
pygame.init()
pygame.mixer.init()

#variables
bg=pygame.image.load("stars.jpg")
bg=pygame.transform.scale(bg,(800,500))

plane=pygame.image.load("Daco_619823.png")
plane=pygame.transform.scale(plane,(70,70))
eplane=pygame.transform.rotate(plane,(180))

sound=pygame.mixer.music
sound.load("blaster.mp3")
sound.set_volume(1)

fps=60
pspeed=5
bspeed=10
screen=pygame.display.set_mode((800,500))
clock=pygame.time.Clock()
running=True
planeYValue=400
enemyplaneX=myplaneX=400

redbullet=pygame.image.load("enemyshoot.png")
redbullet=pygame.transform.scale(redbullet,(6,30))

newbullet=pygame.image.load("myshoot.png")
newbullet=pygame.transform.scale(newbullet,(6,30))
    
ebullet=[]
pbpos=[]
moveR=moveL=False
myScore=enemyScore=0
propertyDict={"planePos":myplaneX,"score":myScore,"bulletPos":pbpos}

colorC=(125,225,0)
font = pygame.font.Font('freesansbold.ttf', 20)
img1=font.render(f"My score {myScore}",True,colorC)
img2=font.render(f"Opponent {enemyScore}",True,colorC)
pvscore=0
###### methods
def fire(x,y):
    pbpos.append([x-3,y-20])
   
def displaybullet():
    global newbullet,screen,pbpos,propertyDict
    distance=10
    for i in range(len(pbpos)):
        if pbpos[i][1]<=5:
            pbpos.pop(i)
            break           
        pbpos[i][1]-=distance
        screen.blit(newbullet,(pbpos[i][0],pbpos[i][1]))
    propertyDict["bulletPos"]=pbpos
    return propertyDict

        
            
### recieve data from server

def recieveData():
    
    s=skt.recv(1024*5)
    value=pickle.loads(s)
    
    return value

def blitenemy():
    global screen,eplane,redbullet,myScore,enemyScore,propertyDict,pvscore,pbpos
    try:
        enemyData=recieveData()
        # print("ed",enemyData)
        # bullets=enemyData[1]
        screen.blit(eplane,(800-enemyData["planePos"]-35,500-planeYValue-70))
        
        myScore=enemyData["score"]
        
        
        for i in range(len(enemyData["bulletPos"])):
            screen.blit(redbullet,(800-enemyData["bulletPos"][i][0]-5,500-enemyData["bulletPos"][i][1]-25))

        for i in range(len(enemyData["bulletPos"])):
            if (myplaneX < 800-enemyData["bulletPos"][i][0]+3 < myplaneX+35) and (planeYValue < 500-enemyData["bulletPos"][i][1]+30 < planeYValue+35):
                enemyScore+=1
              
                propertyDict["score"]=enemyScore
           
                
                pbpos.pop(0)
                pvscore=myScore
    
                propertyDict["bulletPos"]=pbpos
        
    except socket.error as e:
        print(e)

###### sending data to server
def sendData(d):
    byte=pickle.dumps(d)
    skt.send(byte)
    
def sendMyData():
    global propertyDict
    data=propertyDict
    try:
        sendData(data)     
    except:
        print("server not found")
        
#### main loop      
while running:
    for event in pygame.event.get():
       
        if event.type==pygame.QUIT:
            running=False
            break
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                moveL=True
            if event.key==pygame.K_RIGHT:
                moveR=True
            if event.key==pygame.K_UP:
                sound.set_volume(0)
                fire(myplaneX,planeYValue)
                sound.set_volume(1)
                sound.play()
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                moveL=False
            if event.key==pygame.K_RIGHT:
                moveR=False
                
    if(moveL and myplaneX>35):
        myplaneX-=pspeed
    if(moveR and (800-35)>myplaneX):
        myplaneX+=pspeed
    
    screen.blit(bg,(0,0))
    displaybullet()
    screen.blit(plane,(myplaneX-35,planeYValue))#player
    propertyDict["planePos"]=myplaneX

    #sending data to server
    try:
        sendMyData()
    except:
        pass
    #getting data and ploting in game from the server
    try:
        blitenemy()
    except:
        pass
    img1=font.render(f"My score {myScore}",True,colorC)
    img2=font.render(f"Opponent {enemyScore}",True,colorC)
    screen.blit(img1,(10,10))
    screen.blit(img2,(800-130-10,10))
    
            
    pygame.display.update()
    clock.tick(fps)
pygame.quit()



