for number in range(0 , 51):
    if number % 5 == 0 and number % 3 == 0 :
        print(number ,"FizzBuzz")
        continue
    else :
        if number % 3 == 0 :
            print(number , "Fizz")
            continue
        
        if number % 5 == 0 : 
            print(number , "Buzz")
            continue
    print(number)