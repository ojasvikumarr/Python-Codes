def non_decreasing(list):
    if(len(list) <= 1):
        return True
    return list[0] <= list[1] and non_decreasing(list[1:])

L = list(map(int , input("Enter the number with spaces : ").split()))

print(non_decreasing(L))