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




# # dz

math = {"Matvei", "Evgeniya", "Michail", "Maxim", "Natalia"}
physics = {"Maxim", "Matvei", "Alexandr"}
vseprizery = math | physics
print(vseprizery)
both = math & physics
print(both)
math = both
print(math)


