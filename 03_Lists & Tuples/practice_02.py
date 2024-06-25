# WAP to check if a list contains a palindrome of elements. 
# Hint : use copy() method()

list  = [1,2,3,2,1]
copy = list.copy()
copy.reverse()
if(list == copy):
    print("is palindrome")
else:
    print("not a palindrome")
    
