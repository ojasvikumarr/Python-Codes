import string 
dict = {}
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i-1]

file = open("Week06/CipheredText.txt" , "w")
with open("Week06/TobeCiphered.txt" , "r") as myFile :
    while True :
        
        x = myFile.read(1)
        if not x : 
            print("End of File")
            break
        if x in dict :
            data = dict[x]
        else :
            data = x 
        file.write(data)
        print(data)

file.close()
# print(dict)