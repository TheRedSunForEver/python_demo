with open("./file_demo.py", encoding="utf-8") as f:
    content = f.read()
print(content)
print("----")
with open("./file_demo.py") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")

# write file
with open("./data.txt", "w", encoding="utf-8") as f:
    for i in range(5):
        f.write(str(i) + "\n")
