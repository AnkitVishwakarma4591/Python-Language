# Create a new file "practice.txt" using python . Add the following data in it.
#  Hi everyone 
# we are learning file i/o 
# using Java
# i like programming in java .

with open("practice.txt","w") as f:
    f.write("Hi everyone \n we learning file I/o \n using java \n i like programing in java")


# import os
# os.remove("practice.txt")