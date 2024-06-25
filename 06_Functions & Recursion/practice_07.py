# WAP to find Factorial of number:
n = int(input("Enter any number : "))
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n - 1)*n
print(fact(n))


