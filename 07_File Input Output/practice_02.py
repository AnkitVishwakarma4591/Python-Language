# WAF that replace all occurrences of "java" with python in practice file_01


with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")

with open("practice.txt", "w") as f:
    f.write(new_data)
