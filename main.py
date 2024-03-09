# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = [i for i in s if 'a' not in i]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s]   #ternarnoe vyragenie
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c']
# print(a)



# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b) # возвращ множество, объед a и b
# # c = a | b  # это union
# # c = a & b  #оставляет в a только те элементы, которые есть в b
# # c = a - b # оставляет только те, которые входят в а но не входят в b
# c = a ^ b # {0, 4} уникальные из а и b
#
# print(c)
# # a |= b    #добавл в a все элементы b
# # a &= b
# # a -= b
# # a ^= b
# print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}

# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))


# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")


# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")


# drawing = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobby = drawing & music
# print(both_hobby)
# drawing = drawing -  both_hobby
# print(drawing)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a > b)

#frozenset

# # s = frozenset([1, 2, 3, 4, 5, 6])
# s = frozenset("Hello")
# print(s)



# #словари(dict)
#
# s = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(s[1])
# print(d['two'])
#
# s1 = ['one', 'two', 'three']
# d1 = {1: 'one', 2: 'two', 3: 'three'}
# print(s1[1])
# print(d1[2])


# d = {0: 'test', 'one': 45, (1, 2.3): 'Korteg', True: 1, 35: [1, 2]}
# print(d)
# d[(1, 2.3)] = 100
# print(d)

# d= {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
#
# d1 = dict(one=1, two=2)
# print(d)
# print(type(d1))



# # d1 = dict(['one', 1, 'two', 2])
# d1 = dict([["one", 1], ['two', 2]])
# print(d1)


# d = {x: x for x in range(7)}
# print(d)



# d = {'one': 1, 'two': 2, 'three': 3}
# print('four' in d)
# # print(len(d))
# # for i in d:
# #     print(i, '->', d[i])
# key = 'one'
# # if key in d:
# #     print(d[key])
# # try:
# #     print(d[key])
# # except KeyError:
# #     print('takogo klucha net ')
# del d[key]
# print(d)


# b = 1
# a = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# for i in a:
#     b *= a[i]
# print(b)



# # d = dict()
# # d[1] = input('-> ')
# # d[2] = input('-> ')
# # d[3] = input('-> ')
# # d[4] = input('-> ')
# d = {x: input('-> ')for x in range(1, 5)}
# print(d)
# try:
#     dislike = int(input("kakoy element iskluch "))
#     del d[dislike]
# except (KeyError, ValueError) :
#     print("Takogo klucha ne syshestvuet")
# print(d)




# # # dz
#
# math = {"Matvei", "Evgeniya", "Michail", "Maxim", "Natalia"}
# physics = {"Maxim", "Matvei", "Alexandr"}
# vseprizery = math | physics
# print(vseprizery)
# both = math & physics
# print(both)
# math = both
# print(math)

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# print(len(d))


# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400],
# }
# for key in goods:
#     print(key, ") ", goods[key][0], " - ",  goods[key][1], " шт. по ", goods[key][2]," руб.", sep="",)

# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Кол-во: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректное. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], " шт. по ", goods[key][2], " руб.", sep="")

# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# del d['x1']
# d['x4'] = 10
# print(d)
# print(d.values())
# print(d.keys())
# print(d.items())
# # for key, value in d.items():
# #     print(key, "->", value)
# print(list(d))  # ['x1', 'x2', 'x3']
# print(list(d.values()))  # [3, 7, 5]
# print(list(d.items()))  # [('x1', 3), ('x2', 7), ('x3', 5)]

# d = {'x1': 3, 'x2': 7, 'x3': 5}
#
# d2 = d.copy()
# print("d =", d)
# print("d2 =", d2)
#
# d2["x4"] = 10
# d['x1'] = 100
#
# print("d =", d)
# print("d2 =", d2)


# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# print(d["x1"])
# value = d.get("x4", "Такого ключа не существует")
# print(value)
# item = d.pop("x1", 0)
# print(item)
# print(d)
# item2 = d.popitem()  #удал послед элемент
# print(item2)
# print(d)
#
# d.clear()   #очищает список
# print(d)



# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# # item = d.setdefault("x1", 10)
# # print(item)
# # print(d)
# # a = {"one": 1, "two": 2, 'x1': 10}
# # print(a)
# # a = list(a.items())
# a = [('one', 1), ('two', 2), ('x1', 10)]
# print(a)
# d.update(a)
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y
# # z = x.copy()
# # z.update(y)
# print(z)

# d = dict.fromkeys(['a', 'b', 'c'], 100)
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d2 = dict()
# d2['name'] = d.pop("name")
# d2['salary'] = d.pop("salary")
# print(d)
# print(d2)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)


# d = {
#     'first': {
#         1: {
#             11: "abc",
#             12: "abc",
#             113: "abc",
#         },
#         2: {
#             11: "abc"
#         },
#         3: {
#             11: "abc"
#         }
#     },
#     'second': {
#         4: {
#             11: "abc"
#         },
#         5:  {
#             11: "abc"
#         }
#     }
# }
# print(d)
#
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y)
#         for z in d[x][y]:
#             print("\t\t", z, ":", d[x][y][z])


# d = {'три': 3, 'один': 1, 'два': 2, 'четыре': 4}
# # d2 = {value: key for key, value in d.items()}
# d2 = {key: value for key, value in d.items() if value <= 2}
# print(d2)
# # d2[1], d2[4] = d2[4], d2[1]
# # print(d2)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
# print(type(s))
# for i in a:
#     if type(i) == str:  # {'one': [1,2,3], 'two': [10,20], 'three': [], 'four': []}
#         d[i] = []  # d['two'] = []
#         s = i  # s = 'two'
#     else:
#         d[s].append(i)  # d['two'].append(20)
#
# print(d)


# d = {
#     "John": {
#         "N": 3056,
#         "S": 8463,
#         "E": 8441,
#         "W": 2694
#     },
#     "Tom": {
#         "N": 4832,
#         "S": 6786,
#         "E": 4737,
#         "W": 3612
#     },
#     "Anne": {
#         "N": 5239,
#         "S": 4802,
#         "E": 5820,
#         "W": 1859
#     },
#     "Fiona": {
#         "N": 3904,
#         "S": 3645,
#         "E": 8821,
#         "W": 2451
#     }
# }
# for x in d:
#     print(x)
#     for y in d[x]:
#         print(y, ": ", d[x][y])
# imya = input("Имя: ")
# region = input("Регион: ")
# print(d[imya][region])
# znach = input("Новое значение: ")
# d[imya][region] = znach
# print(d[imya])


# zip()

# one = [1, 2, 3]
# two = ["one", "two", "three", 4, 5]
# three = [2.5, 4.6, 8.9]
#
# d = dict(zip(two, one))
# print(d)
#
# lst = list(zip(one, two))  #, three
# lst = list(zip(one))
# print(lst)

# f = {k: v for k, v in zip(two, one)}
# print(f)


# one = {"name": "Igor", "surname": "Doe", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Smith", "job": "Manager"}
# three = {"name": "Irina", "surname": "Smith", "job": "Manager"}
#
#
# for (k1, v1), (k2, v2), (k3, v3) in zip(one.items(), two.items(), three.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)
#     print(k3, "->", v3)


# lst = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*lst)
# print(a)  # (1, 2, 3)
# print(b)  # ('one', 'two', 'three')

# a = {"one": 1, 'two': 2, "three": 5}
# b = {"three": 3, 'four': 4}
# print({**a, **b})  # {"one": 1, 'two': 2, "three": 3, 'four': 4}
#
# for k, v in {**a, **b}.items():
#     print(k, "->", v)

# data = [5, 7, 9, 4, 1, 3, 5, 8, 6, 4]
# data = ["red", "green", "blue"]
#
# for num, color in enumerate(data, 1):
#     print(num, ") ", color, sep="")
# j = 1
# for i in data:
#     print(j, ") ", i, sep="")
#     j += 1

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]  # [1, 2, 3, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7, "abc"))
# print(func())


# def summa(*param):
#     res = 0
#     for i in param:
#         res += i
#     return res
#
#
# print(summa(1, 8, 9, 6, 5, 4, 7, 3, 5, 1, 4, 2, 6))
# print(summa(5, 4, 7, 3, 5, 1, 4))
# print(summa(4, 2, 6))


# def to_dict(*di):
#     # dictionary = {}
#     # for i in di:
#     #     dictionary.update({i: i})
#     #
#     # return dictionary
#     # return dict(zip(di, di))
#     return {i: i for i in di}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))



# def ch(*args):
#     average = sum(args) / len(args)
#     print(average)
#     res = []
#     for num in args:
#         if average > num:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(5, 9, 8, 7, 6))


# def print_scores(student, *scores):
#     print("Name:", student)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Roman", 5, 4, 3, 5, 4, 5, 5, 3, 5)
# print_scores("Nikita", 5, 5, 3, 5)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(name="Python"))


# def intro(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Irina", surname="Sharma", age=22)
# intro(name="Igor", surname="Wood", email="igor@gmail.com", age=26, phone=987654321)



# def func(a, b, *args, dd=5, cc=7, **kwargs):
#     return a, b, args, kwargs, dd, cc
#
#
# print(func(1, 2, 3, 4, 5, aa=1, cc=3, bb=2))  #


# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name="Bob", age=31, weight=61, eyes_color="grey")
# print(my_dict)




# name = "Tom"  # глобальная переменная
# surname = ""
#
#
# def hi():
#     global name, surname
#     name = "Sam"  # локальная переменная
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)


# print(name)
# hi()
# bye()
# print(name)
# print(surname)



# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5



# x = 10
#
#
# def func(a):  # a = 3
#     # x = 2
#
#     def inner():
#         # x = 6
#         print("x:", x)
#         return a + x  # 3 + 10
#
#     return inner()
#
#
# print(func(3))


# students = {}
# a = 0
# Kolvo_stud = int(input("Количество студентов: "))
# for i in range(1, Kolvo_stud + 1):
#     stud = input(str(i) + "-й студент: ")
#     ball = int(input("Балл: "))
#     students[stud] = ball
#     a += ball
# sredball = a/Kolvo_stud
# print(sredball)
# for i in students:
#     if students[i] > sredball:
#         print("Студенты с баллом выше среднего:", i)


# sum = "Hello"
#
# print(sum)
#
# lst = [1, 2, 3, 4, 5, 6, 4]
# print(sum(lst))


# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")



# def fun1():
#     a = 6  # 2
#
#     def fun2(b):  # b = 4
#         a = 4  # 5  # a = 6
#         print(a + b)  # 6  # a + b = 8 (10)
#
#     print("a:", a)  # 3
#     fun2(4)  # 4
#
#
# fun1()  # 1


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         # print(a)
#
#     inner()
#     t = a  # 35
#
#
# fn()
# q = x + t  # 25 + 35
# print(q)  # 60


# def fn1():
#     x = 25  # 55
#
#     def fn2():
#         x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)  # 33  55
#
#     fn2()
#     print("fn1.x =", x)  # 25  55
#
#
# fn1()




# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0  # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print("a:", a)
#         # print("b:", b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]



# def outer(n):  # 5
#     def inner(x):  # 10
#         return n + x
#
#     return inner
#
#
# out1 = outer(5)
# print(out1(10))
#
# out2 = outer(6)
# print(out2(4))

# print(outer(5)(10))



# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())



# def func(city):
#     count = 0  # 3  # 5
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
# res2()
# res2()
#
# res1()
# res1()
# res1()
# res1()



# lambda - функция (выражение)

# def func(x, y):
#     return x + y
#
#
# print(func(2, 3))

# print((lambda x, y: x + y)(2, 3))
# print((lambda x, y: x + y)(12, 3))

# variable = lambda x, y: x + y
#
# print(variable(2, 3))



# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())


# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6))
# print((lambda *args: args)("a", "b", "c"))



# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t("abc_"))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(5)
# print(f(10))


# def outer1(n):
#     return lambda x: n + x
#
#
# f1 = outer1(5)
# print(f1(10))
#
# outer2 = lambda n: lambda x: n + x
#
# f2 = outer2(5)
# print(f2(10))

# print((lambda n: lambda x: n + x)(5)(10))


# print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))
# print((lambda n: lambda x: lambda y: n+x+y)(int(input("Введите 1 число: ")))(int(input("Введите 2 число: ")))
# (int(input("Введите 3 число: "))))


# def func(i):
#     return i[1]
#
#
# d = {"b": 15, "a": 7, "c": 3}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# print(dict(lst))



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

# def outer(a, b, c):  # 2, 4, 6
#     s = 0  # 44
#
#     def inner(i, j):
#         nonlocal s
#         s = s + i * j  # s += i * j   # s = 20 + 24 = 44
#
#     inner(a, b)  # 2, 4
#     inner(a, c)  # 2, 6
#     inner(b, c)  # 4, 6
#     return 2 * s  # 2 * 44
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['last_name'])
# print(res1)
# res2 = sorted(players, key=lambda item: item['rating'])
# print(res2)
# res3 = sorted(players, reverse=True, key=lambda item: item['rating'])
# print(res3)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]
# b = a[0](5, 3)
# print(b)


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
# }
#
# d[3]()

# print((lambda a, b: a if a > b else b)(5, 13))


# print((lambda a, b, c: a if (a < b) and ((b < c) or (b > c)) else b if b < c else c)(12, 15, 6))


# print((lambda a, b, c: a if (a < b) and (a < c) else b if (b < c) and (b < a) else c if (c < a) and (
#             c < b) else "Ну тут уже всё:)")(22, 35, 16))
# print((lambda a, b, c: a if (a < b) and (a < c) else b if (b < c) and (b < a) else c)(12, 36, 15))
#
# print((lambda a, b, c: a if min(a, b, c) == a else b if min(a, b, c) == b else c if min(a, b,

#  c) == c else "Несколько равных")(
#     11, 2, 111))
#
# print((lambda *args: min(args))(12, 5, 6))
# print((lambda *args: sorted(args)[0])(2, 5, 6))
# print((lambda *args: sorted(args)[-1])(2, 5, 6))


# map(func, iterable), filter(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lt = list(map(mult, lst))
# print(lt)

# lt1 = list(map(lambda t: t * 2, lst))
# print(lt1)
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# lst = ['1', '2', '3', '4', '5']
# print(lst)
# print(list(map(lambda x: int(x), lst)))
# print([int(i) for i in lst])
# print(list(map(int, lst)))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: {x: y}, st, num)))

# st = [9, 2, 7, 6, 5]
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: x + y, st, num)))


# t = ('abcd', 'abc', 'cdefg', 'def', 'gth', '', False)  # 'abcdabcdabcd'
#
# # t2 = list(filter(lambda s: len(s) == 3, t))
# t2 = list(filter(lambda s: s, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, b)))


# от 1 до 40

# from random import randint
#
# arr = [randint(1, 40) for i in range(10)]
# print(arr)
# # print(list(filter(lambda a: (a >= 10) and a <= 20, arr)))
# print(list(filter(lambda a: 10 <= a <= 20, arr)))


# Вывести на экран квадраты нечетных чисел от 1 до 10
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
# print([x ** 2 for x in range(1, 10) if x % 2])


# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'  # 3
#
#
# def super_func(func):  # (def hello(): return 'Hello, I am func "hello"')
#     print('Hello, I am func "super_func"')  # 2
#     print(func())  # 4
#
#
# super_func(hello)  # 1


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(id(test))
# print(id(hello))
# print(test())


# def my_decorator(func):
#     def inner():
#         print('Code before')
#         func()
#         print('Code after')
#     return inner
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()



# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print('*' * 40)
#         func()
#         print('-' * 40)
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# @my_decorator
# def hello():
#     print('Hello, I am func "hello"')
#
#
# func_test()
# hello()

#
# s = ["madam", "fire", "tomato", "book", "kiosk", "mom", "pokop"]
# for i in s:
#     if i == i[::-1]:
#          print(i)




# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()




# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Мумладзе")




# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def func(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
# @args_decorator
# def func1(study):
#     print("Мне нравится", study)
#
#
# func("Борис", "Елизавета", "Светлана", study="JavaScript")
# func("Владимир", "Екатерина", "Виктор")
# func1(study="HTML")


# def decor_args(arg1, arg2):
#     def decor(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return decor
#
#
# @decor_args("Сумма:", "+")
# def summa(a, b):
#     print(a + b
#
#
# @decor_args("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2))


# def decor_args(arg1):
#     def decor(fn):
#         def wrap(x):
#             return arg1 * fn(x)  # 3 * 5
#
#         return wrap
#
#     return decor
#
#
# @decor_args(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# Строки

# print(int("19"))
# print(int("19.5"))
# print(int(19.5))

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))


# print(bin(18))  # 0b10010 - двоичная
# print(oct(18))  # 0o22 - восьмеричная
# print(hex(18))  # 0x12 - шестнадцатеричная
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0x12)

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 2)
# print("y1" in e)
# print(e[0])
# print(e[1:3])

# s = "Python"  # Pytton
# # s[3] = "t"
# s = s[:3] + 't' + s[4:]
# print(s)


# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old:
#             s2 = s2 + new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = change_char_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)

# print("Привет")
# print(u"Привет")


# print("C:\\folder\\fil\nes.txt\\")
# print(r"C:\folder\files\\"[:-1])
# print(r"C:\folder\files" + "\\")

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")


# ch = 5.26987412
#
# print(f"Число: {round(ch, 3)}")
# print(f"Число: {ch:.3f}")


# x = 10
# y = 5
# print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# num = 74
#
# print(f"{{{{{num}}}}}")
#
# print("C:\\\\text")

# dir_name = 'my_doc'
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# def avg(fn):
# #     def wrap(*arg):
# #         a = ""
# #         for i in arg:
# #             a += str(i) + ", "  # "2, 3, 3, 4, "
# #         print("Среднее арифметическое:", a[:-2], "=", fn(*arg) / len(arg))
# #
# #     return wrap
# #
# #
# # @avg
# # def summa(*args):  # (2, 3, 3, 4)
# #     print("Сумма чисел:", ", ".join(map(str, args)), "=", sum(args))
# #     return sum(args)
# #
# #
# # summa(2, 3, 3, 4)


# s = """
# Несколько
# строк
# """
# # print(s)
#
# s1 = '''
# Несколько
# строк
# '''
# print(s1)
#
# "Несколько строк"
# print(s2)



# def square(n):
#     """Принимает число n, возвращает квадрат числа n."""
#     print()
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# # max(5, 5)
# # len()
# print(len.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(max.__doc__)
# print(dict.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('й'))


# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(8364))


# a = 97
# b = 122
#
# if a < b:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65


# from random import randint
#
# shortest = 7
# longest = 16
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):  # range(10)
#         rand_char = chr(randint(min_ascii, max_ascii))
#         res += rand_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# s = "hello, WORLD! I am learning Python."
# # print(s.capitalize())  # Hello, world! i am learning python.
# # print(s.lower())  # hello, world! i am learning python.
# # print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# # # print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# # # print(s.title())  # Hello, World! I Am Learning Python.
# # print(s)

# print(s.count("l"))
# print(s.count("l", 3))
# print(s.count("l", 3, 10))


# # print(s.find("Python1"))  # возвращает индекс первого вхождения подстроки в строку, если такой подстроки нет
# # # возвращает "-1"
# # # print(s.find("l", 4, 20))
# # print(s.find("l"))
# # print(s.rfind("l"))
# #
# # print(s.index("l"))  # ValueError
# # print(s.rindex("l"))


# st = input("Введите два слова через пробел: ")
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second + " " + first)


# s = "hello, WORLD! I am learning Python."
# print(s.startswith("I am", 14))
# print(s.index("I am"))
# print(s.endswith("on."))

# print(int("789"))

# print('123'.isdigit())  # только числа
# print('qЙwee'.isalpha())  # только буквы
#
# print('Abc123'.isalnum())  # только буквы или цифры
#
# print('aИc0123"№'.islower())  # только нижний регистр
# print('ASD0123"№'.isupper())  # только верхний регистр

# n = input("Введите число: ")
# if n.isdigit():
#     n = int(n)
#     print(n * 2)


# print('py'.center(10))
# print(' py '.center(11, "-"))


# print('    py    '.lstrip())
# print('    py    '.rstrip())
# print('    p y    '.strip())

# print('https://www.pythons.org'.strip('/:pths.org'))
# print('https://www.pythons.org'.lstrip('/:pths').rstrip('.org'))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. New"
# print(str1.replace("Nython", "Python"))
# print(str1.replace("N", "P"))

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(", ".join("Hello"))

# print("Строка разделенная пробелами".split())  # ['Строка', 'разделенная', 'пробелами']
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit(".", 2))

# name = input("Введите ФИО: ")
# one = name[:name.find(" ")]
# a = name.split()
# print(one + " " + a[1][0] + "." + a[2][0] + ".")





# Регулярные выражения

import re


# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "а"
#
# print(re.findall(reg, s))  # возвращает список содержащий все совпадения
#
# print(re.search(reg, s))  # месторасположение первого совпадения с объектом
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
#
# print(re.match(reg, s))  # поиск совпадения с шаблоном вначале строки
#
# print(re.split(reg, s, 1))  # возвращает список, в котором строка разбита по шаблону
#
# print(re.sub(reg, "!", s, 2))  # поиск и замена


# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 198673 Hello"
# reg = "[21][0-9][0-9][0-9]"
# reg = "[А-яЁё]"
# reg = "[A-Za-z]"
# reg = r"\."
# reg = r"[A-Za-z\[\]-]"
# reg = r"[^0-9]"
# reg = r"[^А-яЁёA-Za-z0-9]"
# print(re.findall(reg, s))

# print(ord('Я'))
# print(ord('а'))



# st = "Час в 24 формате от 00 до 23. 2021-06-15T19 : 30. Минуты, в диапазоне от 00 до 59. 2021-06-15T01 : 09."
# pattern = r"[0-2][0-9]\s:\s[0-5][0-9]"
# print(re.findall(pattern, st))


# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 198673 Hel_lo 20000000000000000000000000"
# reg = r"[20]*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1


# d = "Цифры: 7, +17, --42, 0013, 0.3"
# reg = r'[+-]?[\d.]+'
# print(re.findall(reg, d))


# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", s))
# print(re.sub('-', '.', s))
# print("Дата рождения:", re.sub('-', '.', re.sub(r"\s#.*", "", s)))
# # print("Дата рождения:", "05.03.1987")
# # Дата рождения: 05.03.1987
# print("Дата рождения", re.sub("-", ".", re.sub("\\s#.*", "", s)))



# s = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=\s*[^;]+'
# # reg = r'[^;]+'
# print(re.findall(reg, s))

# s = "12 сентября 2024 года 568789456"
# reg = r"\d{2,4}"
# print(re.findall(reg, s))



# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
# print(re.findall(reg, s))

# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9-]{3,16}$", login)
#
#
# print(validate_login("Python-master"))

#
# nomer = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, nomer))




# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "я"
#
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))


# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))


# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))


# text = """Python,
# python,
# PYTHON"""
#
# reg = "(?mi)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# +?, *?, ??
# {m,n}?, {,n}?, {m,}?

# s = "12 сентября 2024 года 568789456"
# reg = r"\d{2,4}?"
# print(re.findall(reg, s))

# s = "Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0, float"
# reg = r"\w+\s*=\s*\d[.\w]*"
# reg = r"int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*"
# reg = r"(?:int|float)\s*=\s*\d[.\w]*"
# reg = r"(int|float)\s*=\s*\d[.\w]*"
# print(re.findall(reg, s))
# print(re.search(reg, s))

# (?: ....) - группирующая скобка не является сохраняющей



# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# s = "01-12-2024"
# reg = "(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# # print(re.findall(reg, s))
# # print(re.search(reg, s).group())
# # print(m[0])
# # print(m[1])
# # print(m[2])
# # print(m[3])
# print(re.search(reg, s).group())
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))
# print(re.search(reg, s).group(3))




# text = """
# Самара
# Москва
# Тверь
# Цфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))


# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."  # 23.10.2024  24.10.2024
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))


# s = "yandex.com and yandex.ru"
# reg = r"([a-z0-9-]{2,}\.[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))  #


# Рекурсия

# def elevator(n):  # 0
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)  # 1
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)



# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):  # 2, 10
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # convert[15] = 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] = 'E'
#
#
# print(to_str(254, 10))  # to_str(254, 16) => FE





