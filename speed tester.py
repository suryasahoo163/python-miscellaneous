## making a typing speed tester 
import time,pygame
from pygame.locals import *
pygame.init()
pygame.display.set_caption("typing test")
screen=pygame.display.set_mode((700,400))
#####identifire
txt=""
txt_index=0
ust=""
words_no=0
####### functions
font=pygame.font.SysFont(None,25)
img=font.render(txt,True,(0,0,0))
def count_text():
    global ust,words_no
    for i in ust:
        if i==" ":
            words_no+=1
running=True
started=False
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if started==False:
                start=time.time()
                started=True
            if event.unicode:
                ust+=event.unicode
                
                # if txt[txt_index]==event.unicode:
                #     txt_index+=1
    user_text=font.render(ust,True,(0,0,0),(255,255,255))    
    text_rect = user_text.get_rect(center=(350, 300))            
    screen.fill((0,255,0))
    screen.blit(img,(0,0))
    screen.blit(user_text,text_rect)

    pygame.display.update()

pygame.quit()
stop=time.time()
time_taken=stop-start
count_text()
print(words_no+1)
time_taken=round(time_taken)
print(time_taken)
speed=(60*(words_no+1)//time_taken)
print(f"your speed is {speed} words per minute")

