input_numbers = input()
list = input_numbers.split()
for i in range(len(list)):
    list[i] = int(list[i])
# Now i have list having integers of the input list
unique_numbers = []
for num in list:
    if num not in unique_numbers :
        unique_numbers.append(num)

for num in unique_numbers:
    print(num ,end = " ")