# WAP to find the sum of first n numbers.(using while loop):

n = int(input("enter any to find sum :"))
sum = 0
i = 1
while i<=n:
    sum+=i
    i+=1
print("Sum of",n," = ",sum)