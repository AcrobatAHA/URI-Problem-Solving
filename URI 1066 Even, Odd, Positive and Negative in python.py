A =[int(input()),int(input()),int(input()),int(input()),int(input())]
count=0
c=0
d =0
e = 0
for i in range(0,5):
    if A[i]%2==0:
        c=c+1
        
    if A[i]%2!=0:
        d=d+1
        
    if A[i] > 0:
        count = count+1
        
    if A[i]<0:
        e = e+1
        
   # else:
     #   print()
print(c,"valor(es) par(es)")
print(d,"valor(es) impar(es)")
print(count,"valor(es) positivo(s)")
print(e,"valor(es) negativo(s)")
