import math
A=float(input("ENTER VALUE OF A: "))
B=float(input("ENTER VALUE OF B: "))
C=float(input("ENTER VALUE OF C: "))
D=B*B-4*A*C

if D==0:
    print("EQUAL ROOTS")
    print(-B + math.sqrt(D)/2*A)
    print(-B - math.sqrt(D)/2*A)
elif D>0:
    print("UNEQUAL ROOTS")
    print(-B + math.sqrt(D)/2*A)
    print(-B - math.sqrt(D)/2*A)
else:
    print("NO REAL ROOTS")    

