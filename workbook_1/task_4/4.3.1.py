import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(1, 8)
names = ["1 знач.", "2 знач.", "3 знач.", "4 знач.", "5 знач.", "6 знач.", "7 знач.", "8 знач."]

median_value = np.median(a)
average_value = np.mean(a)
print(a, "\n", 'Медианное значение: ', median_value, '\n', 'Среднее значение: ', average_value)

if median_value > average_value:
    print('Медианное значение больше среднего.')
elif median_value < average_value:
    print('Медианная значение ниже среднего.')
else:
    print('Медианная значение равно среднему.')

plt.scatter(names, a)
plt.grid()
plt.show()

