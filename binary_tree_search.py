


class BST:
    def __init__(self,data):
        self.head=data
        self.left=None
        self.right=None
        self.lst=[]
  
    def entry(self,data):
        if data==self.head:
            return self.head
        elif data<self.head:
     
            if self.left:
                # print(self.left,"\n\t",data)
                self.left.entry(data)
            elif self.head>data:
                self.left=BST(data)
        elif data>self.head:
         
            if self.right:
                # print(self.right," \n\t",data)
                self.right.entry(data)
            elif self.head<data:
                self.right=BST(data)
        self.lst.append([self.left,data,self.right])
    def show(self):
        for i in self.lst:
            print(i)
b=BST(10)
import random
for i in range(15):
    d=random.randint(2,60)
    b.entry(d)
b.show()

