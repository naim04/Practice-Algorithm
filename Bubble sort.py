def bubble_sort(arr):
    for i in range (len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[]
n=int(input('Enter Elements Number:'))
print('Enter elements:')
for k in range(n):
    data=int(input())
    arr.append(data)

print("After Sorting")
bubble_sort(arr)
print(arr)