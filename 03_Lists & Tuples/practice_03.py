# WAP to count the number of Students with the "A" grade in the following tuple.
# ["C","B","D","A","K","A","B","A"]
# store the above values in a list & sort them from "A" to "K"

# stu_grade = ["C","B","D","A","K","A","B","A"]
# num_of_stu = stu_grade.count("A")
# print("the number of Students with the A grade",num_of_stu)

# # list = list(stu_grade)
# # print(list)
# # list.sort()
# # print(list)


grade = []
i = 1
while i<=10:
    grade.append(input("Enter grade(A-D) of stu :"))
    i+=1
    
print(grade)
print(grade.count("A"))
grade.sort()
print(grade) 