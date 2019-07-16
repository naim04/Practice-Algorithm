def binary_scarch(arr,l,h,x):
    while(l<=h):
        mid=int(l+(h-l)/2)
        if arr[mid]==x:
            return mid
        elif(arr[mid]<x):
            l=mid+1
        else:
            h=mid-1
    return -1

arr=[2,3,4,5,1,6,7,8,9,12,34]
arr.sort()
x=int(input("Enter the Scarching Number:"))
result=binary_scarch(arr,0,len(arr)-1,x)
if result==-1:
    print("%d is not in the list"%x)
else:
    print("%d Finds in the %d th position" % (x,result+1))
