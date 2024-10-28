r = int(input("Enter number of rows : "))
c = int(input("ENter number of cols : "))
matrix = []
for _ in range(r):
    row = list(map(int , input().split()))
    matrix.append(row)


Sym = True 
Binary = True 
binary = [1 , 0]
for i in range(r):
    for j in range(i):
        if(matrix[i][j] != matrix[j][i]):
            Sym = False
        if(matrix[i][j] in binary and matrix[j][i] in binary):
            continue
        else:
            Binary = False

if(Sym == True and Binary == True):
    print("11")
elif(Sym == True and Binary == False):
    print("01")
elif(Sym == False and Binary == True):
    print("10")
else:
    print("00")