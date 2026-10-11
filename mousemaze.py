
def display(k):
    print("the matrix is")
    for i in range(len(k)):
        print(k[i])


#createe a matrix
mtrx=[]
rootm=[]
n=int(input("enter size of matrix:"))
print("enter elements at")
for i in range(n):
    l=[int(input()) for i in range(n) ]
    mtrx.append(l)
    l=[]
    k=[0 for i in range(n)]
    rootm.append(k)
    k=[]
display(mtrx)

# recurtion function
def checkNext(m,c,r):
    if c+1<len(m):
        if m[c+1][r]==1:
            return True
    if r+1<len(m):
        if m[c][r+1]==1:
            return True
    else:
        return False
    
    
def findrout(m,c=0,r=0):
    global rootm
    rootm[c][r]=1
    print(c,r)
    if c==len(m)-1 and r==len(m)-1:
        return 

    elif checkNext(m,c,r):
        if c+1<len(m):
            if m[c+1][r]==1 :
                findrout(m,c+1,r)
        if r+1<len(m):
            if m[c][r+1]==1:
                findrout(m,c,r+1)
    else:
        if m[c-1][r]==1:
            m[c][r]=0
            rootm[c][r]=0
            findrout(m,c-1,r)
        elif m[c][r-1]==1:
            m[c][r]=0
            rootm[c][r]=0
            findrout(m,c,r-1)
print(findrout(mtrx))            
print("final matrix is\n",display(rootm))
        
            
        