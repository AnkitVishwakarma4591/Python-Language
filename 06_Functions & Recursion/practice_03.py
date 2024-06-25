# WAP to print the elements of a list in a single line (list is a parameter)
cities = ['Mumbai','Jharkhand','Ranchi','Madhya pardesh','Bhopal','Kolkata']

def print_lis(list):
    for items in list:
        print(items,end=" ")
        
print_lis(cities)