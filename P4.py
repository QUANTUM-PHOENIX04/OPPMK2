#CHARACTER TYPE

l = True
while l == True: 
    char = str(input("Enter a character: "))
    if len(char) != 1:
        print("Enter a single letter!")
    else:
        if ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
            print(char,"is a letter.")
        elif (char >='0' and char <= '9'):
            print(char, "is a number.")
        else:
            print(char, "is a symbol.")
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

#LOWERCASE/UPPERCASE
        
l = True
while l == True: 
    char = str(input("Enter a character: "))
    if len(char) != 1 or char.isdigit():
        print("Enter a single Letter!")
    elif char.isupper():
        print(char,"is uppercase.")
    else:
        print(char,"is lowercase.")
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

#NUMBER NAME IN TEXT

def num_2_word(char):
    if char == '0':
        print("Zero")
    elif char == '1':
        print("One")
    elif char == '2':
        print("Two")
    elif char == '3':
        print("Three")
    elif char == '4':
        print("Four")
    elif char == '5':
        print("Five")
    elif char == '6':
        print("Six")
    elif char == '7':
        print("Seven")
    elif char == '8':
        print("Eight")
    else:
        print("Nine")
l = True
while l == True: 
    char = input("Enter a character: ")
    if len(char) != 1 or char.isalpha():
        print("Enter a single number!")
    else:
        print(num_2_word(char), "\n")
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)