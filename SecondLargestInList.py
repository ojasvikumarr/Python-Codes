input_list = input("Please enter the required list : ")
list = input_list.split()

for i in range(len(list)):
    list[i] = int(list[i])
    
firstLargest = -1 
secoLargest = -1 

for num in list:
    if(num > firstLargest):
        secoLargest = firstLargest
        firstLargest = num 
    elif(num > secoLargest and num != firstLargest):
        secoLargest = num 

print(secoLargest)
