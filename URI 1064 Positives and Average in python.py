A =[float(input()),float(input()),float(input()),float(input()),float(input()),float(input())]
count=0
c=0.0
for i in range(0,6):
    if A[i] > 0:
        c=c+A[i]
        count = count+1
        ave = c/count
print("%d"%count,"valores positivos")
print("%.1f"%ave)
    
    


