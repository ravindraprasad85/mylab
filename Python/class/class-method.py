#We are looking to use the class methods 
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name
        self.__class__.name = "Ram"  #Here is refering class vale

p1 = Person()
p1.changeName("rahul")
#print(p1.name)
print(Person.name) #Even if we are calling Person.name Its changing "Ram" by using class method