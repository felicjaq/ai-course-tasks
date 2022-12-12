import numpy as np

x = int(input())
y = int(input())

if x > y:
    a = (x - y) * np.random.random((3, 3)) + y
    print(a)
else:
    print('X должен быть больше Y :)')


