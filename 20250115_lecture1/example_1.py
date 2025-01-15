name = "Happy new year!"
author = "Author name"
year = 2025

tupple = (name, author, year)
print(name, author, year)
print(tupple[0])


# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements
print(my_tuple[0])      # Output: 1
print(my_tuple[3])      # Output: 'a'

#Slicing
print(my_tuple[1:4])    # Output: (2, 3, 'a')

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)         # Output: (1, 2, 3, 'a', 'b', 'c')

#Tuple with a mutable element (a list)
mutable_tuple = ([1, 2, 3], 'a', 'b')
mutable_tuple[0].append(4)
print(mutable_tuple)        # Output: ([1, 2, 3, 4], 'a', 'b')

