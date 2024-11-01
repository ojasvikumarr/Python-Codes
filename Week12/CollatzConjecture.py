while(True):
    n = int(input("Enter the number : "))
    if (n < 1):
        break 
    counter = 0 
    while(n != 1):
        if n % 2 == 0 :
            n = n/2 
        else : 
            n = 3*n + 1 
        counter += 1
        print(int(n))

    print("The iterations were : " , counter)