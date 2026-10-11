#

def nextMove(n,r,c,grid):
    # r=x of bot c= y of bot grid is the format n is the no. of lines
    # p is the princess and m is the bot
    x_lst=["LEFT",'RIGHT']
    Y_LST=["DOWN","UP"]
    # coordinate list
    co=[]
    #position of p (princess)
    for i in grid:
        for j in i:
            if j in "Pp":
                xpos_p=i.index(j)
                ypos_p=grid.index(i)
    # distance between p and m
    dis_x=c-xpos_p
    dis_y=r-ypos_p
    
    # no. of row and no. of column
    for i in ["x_term","y_term"]:
        
        if i=="x_term":
            distance=dis_x
            ps=c
            ind=x_lst
        elif i=="y_term":
            distance=dis_y
            ps=r
            ind=Y_LST
        # checking for x axis
        if distance<ps:
            for i in range(abs(distance)):
                co.append(ind[0])
        else:
            for i in range(distance):
                co.append(ind[1])
    return co[0]
n = int(input())
r,c = [int(i) for i in input().strip().split()]#position of bot
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))