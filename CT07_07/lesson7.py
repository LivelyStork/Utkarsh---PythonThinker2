print("Hello from lesson 7")

## Task 4: Splitting a List in Half
# You have been tasked to divide the basket of fruits into
# 2 equal halves. Given a list of even length, split it
# into 2 equal halves.

fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# 1. Find the midpoint of the list.
# 2. Split the list into 2 halves using slicing.
# 3. Print both halves.
# i = 0
# half = len(fruits) // 2
# x = half + 1
# print(half)
# while i <= half:
#     print(fruits[i])
#     i += 1

# while x <= len(fruits):
#     if x > len(fruits):
#         break
#     print(fruits[x])
#     x += 1

# first = fruits[:half]
# second = fruits[half:]
# print(first)
# print(second)

## Task 6: Merging Lists Unique Items
# You have been given 2 lists of fruits that contains duplicates.
# Your task is to merge the 2 lists into a new list that contain
# no duplicates.

# list1 = ["Apple", "Banana", "Cherry", "Cherry"]
# list2 = ["Cherry", "Durian", "Durian", "Figs"]

# 1. Create an empty list named 'unique'
# 2. Using 'for' loops, append unique elements into 'unique'
# 3. Print the unique elements

# unique = []
# for fruit1 in list1:
#     if fruit1 not in unique:
#         unique.append(fruit1)

# for fruit2 in list2:
#     if fruit2 not in unique:
#         unique.append(fruit2)

# print(unique)

# ---------------------------------------------------------------

# ## Task 7: Merging Lists with Conditions
# You have been given the index number of 2 groups of students.
# However, only students with even index number is allowed
# to come into the room. Create a Python script that will
# merge the 2 lists, including only the elements that are
# even from both.

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
# Create an empty list, ‘even’​

# Merge the lists using the ‘+’ operator into a list named ‘merged’​

# Using ‘for’ loops and ‘if’ condition, check if each item in the merged list is an
# even number and add them into the ‘even’ list​

# Print the even numbers
# even = []
# merged = []

# merged = list1 + list2

# for item in merged:
#     if item%2 == 0:
#         even.append(item)

# print(even)
# ## Task 8: Nested List Splitting
# You are given a nested list of 3 groups of students that
# are each seated in a pair. However, you want to unpack
# the nested lists in order to have a list of all students.

# nested_list = [[1, 2], [3, 4], [5, 6]]

# 1. Use a loop or list comprehension to flatten the list.
# 2. Print the flattened list.

# flat = []

# for sec in nested_list:
#     for stu in sec:
#         flat.append(stu)

# print(flat)

# ---------------------------------------------------------------

# ## Task 9: Partitioning a List into Smaller Lists
# You have been tasked to divide a class of 9 students
# into groups of 3.

# Given a list and a size, split the list into multiple
# sub-lists where each sub-list is of the given size.

students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3

# 1. Use a loop to create sub-lists of the specified size.
# 2. Print the sub-lists.
sub1 = students[:3]
sub2 = students[3:6]
sub3 = students[6:]
nested_list = []

students = sub1 + sub2 + sub3

print(sub1)
print(sub2)
print(sub3)

for i in range(0, len(students), size):
    nested_list.append[i:i+3]

print(nested_list)