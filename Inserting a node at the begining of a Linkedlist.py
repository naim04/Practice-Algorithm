class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None

class Linkedlist:
    def __init__(self):
        headval=None
    def printval(self):
        printval=self.headval
        while printval!=None:
            print(printval.dataval)
            printval=printval.nextval
    def Atbeg(self,newdata):
        Newnode=Node(newdata)
        Newnode.nextval=self.headval
        self.headval=Newnode

list=Linkedlist()
list.headval=Node("sat")
e1=Node("sun")
e2=Node("mon")
list.headval.nextval=e1
e1.nextval=e2
list.Atbeg("fri")
list.printval()