#Methods are functions which belongs to a class

######Class attribute##########

class Student:
    college_name = "GIC Khatima"
    name = "anonymous"
    def __init__(self, name, age, city, marks):
        self.name = name
        self.age = age
        self.city = city
        self.marks = marks

    def welcome(self):
        print("Welcome..!!", self.name)

    def get_marks(self):
        print("Got marks", self.marks)

s1 = Student("Ramesh", 21, "Delhi", 105)

s1.welcome()
s1.get_marks()