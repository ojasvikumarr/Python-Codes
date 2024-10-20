arr = list(map(int , input().split()))
target = int(input())

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if(arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp 

def binarySearch(arr , target):
    left = 0 
    right = len(arr)-1
    bubble_sort(arr)
    print("Sorted array : " , arr)
    while( left < right ):
        mid = (left + right)//2 
        if(arr[mid] == target):
            print("Target found at index : " , mid)
            return 
        else :
            if(arr[mid] < target):
                left = mid+1 
            else:
                right = mid-1 ; 
    print("Didnt find the target in the array maybe its doesnt exists!!")

binarySearch(arr , target)