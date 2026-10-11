#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    #now m is the bot and p is the queen
    lst_y=['RIGHT',"LEFT"]
    lst_x=['UP','DOWN']
    position_p=None
    position_m=None
    it=0
    for i in grid:
        it+=1
        for j in i:
            if j in ["m",'M']:
                position_m=[it,i.index(j)+1]
            elif j in ["p","P"]:
                position_p=[it,  i.index(j)+1]
    steps=[]
    y_pos=position_m[1]-position_p[1]
    x_pos=position_m[0]-position_p[0]
    c=0
    x,y=x_pos,y_pos
    co=position_p[0]
    cs=lst_x
    i=x_pos
    if i<co:
        for j in range(abs(i)):
            steps.append(cs[1])
    elif i>=co:
        for j in range(i):
            steps.append(cs[0])
            
            
    i=y_pos
    co=position_p[1]
    cs=lst_y
    if i<co:
        for j in range(abs(i)):
            steps.append(cs[0])
    elif i>=co:
        for j in range(i):
            steps.append(cs[1])
        
    for i in steps:
        print(i)
mn = int(input())
grid = [] 
for i in range(0, mn): 
    grid.append(input().strip())

displayPathtoPrincess(mn,grid)