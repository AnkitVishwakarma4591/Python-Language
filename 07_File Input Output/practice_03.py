#  search if the "learning" word is exists in the file or not 

# word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
    
#     if word in data:
#         print("Found")
#     else:
#         print("Not Found")


def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(word in data):
            print("Fonnd")
        else:
            print("Not Found")
check_for_word()