A =[int(input()),int(input()),int(input()),float(input()),float(input()),int(input())]
count=0
for i in range(0,6):
    if A[i] > 0:
        count = count+1
print(count,"valores positivos")
