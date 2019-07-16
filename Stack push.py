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
list=stack()
list.add("sat")
list.add("sun")
print(list.peek())
list.add("mon")
list.add('tue')
print(list.peek())