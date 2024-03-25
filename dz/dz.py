# def plosh(a, b, c):
#
#     def inner():
#         s = 2*(a*b + b*c + a*c)
#         print(s)
#     return inner()
#
#
# plosh(2, 4, 6)



# s = 1
#
#
# def plosh(a, b, c):
#     def inner():
#         global s
#         s = 2 * (a * b + b * c + a * c)
#         print(s)
#
#     return inner()
#
#
# plosh(2, 4, 6)



# def decor(fn):
#
#     def wrap(*arg):
#         print("Среднее арифметическое:",  fn(*arg) / len(arg))
#     return wrap
#
#
# @decor
# def func(*args):
#     print("Сумма чисел: ", args, "=", sum(args))
#     return sum(args)
#
#
# func(1, 2, 3, 4)

# name = input("Введите ФИО: ")
# one = name[:name.find(" ")]
# a = name.split()
# print(one + " " + a[1][0] + "." + a[2][0] + ".")


# import re
# nomer = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"[+7?]\d{10}"
# print(re.findall(reg, nomer))


# import re
# s = input("Введите пароль: ")
# reg = r"([a-zA-Z0-9_@-]{6,18}+)"
# print(re.findall(reg, s))


#
# def count_items(item_list):
#     count = 0  # 10
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)  # count += 2
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


s = [-2, 3, 8, -11, -4, 6]

#
# def sum(chisla):
#     if not chisla:
#         return 0
#     count = 0
#     if chisla[0] < 0:
#             count += 1
#     return sum(chisla[1:]) + count
#
#
# print(sum(s))


# import os
#
# root = r'nested1'
# objs = os.listdir(root)
# print(objs)
#
# objs = list(map(lambda i: os.path.join(root, i), objs))
# print(objs)
#
# class Car:
#     def __init__(self, name, god, proizvoditel, moshnost, color, price):
#         self.name = name
#         self.god = god
#         self.proizvoditel = proizvoditel
#         self.moshnost = moshnost
#         self.color = color
#         self.price = price
#
#     def print_info(self):
#
#         print("*"*10, "Данные автомобиля", "*"*10)
#         print("Название модели:", self.name)
#         print("Год выпуска:", self.god)
#         print("Производитель: ", self.proizvoditel)
#         print("Мощность двигателя:", self.moshnost)
#         print("Цвет машины: ", self.color)
#         print("Цена: ", self.price)
#         print("="*40)
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_god(self, god):
#         self.god = god
#
#     def get_god(self):
#         return self.god
#
#     def set_proizvoditel(self, proizvoditel):
#         self.proizvoditel = proizvoditel
#
#     def get_proizvoditel(self):
#         return self.proizvoditel
#
#     def set_moshnost(self, moshnost):
#         self.moshnost = moshnost
#
#     def get_moshnost(self):
#         return self.moshnost
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# p1 = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
# p1.print_info()
# p1.set_name("X7 M50i")
# print(p1.get_name())
# p1.set_god("2021")
# print(p1.get_god())
# p1.set_proizvoditel("BMW")
# print(p1.get_proizvoditel())
# p1.set_moshnost("530 л.с.")
# print(p1.get_moshnost())
# p1.set_color("white")
# print(p1.get_color())
# p1.set_price("10790000")
# print(p1.get_price())



class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def _check_value(a):
        if isinstance(a, int) or isinstance(a, str):
            return True
        return False

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if Person._check_value(name):
            self.__name = name
    @name.deleter
    def name(self):
        del self.__name
    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        if Person._check_value(old):
            self.__old = old
    @old.deleter
    def old(self):
        del self.__old



p = Person("Irina", 26)
print(p.__dict__)
p.name = "Igor"
p.old = 31
print(p.name)
print(p.old)
del p.name
print(p.__dict__)









