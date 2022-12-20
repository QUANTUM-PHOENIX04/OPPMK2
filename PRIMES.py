
N=int(input("ENTER A NATURAL NO: "))

for I in range(2,N):
    if N%I==0:
        print("IT IS NOT A PRIME NO")
        break
    else:
        print("IT IS A PRIME NO") 
        break 


 
print("PRIME NOS TILL ",N," ARE: ") 
l = True
while l == True:
    for i in range(2, N + 1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
    break  


print("FIRST ",N," PRIME NOS ARE :")
l = True
while l == True: 
    h = int(2)
    while N != 0:
        for E in range(2, h):
            if h % E == 0:
                break
        else:
            print(h)
            N -= 1
        h += 1
    break    
