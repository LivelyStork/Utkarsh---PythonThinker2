# print("Hello from lesson 2")
## Task 1: Introduction to while loop
# **Task: Using a separate 'while' loop, print each of the
# following:**
# 1. from 0 to 20
# 2. from 1 to 30
# 3. from 2 to 24
# i = 0
# while i<21:
#     print(i)
#     i += 1

# i = 1
# while i<31:
#     print(i)
#     i += 1

# i = 2
# while i<25:
#     print(i)
#     i += 1

# print 50 to 25
 
# print 100 to 86 only even number

# i = 50
# while i>24:
#     print(i)
#     i -= 1

# i = 100
# while i>85:
#     print(i)
#     i -= 2

# print only those that are multiple of 3, 4, 5 from 100 to 25 in a while loop

# i = 100
# while i>24:
#     if i%3 == 0: 
#         print(i)
#     elif i%4 == 0:
#         print(i)
#     elif i%5 == 0:
#         print(i)
#     i -= 1

# print only those that are prime number from 200 to 100 in a while loop

# ## Task 2: while... break
# The **break** keyword will **break** out (exit) the loop.
# When a **break** is encountered, the code in the **else** will
# not be run.
# Using a while loop:
# 1. print the numbers from 1 to 10
# 2. if the number is 5, **break** out of the loop

# i = 1
# while True:
#     print(i)
#     i += 1
#     if i == 5: 
#         break


## Task 3: while... else
# The else condition will run when the loop exits normally
# i.e. when the while condition is no longer true.

# **Task 3a**: Using a while loop
# 1. print the numbers from 1 to 10
# 2. once count has reached 10, use the else and print "Count
#    has reached 10"

# **Task 3b**:
# Now, modify your 'while' loop such that:
# 1. If the number is 5, **break** out of the loop
# 2. Ensure your code has an else

# Observe if the code in the **else** runs.

# i=1
# while i<11:
#     print(i)
#     i += 1
# else:
#     print("Count has reached 10")

# i=1
# while i<11:
#     print(i)
#     i += 1
#     if i == 5:
#         break
# else:
#     print("Count has reached 10")

# ## Task 4: Ordering Pizzas with while loop
# **Task: Using what you have learned above, code a program to
# take a customer's order for pizza.
# Declare a variable called _topping_.**

# Using a while loop:
# 1. Ask the user to enter a choice of topping
# 2. For each topping entered, concatenate to the 'topping'
#    variable
# 3. exit the while loop if the user enters "end"
# 4. On program end, print out the toppings that the customer
#    has chosen.
# 
# pizza_topping = input("What topping would you want? ")
# topping = " "
# while pizza_topping != "end":
#     topping += pizza_topping + ", "
#     pizza_topping = input("What topping would you want? ")
# else:
#     print("These are all the toppings you ordered: " + topping)

## Task 5: General Knowledge Quiz
# **Task: Create a program to quiz users on their general
# knowledge**

# Using the while loop, ask 3 general knowledge questions
# 1. Using input ask the question
# 2. While answer is not correct, repeat the question.
# 3. Move on to the next question when the answer is correct

# Bonus:
# 1. Add a score system
# 2. Add an ability for users to skip by saying “skip”
# 3. Disqualify user when they have tried too many times
ans1 = 8
ans2 = 5
ans3 = 7
# guess1 = input("How many billion people are there in the world? ")
# while guess1 != ans1:
#     print("That's not right. Try again!")
#     guess1 = input("How many billion people are there in the world? ")

# else:
#     print("Good job! On to the next question!")

# guess2 = input("How many oceans are there in the world? ")
# while guess2 != str(ans2):
#     print("That's not right. Try again!")
#     guess2 = input("How many oceans are there in the world? ")

# else:
#     print("Good job! On to the next question!")

# guess3 = input("How many continents are there in the world? ")
# while guess3 != str(ans3):
#     print("That's not right. Try again!")
#     guess3 = input("How many continents are there in the world? ")

# else:
#     print("Good job! You completed the quiz!")
while True:
    guess1 = input("How many billion people are there in the world? ")

    if guess1 == str(ans1):
        print("Good job! On to the next question!")
        break
    print("That's not right. Try again!")

while True:
    guess2 = input("How many oceans are there in the world? ")
    
    if guess2 == str(ans2):
        print("Good job! On to the next question!")
        break
    print("That's not right. Try again!")

while True:
    guess3 = input("How many continents are there in the world? ")
    
    if guess3 == str(ans3):
        print("Good job! You completed the quiz!")
        break
    print("That's not right. Try again!")