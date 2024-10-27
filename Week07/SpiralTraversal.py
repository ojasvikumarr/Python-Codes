n = int(input("Enter the no. of rows in the matrix : "))
m = int(input("Enter the no. of cols in the matrix : "))

matrix = []
for _ in range(n):
    row = list(map(int , input().split()))
    matrix.append(row)

top = 0 
bottom = n-1 
left = 0 
right = m-1 
while(top <= bottom and left <= right):
    for i in range(left , right+1):
        print(matrix[top][i] , end=" ")
    top += 1 
    for i in range(top , bottom+1):
        print(matrix[i][right] , end=" ")
    right -= 1 
    if top <= bottom :
        for i in range(right , left-1 , -1):
            print(matrix[bottom][i] , end=" ")
    bottom -= 1 
    if left <= right :
        for i in range(bottom , top -1 , -1):
            print(matrix[i][left] , end= " ")
        left += 1
