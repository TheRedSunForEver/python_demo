# class Banks():
#     bankname = "T Bank"
#     def motto(self):
#         return "Hello"
#
#
# userbank = Banks()
# print(userbank.bankname)
# print(userbank.motto())

# 类的初始化方法，定义一个类对象时自动执行这个方法。
# 初始化方法有一个固定名称是__init__()
class Bank():
    bank_name = "T Bank"

    def __init__(self, uname, money):
        self.name = uname
        self.balance = money
        self.__private_money = 0

    def get_balance(self):
        return self.balance

    def set_private_money(self, p_money):
        self.__private_money = p_money

    def get_private_money(self):
        return self.__private_money


hung_bank = Bank("hung", 100)
# print(hung_bank.name.title(), hung_bank.get_balance())
# hung_bank.balance = 1
# print(hung_bank.get_balance())
hung_bank.__prviate_money = 10
print(hung_bank.__prviate_money)


class Father():
    def home_town(self):
        print("我在东北")


class Son(Father):
    pass


hung = Father()
ivan = Son()
hung.home_town()
ivan.home_town()