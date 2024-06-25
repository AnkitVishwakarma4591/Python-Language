# WAF to find in which line of the file does the word "learning" occure first print -1 if word not found.

def check_for_line():
    word = "learning"
    line_no = 1
    data = True
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1
check_for_line()