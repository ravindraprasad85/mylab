# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     def calcPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage)


# stu1.math = 60
# stu1.calcPercentage()
# print(stu1.percentage)


###############Property Decorator 
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem 
        self.math = math

    @property
    def percentage(self):
        return  str((self.phy + self.chem + self.math) / 3) + "%"
    
stu1 = Student(98, 99, 97)
stu1.math = 70
print(stu1.percentage)