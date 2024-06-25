# Example of single inheritance 

class car:
    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car stoped...")
        
class toyotacar(car):
    def __init__(self,name):
        self.name = name
        
    @staticmethod
    def speed():
        print("200KM/h")
        
c1 = toyotacar("Fortuner")
c1.start()
c1.speed()
c1.stop()