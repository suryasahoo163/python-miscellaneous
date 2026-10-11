x=eval(input("enter your list:"))
x=list(x)
for i in range(len(x)//2+1):
    print(i*" ",x[i],((len(x)//2)-i)*2*" ",x[-(i+1)])