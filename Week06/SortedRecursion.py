row = list(map(int , input("Enter the numbers with spaces : ").split()))
# print(row)
def sortedOrNot(row ,i):
    if(i == len(row)):
        return True
    if(row[i] > row[i+1]):
        return False
    
    return sortedOrNot(row , i+1)

def NonDecreasing(row):
    if(len(row) <= 1):
        return True 
    # return row[]
print(sortedOrNot(row , 0))