import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(0, 0, 0)
ax.scatter(3, 3, 3)

plt.show()
