######Object attribute####
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city 

s1 = Student("ravindra", 40, "khatima")
print(s1.name)
print(s1.age)
print(s1.city)


#####Without Constructo###########
class Car:
    name = "maruti"
    color = "blue"
    city = "delhi"

c1 = Car()
print(c1.name)
print(c1.color)
print(c1.city)

######Class attribute##########

class Student:
    college_name = "GIC Khatima"
    name = "anonymous"
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city 

s1 = Student("Ramesh", 42, "Delhi")
print(s1.name)
print(s1.age)
print(s1.city)
print(s1.college_name)