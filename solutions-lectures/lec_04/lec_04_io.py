with open("hi_again.txt", "r") as file:
    file.write("Hello again, World!")

print("File successfully written")

with open("hi_again.txt", "r") as file:
    content = file.read()

print(content)
