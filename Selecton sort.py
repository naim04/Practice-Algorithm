A=[]
def selection_sort(A):
    for i in range (len(A)-1):
        min=i
        for j in range(i+1,len(A)):
            if A[j]<=A[min]:
                min=j
        if min != i:
                A[i],A[min]=A[min],A[i]

n=int(input("Enter Length:"))
for k in range(n):
    data=int(input())
    A.append(data)
print('After Sortion')
selection_sort(A)
print(A)