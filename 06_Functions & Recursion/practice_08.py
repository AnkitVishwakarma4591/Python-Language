# Write a recursive function to calculate the sum of first n natural numbers:

n = int(input("Enter any number : "))
def add(n):
    if(n == 0):
        return 0
    else:
        return add(n-1)+n
    
print(add(n))