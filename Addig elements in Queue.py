class queue:
    def __init__(self):
        self.queue=[]
    def add(self,data):
        if data!=self.queue:
            self.queue.append(data)
            return True
        else:
            return False
    def size(self):
        return self.queue
list=queue()
list.add("sat")
list.add("sun")
list.add("mon")
print(list.size())