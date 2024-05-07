class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w + self.h)



if __name__ == "__main__":
    r1 = Rectangle(1, 2)
    r2 = Rectangle(3, 4)
    print(f"Perimetr prymoug: {r1.get_perimetr()}")


# print(__name__)

__author__ = "Admin"
if __name__ == '__main__':
     print(f"Module {__name__} (author: {__author__})")