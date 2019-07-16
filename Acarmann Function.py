def acarmann(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return acarmann(m-1,1)
    elif m>0 and n>0:
        return acarmann(m-1,acarmann(m,n-1))

m=int(input("Enter m:"))
n=int(input("Enter n:"))
print("Result:",acarmann(m,n))