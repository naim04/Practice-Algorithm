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

list=Linkedlist()
list.headval=Node("Sat")
e1=Node("Sun")
e2=Node("mon")
list.headval.nextval=e1
e1.nextval=e2
list.printval()