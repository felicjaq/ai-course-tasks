import numpy as np

m, n = int(input()), int(input())

matrix = np.arange(m * n).reshape(m, n)
print(matrix)

if m == n:
    print('Форма этой матрицы - квадратная!')
else:
    print('Форма этой матрицы - прямоугольная! ')

print("Размер матрицы равен", np.sqrt(m ** 2 + n ** 2))
print("Размерность матрицы равна", m, 'x', n)
