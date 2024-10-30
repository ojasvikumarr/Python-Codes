string = input("Enter the String : ")


vowels = ["a" , "e" , "i" , "o" , "u" ]
counter = 0 
for c in string : 
    if c in vowels :
        counter += 1 

print(counter)