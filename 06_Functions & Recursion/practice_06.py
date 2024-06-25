# To checking enter nuber is Even or Odd:

num = int(input("Enter any number to check Even or Odd :"))
def checking(num):
    if(num%2 == 0):
        print(num,"Even")
    else:
        print(num,"Odd")
        
checking(num)