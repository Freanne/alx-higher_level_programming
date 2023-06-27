#!/us/bin/python
class Square:
    def __init__(self, __size):
        self.__size = __size

    if (type(__size) != int):
        try:
            raise TypeError
        except:
            print("__size must be an integer")

    if (__size < int):
        try:
            raise ValueError
        except:
            print("__size must be >= 0")
