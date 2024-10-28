str = input("Enter the palindrome : ")
def checkPalindrome(str , idx):
    if( idx >= len(str)//2):
        return True 
    return str[idx] == str[len(str)-1-idx] and checkPalindrome(str , idx + 1)

print(checkPalindrome(str , 0))