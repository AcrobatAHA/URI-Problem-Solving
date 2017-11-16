A =[int(input()),int(input()),int(input()),int(input()),int(input())]
count=0
for i in range(0,5):
    if A[i]%2==0:
        count = count+1
print(count,"valores pares")
