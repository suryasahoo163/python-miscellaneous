#### module sector #####
import os
from tkinter import *
from tkinter import filedialog
import pygame.mixer 
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
##########################  global vaiable    ################################################
SONG_NAME=''
SONG_LIST=[]
SONG_INDEX=0
VOLUME=0.0
types='PAUSE'
STARTED=True
PLAYED=False
lst1=[]
SONG_LIST_ULTIMATE=[]
LOCATION=''
SONG_ADDED=False
bgc='gray25'
fgc='snow'

########################## function sector   ###################################################
def lists():
    global SONG_ADDED,bgc,fgc,SONG_NAME
    new_root=Tk()
    
    new_root.configure(bg=bgc)
    Label(new_root,text='PLAYLIST',fg=fgc,bg=bgc).pack()
    new_root.geometry('200x300')
    new_root.resizable(False,False)
    new_root.title('SONG LIST')
     #### function
    def playselected():
        global SONG_INDEX,SONG_LIST_ULTIMATE
        CURSOR_PLAY=lst.curselection()
        pygame.mixer.music.load(LOCATION+lst.get(CURSOR_PLAY))
        pygame.mixer.music.play()
        CURSOR_PLAY=list(CURSOR_PLAY)
        SONG_INDEX=CURSOR_PLAY[0]
        
        
    #### selecting from the list and playing###
    Button(new_root,text='PLAY',command=playselected,width=30,bg=bgc,fg=fgc,relief='raised').pack(side='top')
    #Button(new_root,text="add song",command=add).pack()
    lst=Listbox(new_root,selectmode='single',width=30,bg=bgc,fg=fgc)
    sc=Scrollbar(new_root,bg=bgc)
    lst.config(yscrollcommand=sc.set)
    sc.config(command=lst.yview)
    sc1=Scrollbar(new_root,orient='horizontal',bg=bgc)
    lst.config(xscrollcommand=sc1.set)
    sc1.config(command=lst.xview)
    sc1.pack(side='bottom',fill='x')
    lst.pack(side='left',fill='both')
    sc.pack(side='right',fill='y')
    if PLAYED==False:
        lst1.clear()
        SONG_LIST_ULTIMATE.clear()
        for k in SONG_LIST:
            lst1.append(k)
        lst.clipboard_clear()
        for i in lst1:
            i=i.replace('\\',"/")
            l=len(i)-1
            for j in range(l,0,-1):
                if i[j]=='/':
                    SONG_LIST_ULTIMATE.append(i[j+1:len(i)])
                    break
    for item in SONG_LIST_ULTIMATE:
        lst.insert(END,item)
    new_root.mainloop()
#####################    
   
    
    

##########################3
def play():
    global types,b1
    if types=="PLAY":
        pygame.mixer.music.unpause()
        types='PAUSE'
        b1['text']='PAUSE'
    elif types=="PAUSE":
        pygame.mixer.music.pause()
        types="PLAY"
        b1['text']='PLAY'

def sng():
    global SONG_LIST,SONG_INDEX
    
    if SONG_INDEX >= len(SONG_LIST):
        SONG_INDEX=SONG_INDEX % len(SONG_LIST)
    elif SONG_INDEX < -(len(SONG_LIST)):
        SONG_INDEX=SONG_INDEX % len (SONG_LIST)  

def change(a):
    global SONG_INDEX
    if a==1:
        SONG_INDEX+=1
    else:
        SONG_INDEX-=1
    
    sng()#### gives the actual index
    pygame.mixer.music.load(SONG_LIST[SONG_INDEX])
    SONG_NAME=SONG_LIST[SONG_INDEX]
    #NM['text']=SONG_NAME    
    pygame.mixer.music.play()
    return SONG_INDEX
def volume(a):
    global VOLUME
    if a==1:
        VOLUME+=0.2
    else:
        VOLUME-=0.2
    pygame.mixer.music.set_volume(VOLUME)
    
    
############################# main program############################
#####  root area######
root=Tk()
root.geometry('200x300')
root.resizable(False,False)
root.title('mp3 player made by surya ;)')
root.config(bg=bgc)
######## body area####
Button(root,text='PLAYLIST',command=lists).grid(column=0,row=1)
#playlist button
frame=Frame(root,bg=bgc)
### image area
##### control button area###
b1=Button(frame,text=types,command=play)
b1.grid(row=1,column=1)
Button(frame,text='NEXT',command=lambda:change(1)).grid(row=1,column=2)
Button(frame,text='PREVIOUS',command=lambda:change(2)).grid(row=1,column=0)
Button(frame,text='VOLUME UP',command=lambda:volume(1)).grid(row=0,column=1)
Button(frame,text='VOLUME DOWN',command=lambda:volume(2)).grid(row=2,column=1)
frame.grid()
##### song entry###
SONG_LIST=filedialog.askopenfilenames()
SONG_LIST=list(SONG_LIST)
sample=SONG_LIST[0]
sample=sample.replace('\\','/')
for k in range(len(sample)-1,0,-1):
    if SONG_LIST[0][k]=='/':
        LOCATION=SONG_LIST[0][0:k]+'/'
        break
#print(SONG_LIST)
pygame.mixer.music.load(SONG_LIST[SONG_INDEX])
if pygame.mixer.music.get_busy()==False:
    pygame.mixer.music.play()
root.mainloop()
### enjoy your day with this beautifull song###
