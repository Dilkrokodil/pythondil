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

name = input("Введите ФИО: ")
one = name[:name.find(" ")]
a = name.split()
print(one + " " + a[1][0] + "." + a[2][0] + ".")




