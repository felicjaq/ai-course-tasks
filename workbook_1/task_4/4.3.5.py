import matplotlib.pyplot as plt
import numpy as np

print('Введите две переменные:')

x, y = float(input()), float(input())
print('x = ', x, 'y = ', y)

print('Выберите номер нобходимой операции:', '\n',
      '1) x + y', '\n',
      '2) x - y', '\n',
      '3) x * y', '\n',
      '4) x / y', '\n',
      '5) e^(x+y)', '\n',
      '6) sin(x + y)', '\n',
      '7) cos(x + y)', '\n',
      '8) x^y', '\n')

k = int(input())
while k <= 0 or k > 8:
    print('Некорректный номер! попробуйте еще раз.')
    k = int(input())

if k == 1:
    print(x, '+', y, '=', x + y)
elif k == 2:
    print(x, '-', y, '=', x - y)
elif k == 3:
    print(x, '*', y, '=', x * y)
elif k == 4:
    print(x, '/', y, '=', x / y)
elif k == 5:
    print('e^(', x, '+', y, ') =', np.exp(x + y))
elif k == 6:
    print('sin(', x, '+', y, ') =', np.sin(x + y))
elif k == 7:
    print('cos(', x, '+', y, ') =', np.cos(x + y))
else:
    print(x, '^', y, '=', x ** y)
