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


def sum(chisla):
    if not chisla:
        return 0
    count = 0
    if chisla[0] < 0:
            count += 1
    return sum(chisla[1:]) + count


print(sum(s))


# import os
#
# root = r'nested1'
# objs = os.listdir(root)
# print(objs)
#
# objs = list(map(lambda i: os.path.join(root, i), objs))
# print(objs)















