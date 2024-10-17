import random
def evolve(x):
    index = random.randint(0 , len(x)-1)
    p = random.randrange(0 , 10)
    if p == 0 : 
        if x[index] == '1' :
            x[index] = '0*' 
        else :
            x[index] = '1*' 
with open ("TheoryOfEvolution/DNA_DATA.txt" , "r") as myDNA :
    x = myDNA.read()
    x = list(x)
for i in range(0 , len(x)):
    evolve(x)

print(x)