# Q.1) print the elements of the following list using a  for loop:
# [1,4,9,16,25,36,49,64,81,100]

# a = [1,4,9,16,25,36,49,64,81,100]
# for i in a:
#     print(i)

# Q.2) Search for a number x in this tuple using  for loop
# (1,4,9,16,25,36,49,64,81,100)

a = (1,4,9,16,25,36,49,64,81,100)
num = int(input("enter any number to search in tuple :"))

for i in a:
    print(i == num)