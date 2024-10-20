array = list(map(int , input().split()))

def sorting(array):
    for i in range(len(array)):
        for j in range (i+1 , len(array)):
            if(array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    print(array)

sorting(array)