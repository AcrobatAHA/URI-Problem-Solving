import math
a,b,c= input().split()
a = float(a)
b = float(b)
c = float(c)
try:
     q= (b**2)-(4*a*c)
     r1=(-b + (math.sqrt(q)))/(2*a)
     r2=(-b - (math.sqrt(q)))/(2*a)
except Exception as e:
    print("Impossivel calcular")


if a!=0 and  q>0:
    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)
