import matplotlib.pyplot as plt
import numpy as np

marks = ["Неуд.", "Удовл.", "Хор.", "Отл."]

data = [3, 7, 8, 4]
fig = plt.figure(figsize=(10, 7))

plt.pie(data, labels=marks)
plt.grid()
plt.show()

plt.scatter(marks, data)
plt.grid()
plt.show()
