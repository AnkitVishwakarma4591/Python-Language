# Define a circle class to create a circle with radius r using the constructor.
# define an Area() method of the class which calculate the area of the circle.
# define a perimeter() method of the class which allows you to calculate the perimeter of the circle.

class circle:
    def __init__(self,radius):
        self.radius = radius
        
    def Area(self):
        self.area = (22/7) * self.radius ** 2
        print("Area of circle is :",self.area)
        
    def Perimeter(self):
        self.perimeter = 2 * (22/7) * self.radius
        print("Perimeter of circle is :",self.perimeter)
        
crl1 = circle(21)
crl1.Area()
crl1.Perimeter()