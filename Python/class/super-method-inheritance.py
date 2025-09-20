class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started..!")

    @staticmethod
    def stop():
        print("Car Stopped..!")


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)  #Using parent method using super()
        super().start()
        self.name = name
car1 = ToyotaCar("prius", "electric")

print(car1.name)
print(car1.type)