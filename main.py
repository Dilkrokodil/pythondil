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


d = {
    "John": {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694
    },
    "Tom": {
        "N": 4832,
        "S": 6786,
        "E": 4737,
        "W": 3612
    },
    "Anne": {
        "N": 5239,
        "S": 4802,
        "E": 5820,
        "W": 1859
    },
    "Fiona": {
        "N": 3904,
        "S": 3645,
        "E": 8821,
        "W": 2451
    }
}
for x in d:
    print(x)
    for y in d[x]:
        print(y, ": ", d[x][y])
imya = input("Имя: ")
region = input("Регион: ")
print(d[imya][region])
znach = input("Новое значение: ")
d[imya][region] = znach
print(d[imya])
