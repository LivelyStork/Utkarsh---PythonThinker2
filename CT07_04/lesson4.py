# print("Hello from lesson 4")

# ## Task 1: List of planets
# **Task: Create a list of 8 planets in the solar system**

# **Task 1a**:
# Create a list of 8 planets in the solar system.
# (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

# **Task 1b**:
# You have conquered Mars, **rename** Mars to a name of
# your liking

# **Task 1c**:
# 1. You have decided Pluto is a planet again, **add** Pluto
#    into the list
# 2. You created an artificial planet between Earth and
#    Mars called "Lalaland". **Insert** the planet in
#    correctly into the list.

# **Task 1d**:
# You launched a war againts Jupiter and destroyed it,
# **delete** Jupiter from the list

# ---------------------------------------------------------------

# ## Task 2: List of planets (part 2)
# Tasks:

# 1. Write a for loop and print out all the names of the
#    planets
# 2. If name == "Earth", print "<planet name> : this is
#    my home"
# 3. If name == "Mars" (or changed name), print
#    "<planet name> : I conquered this"
# 4. If name == "Lalaland", print
#    "<planet name> : I created this"

# ---------------------------------------------------------------

# ## Task 3: Flight Round the Globe
# Task: Write a program to keep track of the countries you
# are visiting.

# 1. Use a while loop to ask the user what country they
#    would like to visit.
# 2. Add the country into a list
# 3. If the user types "end", exit the loop
# 4. Print all the countries in the list in this format.
#    "I would like to visit Germany"
#    "I would like to visit Japan"
#    ... 

# ---------------------------------------------------------------

# ## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."

# planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# planet[3] = "Earth 2.0"
# planet.append("Pluto")
# planet.insert(3, "Lalaland")
# planet.pop(5)
# # print(planet)

# for planet_var in planet:
#     if planet_var == "Earth":
#         print(planet_var + ": This is my home")
    
#     elif planet_var == "Earth 2.0":
#         print(planet_var + ": I conquered this")
    
#     elif planet_var == "Lalaland":
#         print(planet_var + ": I created this")
#     else:
#         print(planet_var)

# countries = []
# visit = input("What country would you like to visit? ")
# countries.append(visit)
# while visit != "end":
#     visit = input("What is another country you would like to visit? ")
#     # if visit != "end":
#     countries.append(visit)
    
#     # if visit == "end":
#     #     countries.pop
#     #     for places in countries:
#     #         print("I would like to visit " + places)
#     #     break

# countries.pop()
# # print(countries)
# for places in countries:
#     print("I would like to visit " + places)



## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

menu = []
item = input("What dish would you like to add to the menu? (Type 'end' if you are done) ")
# if item != "end":
while item != "end":
    menu.append(item)
    item = input("What dish would you like to add to the menu? (Type 'end' if you are done) ")
    # if item != "end":

# menu.pop()
print("This is your menu: ")
print(menu)
# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."
# in
hungry = input("What do you want to eat? ")
while hungry != "I will go next door":
    if hungry in menu:
        print("Yes, we sell that here. Please have a seat! ")
        break
    else:
        print("No we don't sell that here. Sorry, please go next door. Bye! ")
    hungry = input("What do you want to eat? ")


#keep asking the customer until they said they will go next door