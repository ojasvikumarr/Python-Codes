str1 = input("Enter the first String : ")
str2 = input("Enter the second String : ")

print(sorted(str1))
print(sorted(str2))

if(sorted(str1) == sorted(str2)):
    print("They are Anagrams!")
else :
    print("they are not Anagrams!")