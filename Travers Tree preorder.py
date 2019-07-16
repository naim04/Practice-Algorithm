class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def printpreorder(root):
    if root:
        printpreorder(root.left)
        print(root.val)
        printpreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
printpreorder(root)

