import matplotlib.pyplot as plt
import numpy as np

print("Enter the coordinates of 1st point by oX, oY, oZ axes:")
x1, y1, z1 = int(input()), int(input()), int(input())

print("Enter the coordinates of 2nd point by oX, oY, oZ axes:")
x2, y2, z2 = int(input()), int(input()), int(input())

print("Enter the coordinates of 3rd point by oX, oY, oZ axes:")
x3, y3, z3 = int(input()), int(input()), int(input())

print("Enter the coordinates of 4th point by oX, oY, oZ axes:")
x4, y4, z4 = int(input()), int(input()), int(input())

point1 = np.array([x1, y1, z1])
point2 = np.array([x2, y2, z2])
point3 = np.array([x3, y3, z3])
point4 = np.array([x4, y4, z4])

points = [point1, point2, point3, point4]

i = 1
for point in points:
    print("Coordinates of the", i, "point is:", point)
    i += 1

print("")

i = -1
k = 1
for point in points:
    if k < 4:
        print("Euclidean distance between", k, "and", k + 1, "point is equal to",
              np.linalg.norm(points[i] - points[i + 1]))
        k += 1
    elif k == 4:
        print("Euclidean distance between", 4, "and", 1, "point is equal to",
              np.linalg.norm(points[i] - points[i + 1]))
    else:
        print('ERROR 001')
    i += 1

print("")

i = -1
k = 1
for point in points:
    if k < 4:
        print("Qadro-euclidean distance between", k, "and", k + 1, "point is equal to",
              (np.linalg.norm(points[i] - points[i + 1])) ** 2)
        k += 1
    elif k == 4:
        print("Quadro-euclidean distance between", 4, "and", 1, "point is equal to",
              (np.linalg.norm(points[i] - points[i + 1])) ** 2)
    else:
        print('ERROR 002')
    i += 1

print("")

i = -1
k = 1
for point in points:
    if k < 4:
        print("Chebyshev distance distance between", k, "and", k + 1, "point is equal to",
              np.linalg.norm(points[i] - points[i + 1], ord=np.inf))
        k += 1
    elif k == 4:
        print("Chebyshev distance distance between", 4, "and", 1, "point is equal to",
              np.linalg.norm(points[i] - points[i + 1], ord=np.inf))
    else:
        print('ERROR 003')
    i += 1

print("")

i = -1
k = 1
for point in points:
    if k < 4:
        print("Hemming distance distance between", k, "and", k + 1, "point is equal to",
              np.linalg.norm(points[i] - points[i + 1], ord=1))
        k += 1
    elif k == 4:
        print("Hemming distance distance between", 4, "and", 1, "point is equal to",
              np.linalg.norm(points[i] - points[i + 1], ord=1))
    else:
        print('ERROR 004')
    i += 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x1, y1, z1)
ax.scatter(x2, y2, z2)
ax.scatter(x3, y3, z3)
ax.scatter(x4, y4, z4)

plt.show()
