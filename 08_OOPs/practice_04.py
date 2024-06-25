# Example of multi level Inheritance
class car :
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stoped...")
        
class toyota_car(car):
    def __init__(self,brand):
        self.brand = brand
        
class fortuner(toyota_car):
    def __init__(self,type):
        self.type = type
        super().__init__("BMW")
        

c2 = fortuner("Diesel")
c2.start()
print(c2.type)
print(c2.brand)
c2.stop()