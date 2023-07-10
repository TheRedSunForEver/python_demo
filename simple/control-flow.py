score = 95
if score >= 60:
    print("及格")
else:
    print("不及格")

str_for_loop = "Matplotlib"
for str_idx in str_for_loop:
    print(str_idx)

i = 0
while i < 5:
    print(i)
    i += 1

try:
    x = 1 / 0
except ZeroDivisionError:
    print("除数不能为零")