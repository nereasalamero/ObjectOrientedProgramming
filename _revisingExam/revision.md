## 🧠 Part 1: Multiple Choice Questions
1. Which of the following is not a key principle of object-oriented programming?<br>
    a) Encapsulation<br>
    b) Compilation<br>
    c) Inheritance<br>
    d) Polymorphism

2. What does the __str__ method in a class do?<br>
    a) Initializes a new object<br>
    b) Returns a string representation of the object<br>
    c) Converts an object to a dictionary<br>
    d) Saves the object to a file

3. What is true about Python’s @staticmethod?<br>
    a) It can access instance attributes<br>
    b) It takes self as its first argument<br>
    c) It takes cls as its first argument<br>
    d) It doesn't access instance or class-specific data<br>

4. Which statement about Python access modifiers is incorrect?<br>
    a) __attribute makes an attribute private.<br>
    b) _attribute makes an attribute protected.<br>
    c) Python enforces strict access control for private attributes.<br>
    d) Public attributes have no underscores.

5. What is the main difference between a class method and a static method?<br>
    a) Class methods require self, static methods require cls<br>
    b) Class methods are not accessible outside the class<br>
    c) Class methods take cls as their first argument<br>
    d) Static methods can only be called from instances

6. What does the __call__() method allow you to do with an object?<br>
    a) Compare it to another<br>
    b) Add it to a dictionary<br>
    c) Use it like a function<br>
    d) Override its constructor


## ✍️ Part 2: Short Answer Questions
1. Define the difference between aggregation and composition.

2. What are the differences between public, protected, and private attributes in Python?

3. What’s the purpose of super().__init__() in an inherited class?

4. What does the is operator check in Python?

5. Explain the difference between == and is in Python.

6. What is the benefit of using operator overloading in a class?

7. What is the purpose of __iter__() and __next__() in custom classes?

8. How can you ensure that resources (like files) are always released, even if an error occurs?

9. Describe the difference between composition and inheritance. When would you use one over the other?

10. Explain how dynamic methods are added to instances in Python.

11. What happens when you try to access a private attribute (__attribute) from a subclass?

12. What’s the purpose of using @classmethod for factory methods like copy_book()?

13. How does Python handle exception propagation if an exception isn’t caught in a function?



## 🧪 Part 3: Code-Based Questions
1. Write a Python class Student that inherits from a class Person, and adds a student_id attribute.

2. Write a function that receives three dictionaries and returns the smallest value from all of them.

3. Create a static method in a class MathOps that multiplies two numbers.

4. Create a Book class that can be sorted based on its price using operator overloading.

5. Write a comprehension that selects all Book objects from a list with price > 50 and returns their names.

6. Define a custom exception LowCreditError and raise it when a member’s credit is below 10.

7. What is the output of the following code?
    ```
        class A:
            def __init__(self, x):
                self.__x = x

            def get_x(self):
                return self.__x

        class B(A):
            def __init__(self, x, y):
                super().__init__(x)
                self.y = y

        a = A(5)
        b = B(10, 20)

        print(b.get_x())
        print(hasattr(b, '__x'))
    ```

8. What will this return and why?
    ```
        class Engine:
            def __init__(self, fuel_type):
                self.fuel_type = fuel_type

            def __eq__(self, other):
                return self.fuel_type == other.fuel_type

        e1 = Engine("gasoline")
        e2 = Engine("gasoline")

        print(e1 == e2)
        print(e1 is e2)
    ```

9. Design a class NotebookPro that inherits from Notebook and allows searching through notes. Use protected attributes.

10. Write a class Thesis that inherits from Book, overrides the summary() method, and adds a university attribute.

11. Write code that demonstrates how an object passed as an argument to a function can be modified within the function.

