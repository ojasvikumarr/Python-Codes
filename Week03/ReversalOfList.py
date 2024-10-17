input_numbers = input("Please eneter a list with spaced numbers : ")

list = input_numbers.split()
for i in range(len(list)):
    list[i] = int(list[i])

reversed_list = list[::-1]

# for i in range(len(list)):
#     reversed_list[len(list)-i-1] = list[i]

# for num in reversed_list : 
#     print(num, end=" ")

new_list = list 

for i in range(len(reversed_list)):
    if(i % 2 != 0):
        new_list[i] = reversed_list[i] + new_list[i]

for num in new_list : 
    print(num, end=" ")