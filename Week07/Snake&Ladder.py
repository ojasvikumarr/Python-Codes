ladder = list(map(int , input().split()))
snakes = list(map(int , input().split()))
currPosi = int(input())
dieRoll  = int(input())

newPosi = currPosi + dieRoll 

def check(newPosi):
    if(newPosi in ladder):
        print(1)
    elif(newPosi in snakes):
        print(-1)
    else:
        print(0)

check(newPosi)