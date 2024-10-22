n = int(input("Enter the number a : "))
m = int(input("Enter the number b : "))


def Multiplication(n , m):
    if(m == 0):
        return 1 
    
    return n * Multiplication(n , m-1)

print(Multiplication(n , m))