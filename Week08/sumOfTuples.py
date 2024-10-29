n = int(input())
grid = []
for _ in range(n):
    my_tuple = tuple(map(int , input().split()))
    grid.append(my_tuple)

sum = 0 

for i in range(n):
    sum += grid[i][0]

print(sum)