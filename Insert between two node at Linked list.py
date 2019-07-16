class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def printval(self):
        printval=self.headval
        while printval!=None:
            print(printval.dataval)
            printval=printval.nextval
    def Inbetween(self,midnode,newnode):
        if midnode==None:
            print("The mension node is absent")
            return
        Newnode=Node(newnode)
        Newnode.nextval=midnode.nextval
        midnode.nextval=Newnode

list=Linkedlist()
list.headval=Node("sat")
e1=Node("sun")
e2=Node("tue")
list.headval.nextval=e1
e1.nextval=e2
list.Inbetween(list.headval.nextval,"mon")
list.printval()