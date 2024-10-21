row1 = list(map(int ,input("Enter Values for List 1 : ").split()))

row2 = list(map(int , input("Enter Values for List 2 : ").split()))

i = 0 
j = 0 

ans = []
while( i < len(row1) and j < len(row2)):
    if(row1[i] < row2[j]):
        ans.append(row1[i])
        i = i+1
    else:
        ans.append(row2[j])
        j = j+1

while( i < len(row1) ):
    ans.append(row1[i])
    i = i+1 

while( j < len(row2) ):
    ans.append(row2[j])
    j = j+1 

print(ans)
