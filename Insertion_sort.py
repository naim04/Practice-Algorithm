a=[]
def insertion_sort(a):
    for i in range(1,len(a)):
        for j in range(i-1,-1,-1):
            if a[j+1]<a[j]:
                a[j+1],a[j]=a[j],a[j+1]
            else:
                break

n=int(input("Enter length:"))
for k in range(n):
    data=int(input())
    a.append(data)
print("After Sorting")
insertion_sort(a)
print(a)