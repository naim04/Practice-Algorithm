class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def printlist(self):
        printval=self.headval
        while printval!=None:
            print(printval.dataval)
            printval=printval.nextval

    def scarch(self,k):
        p=self.headval
        if p!=None:
            while p.nextval!=None:
                if p.dataval==k:
                    return True
                p=p.nextval
            if p.dataval==k:
                return True
        return False

list=Linkedlist()
list.headval=Node("sat")
e1=Node("Sun")
e2=Node("Mon")
list.headval.nextval=e1
e1.nextval=e2
list.printlist()
print("Given node is",list.scarch("sat"))
