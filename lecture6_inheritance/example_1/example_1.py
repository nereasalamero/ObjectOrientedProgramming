# Author:       Nerea Salamero Labara
# Date:         28/03/2025
# File:         example_1.py
# Description:  
from student import Student
from teacher import Teacher

def change_email(s: Student):
    s.email = s.email.replace(".com", ".fi")

def change_email2(t: Teacher):
    t.email = t.email.replace(".com", ".fi")

if __name__ == "__main__":
    t = Teacher("John Doe", "Imaginary address", "john.doe@b.com", 9999)
    s = Student("Student 1", "School", "1234@hotmail.com")

    print(s.name)
    print(s.email)

    print(t.name)
    print(t.email)

    change_email(s)
    change_email2(t)

    print(s.email)
    print(t.email)