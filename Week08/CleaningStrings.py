str1 = input()
str2 = input()

def clean_Strings(str):
    return ' '.join(char.lower() for char in str if char.isalpha())

def checkAnagram(str1 , str2):
    cleaned_str1 = clean_Strings(str1)
    cleaned_str2 = clean_Strings(str2)
    return sorted(cleaned_str1) == sorted(cleaned_str2)

if(checkAnagram(str1 , str2)):
    print(1)
else : 
    print(0)