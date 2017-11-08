x,y=input().split()
x = int(x)
y = int(y)
if x==1:
    price=y*4.0
    print('Total: R$ %.2lf'%price)
elif x==2:
    price=y*4.50
    print('Total: R$ %.2lf'%price)
elif x==3:
    price=y*5.0
    print('Total: R$ %.2lf'%price)
elif x==4:
    price=y*2.0
    print('Total: R$ %.2lf'%price)
elif x==5:
    price=y*1.50
    print('Total: R$ %.2lf'%price)
else:
    print()
