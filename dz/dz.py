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




#
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     def _check_value(a):
#         if isinstance(a, int) or isinstance(a, str):
#             return True
#         return False
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         if Person._check_value(name):
#             self.__name = name
#     @name.deleter
#     def name(self):
#         del self.__name
#     @property
#     def old(self):
#         return self.__old
#     @old.setter
#     def old(self, old):
#         if Person._check_value(old):
#             self.__old = old
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
#
# p = Person("Irina", 26)
# print(p.__dict__)
# p.name = "Igor"
# p.old = 31
# print(p.name)
# print(p.old)
# del p.name
# print(p.__dict__)



#
# class Ploshad:
#
#     def __init__(self, trosnov, trvysota, kvstorona, prymougst1, prymougst2):
#         self.trosnov = trosnov
#         self.trvysota = trvysota
#         self.kvstorona = kvstorona
#         self.prymougst1 = prymougst1
#         self.prymougst2 = prymougst2
#
#
#     @staticmethod
#     def plosh_tr(osnov, vysota):
#         return 1/2 * osnov * vysota
#
#     @staticmethod
#     def plosh_kv(a):
#         return a**2
#
#     @staticmethod
#     def plosh_pr(a, b):
#         return a * b
#
#
#     def nahogdenye_plosh_tr(self):
#         plosh = Ploshad.plosh_tr(self.trosnov, self.trvysota)
#         print(f"Площадь треугольника через основание и высоту (6, 7): {plosh}")
#
#
#     def nahogdenye_plosh_kv(self):
#         plosh = Ploshad.plosh_kv(self.kvstorona)
#         print(f"Площадь квадрата (7): {plosh}")
#
#
#     def nahogdenye_plosh_pr(self):
#         plosh = Ploshad.plosh_pr(self.prymougst1, self.prymougst2)
#         print(f"Площадь прямоугольника (2,6): {plosh}")
#
#
#
#
# pl = Ploshad(6, 7, 7, 2, 6)
# pl.nahogdenye_plosh_tr()
# pl.nahogdenye_plosh_kv()
# pl.nahogdenye_plosh_pr()
#

#
#
# class Clock:
#     __Day = 86400
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__Day
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec % other.sec)
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec < other.sec:
#             return True
#         return False
#
#     def __le__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec <= other.sec:
#             return True
#         return False
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec > other.sec:
#             return True
#         return False
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         if self.sec >= other.sec:
#             return True
#         return False
#
#
#
# c1 = Clock(600)
# c2 = Clock(200)
# c7 = Clock(800)
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = c1 - c2
# print("c1 - c2: ", c3.get_format_time())
# c4 = c1 * c2
# print("c1 * c2: ", c4.get_format_time())
# c5 = c1 // c2
# print("c1 // c2: ", c5.get_format_time())
# c6 = c1 % c2
# print("c1 % c2: ", c6.get_format_time())
# c1 -= c2
# print("c1 -= c2: ", c1.get_format_time())
# c1 = Clock(600)
# c1 *= c2
# print("c1 *= c2: ", c1.get_format_time())
# c1 = Clock(600)
# c1 //= c2
# print("c1 //= c2: ", c1.get_format_time())
# c1 = Clock(600)
# c1 %= c2
# print("c1 % c2: ", c1.get_format_time())
# c1 = Clock(600)
# if c1 < c7:
#     print("c1 < c7 True")
# else:
#     print("c1 < c7 False")
#
# if c1 <= c7:
#     print("c1 <= c7 True")
# else:
#     print("c1 <= c7 False")
#
# if c1 > c7:
#     print("c1 > c7 True")
# else:
#     print("c1 > c7 False")
#
# if c1 >= c7:
#     print("c1 >= c7 True")
# else:
#     print("c1 >= c7 False")






class Celoe_chislo:
    def __set_name__(self, owner, name):
        self.__name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value < 0:
                raise ValueError(f"Значение {self.name} должно быть целым числом")
        instance.__dict__[self.__name] = value



class Point3D:
    x = Celoe_chislo()
    y = Celoe_chislo()
    z = Celoe_chislo()
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


P = Point3D(1, 2, 3)
print(P.__dict__)





