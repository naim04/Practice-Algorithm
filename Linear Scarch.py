Arr=[1,2,3,4,5,6,7,8,9,10]
x=int(input("Enter the Number:"))
Found=False
for i in range(len(Arr)):
    if (x==Arr[i]):
        Found=True
        print("%d is in the %d th position"%(x,i+1))
        break

if Found==False:
    print("%d is not in the List"%x)


