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


import re
s = input("Введите пароль: ")
reg = r"([a-zA-Z0-9_@-]{6,18}+)"
print(re.findall(reg, s))














