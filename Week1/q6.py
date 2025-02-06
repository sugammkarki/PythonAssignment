word = input (" Enter the word : ")

if len(word) > 1:
    swap = word[-1] + word [1:-1] + word [0]


else:
    swap = word
print ("Original Word : ", word)
print ( " Swapped Word: " , swap)
