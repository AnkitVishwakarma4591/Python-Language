# Q.1) print number from (1 to 100) using for loop

for i in range(1,101,1):
    print(i)
    
# Q.2) print number from (100 to 1) using for loop
for i in range(100,0,-1):
    print(i)
    
    
# Q.3) print the multiplication table of a number, using for loop.
n = int(input("enter any number to print a table :"))
for i in range(1,11,1):
    print(n,"*",i," = ",n*i)