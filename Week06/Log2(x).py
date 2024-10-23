x = int(input("Enter the number whose Log with base 2 you want : "))

def log2(x):
    if(x == 1):
        return 0 
    
    return 1 + log2(x//2)

print(log2(x))