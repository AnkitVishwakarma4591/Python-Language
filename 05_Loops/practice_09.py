# WAP to find the factorial of first n number.(using for loop)

n = int(input("enter number to find factorial :"))
fact = 1
for i in range(1,n+1,1):
    fact*=i
    
print("Factorial of",n," = ",fact)