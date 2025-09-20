#Private attribute and Methods
#Private attribute and methods are meant to be used only within the class and are not accessible from outside the class.
# 
class Account:
    def __init__(self, acc_no, password):
        self.acc_no = acc_no
        self.password = password

    def hello(self):
        print("Hello Person..")

    def password(self):
        self.hello()

acc1 = Account(12345, "abcde")

print(acc1.acc_no)
print(acc1.password)

acc1.password()

###########################
class Person:

    def __hello(self):
        print("Hello Person!..")

    def welcome(self):
        self.__hello()
  
p1 = Person()
#print(p1.__hello()) #This will not work as its calling private method
p1.welcome()
