N=int(input("ENTER A NATURAL NO: "))

for I in (2,N):
    if N%I==0:
        print("IT IS NOT A PRIME NO")
        break
    else:
        print("IT IS A PRIME NO") 
        break   