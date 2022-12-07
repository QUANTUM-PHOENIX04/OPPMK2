N=int(input("ENTER A NATURAL NO: "))

for I in range(2,N):
    if N%I==0:
        print("IT IS NOT A PRIME NO")
        break
    else:
        print("IT IS A PRIME NO") 
        break 


while True:
    for I in range(2,N):
      for J in range(2,I):
        if I%J==0:
           break
        else:
           print(I)
           break
    break     