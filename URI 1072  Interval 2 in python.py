n = int(input())
In=0
Out=0
for i in range(n):
    x=int(input())
    if x>=10 and x<=20:
        In+=1
    else:
        Out+=1
print(In,'in')
print(Out,'out')
