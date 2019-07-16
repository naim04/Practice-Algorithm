class stack:
    def __init__(self):
        self.stack=[]
    def add(self,dataval):
        if dataval !=self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):
        return self.stack
    def remove(self):
        if len(self.stack)<=0:
            print("No elements in stack")
        else:
            return self.stack.pop()

list=stack()
list.add("sat")
list.add("sun")
list.add("mon")
list.add('tue')
print(list.peek())
print(list.remove())
print(list.remove())
print(list.remove())