def hanoi(disks,source,aux,target):
    if disks>=1:
        hanoi(disks-1,source,target,aux)
        move(source,target)
        hanoi(disks-1,aux,source,target)
def move(f,t):
    print("Move disks",f,"to",t);
n=int(input("Enter the number of the disks:"))
hanoi(n,'A','B','C')
