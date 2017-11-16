n = int(input())
a=[]
for i in range(1,n+1):
    a.append(int(input()))
for i in range(0,n):
    if a[i]==0:
        print("NULL")
    elif a[i]%2==0 and a[i]<0:
        print("EVEN NEGATIVE")
    elif a[i]%2==0 and a[i]>0:
        print("EVEN POSITIVE")
    elif a[i]%2!=0 and a[i]<0:
        print("ODD NEGATIVE")
    elif a[i]%2!=0 and a[i]>0:
        print("ODD POSITIVE")
