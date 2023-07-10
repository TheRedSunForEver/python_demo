def greeting(name):
    print("hi, " + name)


greeting("Tom")


def add_numbers(a, b):
    result = a + b
    return result


sumValue = add_numbers(2, 3)
print(sumValue)


# 参数默认值
def greet(name, greet_prefix="Hello"):
    print(f"{greet_prefix}, {name}")


greet("James")
greet("James", "Good morning")
