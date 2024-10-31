str = input("Enter the String : ")
print("LowerCase :" , str.lower() , "Upper Case :" , str.upper())

sList = list(str)
print(sList)

print(str.replace("o" , "#"))
print(str.replace("oOjas" , "&"))
print(str.replace("jas" , "&*"))

# this is called slicing
print(str[1:4])
# this removes the last character
print(str[:-1])
print(sList[:8])
print(str[:9])
print(str[:])

# print(str.index("O"))
# print(str.index("jas"))

# remove the spaces from the sentences 
print(str.replace(" " , ""))