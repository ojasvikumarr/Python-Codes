import random 

def choose():
    words = ["banana" , "Coffee" , "Mango" , "Apple" , "Orange"]
    pick = random.choice(words)
    return pick 

def printChoice():
    for i in range(10):
        print(jumbling(choose()))
def jumbling(word):
    jumbled = "".join(random.sample(word , len(word)))
    return jumbled 
# printChoice()

print(jumbling("abcdefg"))