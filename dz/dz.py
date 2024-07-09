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





#
# class Celoe_chislo:
#     def __set_name__(self, owner, name):
#         self.__name = name
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#     def __set__(self, instance, value):
#         if value < 0:
#                 raise ValueError(f"Значение {self.name} должно быть целым числом")
#         instance.__dict__[self.__name] = value
#
#
#
# class Point3D:
#     x = Celoe_chislo()
#     y = Celoe_chislo()
#     z = Celoe_chislo()
#     def __init__(self, x, y, z):
#         self._x = x
#         self._y = y
#         self._z = z
#
#
# P = Point3D(1, 2, 3)
# print(P.__dict__)


#
# class Student:
#     def __init__(self):
#         self.name1 = "Roman"
#         self.name2 = "Vladimir"
#         self.noyt = self.Nout()
#
#     def info(self):
#         print(f"{self.name1} => {self.noyt.model}, {self.noyt.processor}, {self.noyt.pamyt}")
#         print(f"{self.name2} => {self.noyt.model}, {self.noyt.processor}, {self.noyt.pamyt}")
#
#     class Nout:
#         def __init__(self):
#             self.model = "HP"
#             self.processor = "i7"
#             self.pamyt = 16
#
# student = Student()
# student.info()


#
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def proiz(self):
#         print(f"Произведение: ", self.a * self.b)
#
#     def sum(self):
#         print(f"Сумма: ", self.a + self.b)
#
#     def change(self):
#         self.a = 10
#         self.b = 20
# class RTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.g = round((self.a ** 2 + self.b ** 2) ** (1/2), 2)
#
#
#     def gipotinyza(self):
#         print(f"Гипотенуза ABC: ", round((self.a ** 2 + self.b ** 2) ** (1/2), 2))
#
#     def plosh(self):
#         print(f"Площадь АВС: ", self.a * self.b * 1/2)
#
#     def info(self):
#         self.gipotinyza()
#         print(f"Прямоугольный треугольник АВС ({self.a}, {self.b}, {self.g})")
#         self.plosh()
#
# pair = Pair(5, 8)
# r = RTriangle(5, 8)
# r.info()
# print()
# pair.sum()
# pair.proiz()
# pair.change()
# r.change()
# print()
# r.info()
# pair.sum()
# pair.proiz()


# import json
# from random import choice
#
#
# def gen_person():
#     _id = ''
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(_id) != 10:
#         _id += choice(nums)
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         _id: {
#             'name': name,
#             'tel': tel
#         }
#     }
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data = data | person_dict
#     with open("persons.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
#
#
# todos_by_user = {}  # {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo['userId']] += 1  # {1: 2}
#         except KeyError:
#             todos_by_user[todo['userId']] = 1  # {1: 1, 2: 1, 3: 1}
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]
#
# max_complete = top_users[0][1]
# print(max_complete)  # 12
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:  # 11 < 12
#         break
#     users.append(str(user))
# print(users)  # ['5', '10']
#
# max_users = " and ".join(users)
# print(max_users)
# print(f"Users {max_users} completed {max_complete} Todos")
#
#
# def keep(todo):
#     completed = todo["completed"]
#     max_count = str(todo["userId"]) in users
#     return completed and max_count




# import requests
# import json
# import csv
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# with open("todos.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(todos[0].keys()))
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)


#
# import requests
# from bs4 import BeautifulSoup
#
# def main():
#     url = "https://www.joomfox.org/subject-themes/news-portal.html"
#     get_data(get_html(url))
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("div", class_="container")
#     plagins = p1.find_all("id=leading-0")
#     print(plagins)
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# if __name__ == '__main__':
#     main()


# dz.
#
# from jinja2 import Template
#
# menus = [
#     {"href": "/index", "menu": "Главная"},
#     {"href": "/news", "menu": "Новости"},
#     {"href": "/about", "menu": "О компании"},
#     {"href": "/shop", "menu": "Магазин"},
#     {"href": "/contacts", "menu": "Контакты"}
# ]
#
# link = """
# <ul>
#     {% for c in menus %}
#         {% if c.menu == "Главная" -%}
#             <li><a href="{{ c['href'] }}" class = "active">{{ c['menu'] }}</a></li>
#         {% else -%}
#             <li><a href="{{ c['href'] }}">{{ c['menu'] }}</a></li>
#         {% endif -%}
#
#     {% endfor %}
# </ul>
# """
#
# tm = Template(link)
# msg = tm.render(menus=menus)
#
# print(msg)




from jinja2 import Template


html = """
{%- macro get_input(type='text', name='', placeholder='') -%}
    <input type="{{type}}" name="{{name}}"  placeholder="{{placeholder}}">
{%- endmacro -%}

<p>{{get_input(name='firstname', placeholder='Имя')}}</p>
<p>{{get_input(name='lastname', placeholder='Фамилия')}}</p>
<p>{{get_input(name='address', placeholder='Адрес')}}</p>
<p>{{get_input(type='tel', name='phone', placeholder='Телефон')}}</p>
<p>{{get_input(type='email', name='email', placeholder='Почта')}}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)












