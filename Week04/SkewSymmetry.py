n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

def checkSkewOrNot(matrix , n ):
    transpose = []

    for j in range(n):
        list = []
        for i in range(n):
            list.append(-matrix[i][j])
        transpose.append(list)
    
    if transpose == matrix :
        print('1')
    else :
        print("0")

checkSkewOrNot(matrix , n )
