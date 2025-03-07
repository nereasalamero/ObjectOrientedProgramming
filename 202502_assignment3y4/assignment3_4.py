# **********************************************
# Title:        Asignments 3 & 4
# Author:       Nerea Salamero Labara
# Date:         29/01/2025
# File:         assignment3_4.py
# Subject:      Object Oriented Programming
# Description:  
# **********************************************

# Assignment 3:
# Write a function named list_all_years(dates: list) which takes a list of date type objects as its argument. The 
# function should return a new list, which containsthe years in the original list in chronological order, from 
# earliest to latest. An example of the function in action.
# from datetime import date
# 
# def list_all_years(dates: list):
#     years = []
#     for date_o in dates:
#         years.append(date_o.year)
#     return sorted(years)
# 
# # Test
# d1 = date(2018, 2, 1)
# d2 = date(2023, 10, 20)
# d3 = date(1998, 1, 7)
# 
# years = list_all_years([d1, d2, d3])
# print(years)



# Assignment 4:
# This ShoppingList class has methods for adding items, removing items, getting the count of unique items, getting 
# the total units, and displaying the current shopping list etc. Create a ShoppingList class which has several 
# methods item_count, add_item, unit_count etc. Here is partially created shopping list class. Fill the gaps.

class ShoppingList:
    def __init__(self):
        self.items = {}         # Dictionary to store items and their quantities

    # Get the item name by using the index value
    def item(self, i: int):
        if len(self.items) > i:
            return list(self.items.keys())[i]
    
    # Add an item to the shopping list
    def add_item(self, item: str, unit: int):
        if item in self.items:
            self.items[item] += unit
        else:
            self.items[item] = unit
    
    # Remove a specified quantity of an item from the shopping list
    def remove_item(self, item, quantity: int):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                self.items.pop(item)
    
    # Get the total count of unique items on the shopping list
    def item_count(self):
        return len(self.items)
    
    # Get the total count of all units (quantities) of items on the shopping list
    def unit_count(self):
        return sum(self.items.values())
    
    # Display the current shopping list
    def display_list(self):
        print("Shopping List:")
        for item, unit in self.items.items():
            print(f"- {item}: {unit}")

# Test
shopping_list = ShoppingList()
shopping_list.add_item('Apple', 3)
shopping_list.add_item('Banana', 2)
shopping_list.add_item('Orange', 4)
shopping_list.display_list()

print(f"Total unique items: {shopping_list.item_count()}")    # Output: 3
print(f"Total units: {shopping_list.unit_count()}")    # Output: 9

shopping_list.remove_item('Banana', 1)
shopping_list.display_list()

# Display one item (Banana) by using the index
print(shopping_list.item(1))    # Output: Banana