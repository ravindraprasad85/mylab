#Static methods don't use the self paramater, that work at class level
#####Creating class for several students with three subject marks and its average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod  #Decorator
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,", self.name, "Your average score is", sum/3)




s1 = Student("Ram", [40, 50, 60])
s2 = Student("Ravindra", [80, 70, 90])

s1.get_avg()
s2.name = "Suresh"
s2.get_avg()
s1.hello()
