x = float(input("输入一个值："))
abs_x = x

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
    abs_x = -x
print("该值绝对值为：", abs_x)