import random


class Warrior:

    def __init__(self, health):
        self.health = health

    def hit(self, target, target1):

        if target.health > 0:
            target.health -= 20

        if target1 == warrior1:
            target1 = "Warrior1"

        if target1 == warrior2:
            target1 = "warrior2"

        print(target1, " has attacked")
        print(target.health, "left")

        if target.health == 0:
            print(target1, "has won")


warrior1 = Warrior(100)
warrior2 = Warrior(100)
q = int(input("Enter 1 to attack. Enter 2 to stop program:"))

while q != 2:
    if q == 1:
        j = random.randint(1, 3)
        if j % 2 == 0:
            warrior1.hit(warrior2, warrior1)
            q = int(input("Enter 1 to let some warrior attack:"))
        else:
            warrior2.hit(warrior1, warrior2)
            q = int(input("Enter 1 to let some warrior attack:"))
    else:
        print("Wrong input.")
        break
