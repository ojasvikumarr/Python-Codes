array = list(map(int , input().split()))
counter = 0

def sorting(array):
    for i in range(len(array)):
        for j in range (i+1 , len(array)):
            if(array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    print(array)

# sorting(array)
def sortingReal(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp 
                counter += 1
    print(arr)
    print(counter)

sortingReal(array)