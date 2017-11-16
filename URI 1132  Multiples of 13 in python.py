x=int(input())
y=int(input())
total=0
if x>y:
    for i in range(y,x+1):
        if i%13!=0:
            total+=i
    
elif x<y:
    for i in range(x,y+1):
        if i%13!=0:
            total+=i

print(total)            
