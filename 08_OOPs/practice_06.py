# Adding Complex number

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def show_number(self):
        print(self.real,"i +",self.img,"j")
        
    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img 
        print("_________")
        return complex(newReal,newImg)
    
num1 = complex(1,2)
num1.show_number()

num2 = complex(2,5)
num2.show_number()

num3 = num1.add(num2)
num3.show_number()