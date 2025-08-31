# a) TODO: Extend the class called 'Books' with the following specifications:
# - It should have attributes for 'title', 'author', and 'pages'
# - Use the `__init__` method to initialize the attributes
# - Include a method called 'display_info' that prints all the book's information
# - Add a method 'is_short' that returns True if the book has less than 100 pages, False otherwise

class Books:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def is_short(self):
        return self.pages < 100

    def is_long(self):
        return self.pages > 400

# b) TODO: Create your favorite book as an object to the class you just created. Check if it is a long book.

# b) Create your favorite book as an object
favorite_book = Books("Miami Punk", "Juan S. Guse", 640)
print("Is my favorite book long?", favorite_book.is_long())

# c) TODO: Create a class called 'Student' with the following specifications:
# - It should have attributes for 'name', 'age', and 'current_grade'
# - Add a method 'is_excellent' that returns True if the student's grade is lower than 2.0
# - Add a method 'student_grade' that returns the current grade with the following printed statement: 
# - If the grade is lower than 2.0: "The current grade of the student is: <grade>. This is a fantastic grade."
# - If the grade is higher than 2.0 but lower than 4.0: "The current grade of the student is: <grade>. This is still a fantastic grade.
# - If the grade is higher than 4.0: "The current grade of the student is: <grade>. This is a not so fantastic grade..."
class Student:
    def __init__(self, name, age, current_grade):
        self.name = name
        self.age = age
        self.current_grade = current_grade

    def is_excellent(self):
        return self.current_grade < 2.0

    def student_grade(self):
        if self.current_grade < 2.0:
            return f"The current grade of the student is: {self.current_grade}. This is a fantastic grade."
        elif 2.0 <= self.current_grade < 4.0:
            return f"The current grade of the student is: {self.current_grade}. This is still a fantastic grade."
        else:
            return f"The current grade of the student is: {self.current_grade}. This is a not so fantastic grade..."

# d) TODO: Create your yourself as an object to the class you just created. Check if you are excellent and print your grade.
myself = Student("Tobias", 30, 2.3)
print("Am I excellent?", myself.is_excellent())
print(myself.student_grade())