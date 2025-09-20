#Creating class and then create Object called instance 


# class Student:
#     name = "Ravindra"
#     Age = 41

# s1 = Student()
# s2 = Student()
# print(s1.name)
# print(s2.Age)



# class Car:
#     color = "Blue"
#     brand = "Baleno"
#     model = "BL25"
#     country = "India"

# col = Car()
# print(col.color)
# print(col.brand)
# print(col.model)
# print(col.country)





####Creating Class and Constructor along with Object (Instance)  reation
class Student:
    def __init__(self, fullname, age, city):
        self.name = fullname
        self.age =  age
        self.city = city
        print("Adding new student in database..")

s1 = Student("Ravindra", 21, "Khatima")
# s1 = Student(21)
# s1 = Student("Khatima")
print(s1.name)
print(s1.age)
print(s1.city)

s2 = Student("Shyam", 23, "Delhi")
print(s2.name)
print(s2.age)
print(s2.city)