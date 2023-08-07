# 字符串相关演示

# 单行字符串：由一对单引号或一对双引号表示
# 多行字符串：由一对三单引号/双引号表示

print('-- 基础演示 --')
str_a = 'abcd'
str_b = "I'm your teacher, " \
    "Are you ok?" \
    "Hello!"
str_c = '''I'm your teacher,
Are you ok?
Hello!'''

print(str_a)
print(str_b)
print(str_c)

# 常用操作
## x + y: 字符串变量之间用+拼接字符串
print()
print('-- 字符串拼接(+)演示 --')
str1 = 'i'
str2 = 'love'
str3 = 'apple'
print(str1.title() + " " + str2 + " " + str3)
