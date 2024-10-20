n = int(input())
m = int(input())
matrix = []
for _ in range(n):
    # list = input()
    # list = list.split()
    # list = [int(i) for i in list]
    row = list(map(int , input().split()))
    matrix.append(row)

def findSaddlePoint(matrix , n , m):
    isSaddlePoint = True
    for i in range(n):
        # find the mini element 
        mini = min(matrix[i])
        mini_col_idx = matrix[i].index(mini)
        for j in range(n):
            if(matrix[j][mini_col_idx] > mini):
                isSaddlePoint = False
                break 
        if(isSaddlePoint == True):
            print("1")
            break
    print("0")

findSaddlePoint(matrix , n , m)