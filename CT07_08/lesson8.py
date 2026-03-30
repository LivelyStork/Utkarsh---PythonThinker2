print("Hello from lesson 8")
student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# Task​

# Given a list of student index numbers (with duplicates), create a cleaned list where each
# student appears once.​

# Sort the cleaned list in ascending order.​

# Print the final list and also print how many duplicates were removed.​

# Print the count of how many students attended the Math Enrichment Class.

# uni_list = []
# no_dupli = 0

# for stu in student_indexes:
#     if stu not in uni_list:
#         uni_list.append(stu)
#     else:
#         no_dupli += 1

# print(sorted(uni_list))
# print("The number of duplicates are " + str(no_dupli))
# print(str(len(uni_list)) + " students are attending Math Enrichment. ")

# Task 1a​
# Ask the user to input their first name until it is a valid name. ​
# A valid name only contains alphabets.​
# Keep asking for a name until a valid name is input.​
# Task 1b​
# Ask the user to input their age until it is a valid number. ​
# Keep asking for a name until a valid number is input.​
# Task 1c​
# Ask the user to input a valid username. A valid username must contain
# alphabets and numbers, but not contain special characters​

# first_name = ""
# age = ""
# valid_username = ""
# while not first_name.isalpha():
#     first_name = input("What is your name? ")
# while not age.isdigit():
#     age = input("What is your age? ")
# # while not username.isalpha and username.isdigit():
# #     username = input("What is your username? ")
# while True:
#     valid_username = input("What is the username? ")
#     if valid_username.isalpha() or valid_username.isdigits():
#         print("Username must contain numbers AND letters. ")
#     if valid_username.isalnum() and not valid_username.isalpha() and not valid_username.isdigit():
#         break
# print(valid_username)

# Task 2a​
# Ask the user to input their phone number until it is valid using
# a while loop.​
# Make sure to check if the input is the correct data type as well!​

# Task 2b​
# Ask the user to a username and check if it is between 5 to 18
# characters long.​

# phone_no = input("What is your phone number? ")
# while not len(phone_no) == 8 or not phone_no.isdigit():
#     phone_no = input("What is your phone number? ")

# username = input("What is your username? ")
# while not 5 <= len(username) <= 18 or not username.isalpha():
#     username = input("What is your username? ")
# # Lesson 8 - Input Validation

# ## Recap 1: List Manipulation
# You have a list of student index numbers who attended the Math Enrichment class. 
# However, some students’ attendance were recorded more than once due to a human error.
# Your task is to clean the list and produce a list of unique Student Indexes

# Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# Sort the cleaned list in ascending order.
# - Print the final list and also print how many duplicates were removed.
# - Print the count of how many students attended the Math Enrichment Class.

# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]

# ## Task 1: Data Format Check

# ### Task 1a
# Ask the user to input their first name until it is a valid name. 
# A valid name only contains alphabets.
# Keep asking for a name until a valid name is input.

# ### Task 1b
# Ask the user to input their age until it is a valid number. 
# Keep asking for a name until a valid number is input.

# ### Task 1c
# Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

# ## Task 2: Length Check (using a while loop)

# ### Task 2a
# Ask the user to input their phone number until it is valid using a while loop.
# Make sure to check if the input is the correct data type as well!

# ### Task 2b
# Ask the user to a username and check if it is between 5 to 18 characters long.

# ## Task 3: Range Check (using a while loop)

# ### Task 3a
# Ask the user to input their birth year and check if it is between 1900 and the current year.
#  Keep asking until a correct value is given.
# while True:
#     year = input("What is your birth year? ")
#     if int(year) >= 1900 and int(year) <= 2026:
#         print(year + " is valid. ")
#         break
#     else:
#         print("That is invalid. ")
# ### Task 3b
# Ask the user to input their volume setting and check if it is between 0 and 100.
# while True:
#     volume = input("What is your volume setting? ")
#     if int(volume) >= 0 and int(volume) <= 100:
#         print(volume + " is valid. ")
#         break
#     else:
#         print("That is invalid. ")

# ## Task 4: Mocking Text Generator
# Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
# For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

# 1. Using input(), ask the user for a sentence
# 2. Use loops to iterate through each letter in the sentence
# 3. Alternate between .upper() and .lower() for each letter
# 4. Print the result.

# sentence = input("What is your sentence? ")
# new_sentence = ""
# is_upper = True
# for char in sentence:
#     if char.isalpha():
#         if is_upper:
#             new_sentence += char.upper()
#         else:
#             new_sentence += char.lower()
#         is_upper = not is_upper
#     else:
#         new_sentence += char
# print(new_sentence)


# ## Task 5: Slice String
# word = “SINGAPORE”

# Slice the string and print these words:
# a. SING
# b. GAP
# c. PORE
# d. SNAOE

# word = "singapore"
# print(word[:4])
# word = "singapore"
# print(word[3:6])
# word = "singapore"
# print(word[5:])
# word = "singapore"
# print(word[::2])

# ## Task 6: Palindrome
# Ask the user for an input and check if it is a palindrome, until the input is ‘end’.

# while True:
#     pal = input("Enter your word and see if it is a palindrome! ")
#     if pal == "end":
#         break
#     if pal[::-1] == pal[:]:
#         print("Your word is a palindrome!")
#     else:
#         print("Your word is not a palindrome. ")

# You can try this list of words:
# - civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow

# ## Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# bday = ["Alice", "Bob", "Carl", "Dylan"]
# while True:
#     name = input("What is your name? ")
#     if name == " ":
#         print("Please enter your name")
#     if name in bday:
#         print("Access approved. Welcome! ")
#         break
#     else:
#         print("Access denied. ")
#         break

# Create a list with your friends’ names
# - e.g. [“Alice”, “Bob”, Carl”, “Dylan”]

# Write a program to ask for the visitor’s name and check if:
# - Name is entered (presence check)
# - Name is in your friend list (existence check)

# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.

# ## Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long

# ## Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.
is_8char_long = False
is_upper_case = False
is_lower_case = False
is_num = False
is_alnum = False

while True:
    password = input("password?: ").strip()

    if password == "":
        print("Password cannot be empty or blank. ")
        continue
    if len(password) >= 8:
        is_8char_long = True
    for char in password:
        if char.isupper():
            is_upper_case = True
            continue
        if char.islower():
            is_lower_case = True
            continue
        if char.isdigit():
            is_num = True
            continue
        if char.isalnum():
            is_alnum = True
            continue
    if is_8char_long and is_upper_case and is_lower_case and is_num and is_alnum:
        print("Your password is " + str(password) + ". Have a good day! ")
        break
    

# Write a program that will ask the user for a password, and check if the password fits all criteria

# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me

# first_letter = ["S", "T", "F", "G", "M"]
# is_first_last_char_upper = False
# is_first_letter_in_list = False
# is_7digit_between_alphabet = False

# while True:
#     nric = input("NRIC? ").strip()

#     if nric == "":
#         print("NRIC cannot be empty or blank. ")
    
#     if len(nric) == 9:
#         is_9char_long = True
#     else:
#         print("NRIC must be 9 characters long. ")

#     if nric[0].isupper() and nric[-1].isupper():
#         is_first_last_char_upper = True
#     else:
#         print("First and last character are alphabets in upper case. ")

#     if nric[0] in first_letter:
#         is_first_letter_in_list = True
#     else:
#         print("First letter must be S, T, F, G, or M. ")

#     if nric[1:8].isdigit():
#         is_7digit_between_alphabet = True
#     else:
#         print("Need to have 7 digits between the alphabets. ")

#     if first_letter and is_first_last_char_upper and is_first_letter_in_list and is_7digit_between_alphabet:
#         print("Your NRIC number is " + str(nric) + ". Have a good day! ")
#         break