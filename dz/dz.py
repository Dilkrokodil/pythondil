# def plosh(a, b, c):
#
#     def inner():
#         s = 2*(a*b + b*c + a*c)
#         print(s)
#     return inner()
#
#
# plosh(2, 4, 6)



s = 1


def plosh(a, b, c):
    def inner():
        global s
        s = 2 * (a * b + b * c + a * c)
        print(s)

    return inner()


plosh(2, 4, 6)