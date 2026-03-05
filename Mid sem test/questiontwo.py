# ============================================================
# Q2. Food Order System
# ============================================================
# Write a PYTHON program that simulates a restaurant order
# system using list and while loop.

# Requirements:
# - Use a while loop
# - Ask: "What would you like to order?"
# - Store each order into a list
# - Stop when user enters "end"
# - After ending, print all orders in numbered format

# ============================================================
# """

# # ============================================================
# # Step 1: Initialize variables
# # ============================================================

foods = []
dish = input("What would you like to order? ")
number = 1

# # ============================================================
# # Step 2: Create a loop
# # ============================================================

while dish != "end":
    foods.append(dish)
    dish = input("What would you like to order? ")


# ============================================================
# Step 3: Print the final order summary
# ============================================================
# Print the final order in this format:
# You have ordered the following:
# 1. Item1
# 2. Item2
# 3. Item3
# ============================================================

for item in foods:
    print(str(number) + ". " + item)
    number += 1