# Search for a number x in this tuple using loop.
# (1,4,9,16,25,36,49,64,81,100)

# tuple = (1,4,9,16,25,36,49,64,81,100)
# num = int(input("enter number to search:"))
# i = 0 
# while i<=len(tuple):
#     print(num == tuple[i])
#     i+=1

tuple = (1,4,9,16,25,36,49,64,81,100)
num = int(input("enter number to search:"))
i = 0 
while i<=len(tuple):
    if(num == tuple[i]):
        print("Found")
    else:
        print("Not found")
    i+=1
    

