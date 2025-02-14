#question 1
#numbers = [10, 12, 25, 30, 40, 45, 55, 60, 70, 15, 5, 22, 8]


#for num in numbers:
 #   if num > 50:
  #      break 
   # if num % 5 == 0:
    #    continue  
    #print(num)  


#question 2
# Taking password input from the user
#password = input("Enter your password: ")

# Checking password strength
#if len(password) < 6 or password.isalpha():
 #   print("Weak Password")
#elif len(password) >= 6 and password.isalnum():
 #   print("Moderate Password")
#elif len(password) >= 8 and any(char in "@#$%&" for char in password):
 #   print("Strong Password")
#else:
#    print("Moderate Password")  


#question 3
# Take a string input from the user
#sentence = input("Enter a sentence: ")

# Split the sentence into words
#words = sentence.split()

# Process each word, reversing every alternate word
#NewWords = [word[::-1] if i % 2 != 0 else word for i, word in enumerate(words)]

# Join the words back into a sentence
#NewSentence = " ".join(NewWords)

# Print the result
#print("Modified sentence:", NewSentence)


#QUESTION 4
# Taking input
#words = ["ram", "ram", "shyam", "hari", "hari", "ram"]


#WordCount = {}

# Counting
#for word in words:
 #   WordCount[word] = WordCount.get(word, 0) + 1

# Filtering
#duplicates = {word: count for word, count in WordCount.items() if count > 1}

# Print 
#print(duplicates)




#Question 5
# Creating Dictionary 
#books = {
 #   'Book_1': 9,
  #  'Book_2': 2,
   # 'Book_3': 3,
    #'Book_4': 2,  
    #'Book_5': 10
#}

# Print
#print(books)


#Question 6


# Dictionary 
#book_store = {
 #   'Titanic': 5,
  #  'Ben10': 6,
   # 'Comic': 10,
    #'Novel': 3,
    #'RandomBook': 7
#}

# Ask the user for the input
#book_choice = input("Enter the name of the book you want: ")

# Checking
#if book_choice in book_store:
    
    
 #   while True:
  #      try:
   #         quantity = int(input("Enter the number of copies you want to buy: "))
    #        break  # Exit loop if input is valid
     #   except ValueError:
      #      print("Invalid input! Please enter a number.")

    # Checking availability
    #stock = book_store[book_choice]
    
    #if quantity <= stock:
     #   print("It is available in our store")
    #else:
      #  print("Limited Available (Only", stock, "copies left)")

#else:
 #   print("It is not available in our store")


#question 7

# Taking a list 
#WordList = input("Enter words separated by spaces: ").split()

# Dictionary to store 
#WordCount = {}

# Counting the occurrences 
#for SingleWord in WordList:
    #LowerCaseWord = SingleWord.lower()  # Convert to lowercase 
    #if LowerCaseWord in WordCount:
   #     WordCount[LowerCaseWord] += 1
  #  else:
 #       WordCount[LowerCaseWord] = 1

# Print 
#print("Word Frequency:", WordCount)
