class Car:
    @staticmethod
    def start():
        print("Car Started..!")

    @staticmethod
    def stop():
        print("Car Stopped..!")

class TototaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(TototaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start() #Its working even its not define in last two classes , its only in top class , Instance created for last class only 