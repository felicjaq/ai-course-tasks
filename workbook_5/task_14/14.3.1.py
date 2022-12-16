import numpy as np


class Trigonometry:

    def sin(self):
        print(np.sin(x))

    def cos(self):
        print(np.cos(x))

    def tan(self):
        print(np.tan(x))

    def arcsin(self):
        if (x > -1) and (x < 1):
            print(np.arcsin(x))
        else:
            print("\033[31mERROR 002: WRONG INPUT. "
                  "The arcsinus value must be in the range from -1 to 1! \033[0m")

    def arccos(self):
        if (x > -1) and (x < 1):
            print(np.arcsin(x))
        else:
            print("\033[31mERROR 003: WRONG INPUT. "
                  "The arccosinus value must be in the range from -1 to 1! \033[0m")

    def arctan(self):
        print(np.arctan(x))

    def radian(self):
        print(np.radians(x))


print("Welcome to the best trigonometric calculator!")

x = float(input("Enter yor number:  "))
obj = Trigonometry()

print("List of operations:  ")

choice = 1
while choice != 0:
    print("1 - Sinus")
    print("2 - Cosinus")
    print("3 - Tangens")
    print("4 - Arcsinus")
    print("5 - Arccosinus")
    print("6 - Artangens")
    print("7 - Conversion from degrees to radians \n")
    choice = int(input("Enter operation's number:  "))

    if choice == 1:
        print(obj.sin())
    elif choice == 2:
        print(obj.cos())
    elif choice == 3:
        print(obj.tan())
    elif choice == 4:
        print(obj.arcsin())
    elif choice == 5:
        print(obj.arccos())
    elif choice == 6:
        print(obj.arctan())
    elif choice == 7:
        print(obj.radian())
    elif choice == 404:
        exit()
    else:
        print("\033[31mERROR 001: WRONG INPUT. "
              "The number must be in the range from 1 to 7! \033[0m")
