sentence = input("Enter the sentence: ")
words = 0
totalLetters = 0

for i in range(len(sentence)):
    if sentence[i] != " ":
        totalLetters += 1  # Count letters if not a space
    if (i == len(sentence) - 1 or sentence[i+1] == " ") and sentence[i] != " ":
        words += 1  # Count words when reaching a space or end of sentence

if words > 0:
    average = totalLetters // words
    if average > 4:
        print(1)
    else:
        print(0)
else:
    print("No words found.")