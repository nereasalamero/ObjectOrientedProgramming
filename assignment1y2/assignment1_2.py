# **********************************************
# Title:        Asignments 1 & 2
# Author:       Nerea Salamero Labara
# Date:         22/01/2025
# File:         assignment1_2.py
# Subject:      Object Oriented Programming
# Description:  
# **********************************************


# Create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing elements
print(my_dict['name'])      # Output: John
print(my_dict['age'])       # Output: 30

# Modifying values
my_dict['age'] = 26
print(my_dict['age'])    # Output: 26

# Adding key-value pairs
my_dict['occupation'] = 'Engineer'
print(my_dict)          # Output: {'name': 'John', 'age': 26, 'city': 'New York', 'occupation': 'Engineer'}

# Deleting key-value pairs
del my_dict['city']
print(my_dict)          # Output: {'name': 'John', 'age': 26, 'occupation': 'Engineer'}

# Checking if a key exists
print('name' in my_dict)    # Output: True
print('gender' in my_dict)    # Output: False

# Getting a list of keys and values
keys = my_dict.keys()
values = my_dict.values()
print(keys)     # Output: dict_keys(['name', 'age', 'occupation'])
print(values)   # Output: dict_values(['John', 26, 'Engineer'])



# Assignment 1: Find the Smallest Value

# Objective: Write a Python function named smallest_value that takes three dictionary objects as its arguments.
# Instructions:
#   1. Function Declaration: Declare a function named smallest_value with the following signature:
#   2. Dictionary Structure: Each dictionary (person_1, person_2, person_3) represents a person's data and contains
#      keys for different attributes (e.g., 'age', 'height', 'weight'). Assume each dictionary has the same set of keys.
#   3. Find the Smallest Value: In the function, compare the values of a specific attribute (e.g., 'age') from all three dictionaries.
#      Identify the person with the smallest value for that attribute.
#   4. Return Result: Return a tuple containing the person's name and the corresponding attribute value.
#   5. Example: calling smallest_value({'name':'Alice','age':25,'height':160}, {'name':'Bob','age':30,'height':175}, 
#               {'name':'Charlie','age':22,'height':155}) might return ('Charlie',22) if we are comparing the 'age' attribute.

def smallest_value(person_1: dict, person_2: dict, person_3: dict):
    min_value = min(person_1['age'], person_2['age'], person_3['age'])
    if min_value == person_1['age']:
        return (person_1['name'], person_1['age'])
    elif min_value == person_2['age']:
        return (person_2['name'], person_2['age'])
    else:
        return (person_3['name'], person_3['age'])

print(smallest_value({'name': 'Alice', 'age': 25, 'height': 160}, {'name': 'Bob', 'age': 30, 'height': 175}, {'name': 'Charlie', 'age': 22, 'height': 155}))



# Assignment 2: Calculate Row Sums
# Write a function named calculate_row_sums(my_matrix: list), where you give an integer matrix as its argument.
# The function adds a new element on each row in the matrix. This element contains the sum of the other elements on that row.
# 
# Example: 
#   matrix = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
# Result:
#             [1, 2, 3, 6]
#             [4, 5, 6, 15]
#             [7, 8, 9, 24]

def calculate_row_sums(my_matrix: list):
    for i in range(len(my_matrix)):
        my_matrix[i].append(sum(my_matrix[i]))
    return my_matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(calculate_row_sums(matrix))


