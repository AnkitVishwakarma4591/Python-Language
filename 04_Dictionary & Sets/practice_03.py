# WAP to enter mark of 3 students from the user and store them in a dictionary. 
# start with an empty dictionary & add one by one are subject name as key & marks.

# stu_details = { }

# score1 = int(input("Enter math mark :"))
# stu_details.update({"Math":score1})
# score2 = int(input("Enter phy mark :"))
# stu_details.update({"Physics":score2})
# score3 = int(input("Enter chem mark :"))
# stu_details.update({"Chemistry":score3})
# print(stu_details)

info = {}
info["math"] = int(input("Enter math mark :"))
info["Physics"] = int(input("Enter phy mark :"))
info["Chemistry"] = int(input("Enter chem mark :"))
print(info)