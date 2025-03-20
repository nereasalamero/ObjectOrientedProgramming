# Object Oriented Programming
**Author:** `Salamero Labara, Nerea`<br>
**Date:** `Spring semester (January-May) 2025` <br>
**Summary:** This repository contains the small projects I developed in Mobile Technology And Programming, a subject I did while I was studying as an exchange student at Savonia UAS.

## Theory
**Lecture 1.**  Objects and Methods <br>
**Lecture 2.**  Classes and Objects <br>
**Lecture 3.**  Class Definition <br>
**Lecture 4.**  Objects and references <br>
**Lecture 5.**  Objects as attributes <br>
**Lecture 6.**  Inheritance <br>
**Lecture 7.**  Inheritance continues <br>
**Lecture 8.**  Comprehension exceptions <br>
**Lecture 9.**  Threading <br>
**Lecture 10.** Pygame <br>
**Lecture 11.** Exercises <br>
**Lecture 12.**  <br>
**Lecture 13.**  <br>
**Lecture 14.**  <br>

## Exercises
### Assignment 1
Write a function smallest_value() that finds the smallest value in three dictionaries objects as its arguments.

### Assignment 2
Write a function calculate_row_sums() that adds a new element to each row in a matrix containing the sum of the row elements.

### Assignment 3
Write a function list_all_years(dates: list) which takes a list of date type objects as its argument. The function should return a new list that contains the years in the original list in chronological order, from the earliest to the latest.

### Assignment 4
Implement a ShoppingList class with methods to add items, remove items, get the count of unique items, get the total units, display the current shopping list, etc.

### Assignment 5
Implement a Stopwatch class with private attributes and methods like start(), stop(), reset(), and elapsed_time(). Define all the attributes as private.

### Assignment 6. Secret Society with Artifacts

**Create a class named Artifact with the following attributes:**
- name (string): the name of the artifact.
- power (string): the power or ability associated with the artifact.

**Implement methods within the Artifact class:**
- __init__(self, name, power): A constructor method that initializes the name and power of the artifact.

**Create a class named Member with the following attributes:**
- secret_identity (string): a unique identifier for the member.
- name (string): the public name of the member.
- access_level (string): the level of access the member has within the society.
- artifacts (list): a list to store instances of the Artifact class representing artifacts owned by the member.

**Implement methods within the Member class:**
- __init__(self, secret_identity, name, access_level): A constructor method that initializes the secret_identity, name, and access_level of the member.
- add_artifact(self, artifact): A method that takes an Artifact object as an argument and adds it to the member's list of artifacts.

**Create a class named Society with the following attributes:**
- society_name (string): the name of the secret society.
- members (list): a list to store instances of the Member class representing society members.

**Implement methods within the Society class:**
- __init__(self, society_name): A constructor method that initializes the society_name and an empty list for members.
- add_member(self, member): A method that takes a Member object as an argument and adds the member to the society.
- remove_member(self, member): A method that takes a Member object as an argument and removes the member from the society.
- print_society_info(self): A method that prints information about the society, including the society name, a list of members, and their associated artifacts.


### Assignment 7