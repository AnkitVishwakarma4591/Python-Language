# figureout a way to store 9 & 9.0as separate value in the set

# value = {9,"9.0"}
# print(value)

value = {("float",9.0),("int",9)}
print(value)