# Write a recursive function to print all elements in a list
# Hint : use list & index as parameter.

cities = ['Mumbai','Jharkhand','Ranchi','Madhya pardesh','Bhopal','Kolkata']

def print_list(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
print_list(cities)


# city = []
# for i in range(1,11,1):
#     city.append(input(f"enter {i} cities name :"))
    
# print(city)