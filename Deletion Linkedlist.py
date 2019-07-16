class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
        self.preval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def printval(self):
        printval=self.headval
        while printval!=None:
            print(printval.dataval)
            printval=printval.nextval

    def scarch(self,k):
        p=self.headval
        if p!=None:
            while p.nextval!=None:
                if p.dataval==k:
                    return p
                p=p.nextval
            if p.dataval==k:
                return p
        return None
    def remove(self,k):
        if self.headval==k:
            self.headval=self.headval.nextval
        else:
            tmp = k.preval
            k.preval.nextval = k.nextval
            k.preval = tmp

list=Linkedlist()
list.headval=Node("sat")
e1=Node("Sun")
e2=Node("Mon")
list.headval.nextval=e1
e1.nextval=e2
list.headval.preval=None
e1.preval=list.headval
e2.preval=e1
list.printval()
list.remove(list.scarch("Mon"))
list.printval()
