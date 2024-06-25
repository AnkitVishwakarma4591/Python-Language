# WAP to find the factorial of number(n the parameter)

def factorial(n):
    fact = 1
    for i in range(1,n+1,1):
        fact*=i
    print(fact)
    
factorial(5)