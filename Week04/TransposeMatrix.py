n = int(input())
m = int(input())
matrix = []
for _ in range(n):
    row = list( map(int, input().split()))
    matrix.append(row)
sV = int(input())
def findTransposeMatrix(matrix , n , m , sV):
    transpose = []
    for j in range(m):
        list = []
        for i in range(n):
            list.append(sV*matrix[i][j])
        transpose.append(list)
    
    print(transpose)

def PrintfindTransposeMatrix(matrix , n , m , sV):
    transpose = []
    for j in range(m):
        list = []
        for i in range(n):
            print(sV*matrix[i][j], end=" ")
        print("")
    
    # print(transpose)

PrintfindTransposeMatrix(matrix , n , m , sV)