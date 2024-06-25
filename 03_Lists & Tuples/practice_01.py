# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# 1st way

# movies1 = input("Enter your 1st favorite movie :")
# movies2 = input("Enter your 2nd favorite movie :")
# movies3 = input("Enter your 3rd favorite movie :")

# movies = [movies1,movies2,movies3]
# print(movies)

# 2nd way

# movies = []
# movies.append(input("Enter your 1st favorite movie :"))
# movies.append(input("Enter your 2nd favorite movie :"))
# movies.append(input("Enter your 3rd favorite movie :"))
# print(movies)

# 3rd way 

movies = []
movies1 = input("Enter your 1st favorite movie :")
movies2 = input("Enter your 2nd favorite movie :")
movies3 = input("Enter your 3rd favorite movie :")

movies.append(movies1)
movies.append(movies2)
movies.append(movies3)
print(movies)