#FREQUENCY OF STRINGS

l = True
while l == True: 
    my_string = str(input("Enter a string: "))
  
    freq = {}
  
    for i in my_string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
  
    print ("Count of all characters in", my_string, "is :","\n " +  str(freq))
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

#REPLACE CHARACTER BY ANOTHER IN STRING

string = str(input("Enter a string: "))
new_string = string.replace(input("Enter the character to replace: "), input("Enter the character to replace with: ") )
print("Original String: ",string)
print("New String: ",new_string)

#REMOVE 1ST OCCURENCE

str1 = str(input("Enter a sentence: "))
result = ""
ch_to_remove = str(input("input a char: "))
occurred_flag = False
for ch in str1:
    if ch == ch_to_remove and occurred_flag == False:
        occurred_flag = True
        continue
    else:
        result += ch
print(result)

#REMOVE ALL OCCURENCES

str1 = str(input("Enter a sentence: "))
result = ""
ch_to_remove = str(input("input a char: "))
for ch in str1:
    occurred_flag = False
    if ch == ch_to_remove and occurred_flag == False:
        occurred_flag = True
        continue
    else:
        result += ch
print(result)