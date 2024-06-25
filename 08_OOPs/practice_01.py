# Create student class that takes name & marks of 3 students as arguments in constructor .Then create a method to print the average.

# class student :
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,"your avg score is  :",sum/len(self.marks))
        
# s1 = student("Ankit",[10,20,30])
# s1.get_avg()


# class Student :
#     def __init__(self,name):
#             self.sub_marks_a = int(input("enter 1st sub marks:"))
#             self.sub_marks_b = int(input("enter 2nd sub marks:"))
#             self.sub_marks_c = int(input("enter 3rd sub marks:"))
#             self.sum = self.sub_marks_a + self.sub_marks_b + self.sub_marks_c
#             self.avg = self.sum/3
#             self.name = name
        
#     def get_avg(self):
        
#         print("hi",self.name,"your avg score is :",self.avg)
        
# s1 = Student("Ankit")
# s1.get_avg()


class Student :
    def __init__(self,name):
        print("To see avg score of subjects")
        self.sub = int(input("Enter no. of Subject :"))
        self.marks =[]
        for i in range(1,self.sub+1,1):
            self.marks.append(int(input(f"Enter {i} sub marks :")))
            
        self.sum = 0
        for itme in self.marks:
            self.sum+=itme
            
        self.avg = self.sum/len(self.marks)
        self.name = name
        
    def get_avg(self):
        
        print("hi",self.name,"your avg score of",self.sub,"subjects are :",self.avg)
        
s1 = Student("Ankit")
s1.get_avg()