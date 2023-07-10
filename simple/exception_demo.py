try:
    x = int(input("请输入一个被除数："))
    print("30除以", x, "等于", 30 / x)
except ValueError:
    print("输入了无效的整数，请重新输入")
except ZeroDivisionError:
    print("被除数不能等于0，请重新输入")
except:
    print("其他异常")
else:
    print("再见")
