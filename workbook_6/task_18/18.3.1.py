def qZ(x, y):
    return (x - 3 * y - 3) / (x ** 2 + 2 * y ** 2 + 1)


def qSumZ(Z):
    return sum(Z)


def exchangeScheme(oldX, oldY, sortdID):
    X = [0 for i in range(4)]
    Y = [0 for i in range(4)]

    X[2] = oldX[sortdID[2]]
    X[3] = oldX[sortdID[2]]
    X[0] = oldX[sortdID[0]]
    X[1] = oldX[sortdID[1]]

    Y[0] = oldY[sortdID[2]]
    Y[1] = oldY[sortdID[2]]
    Y[2] = oldY[sortdID[0]]
    Y[3] = oldY[sortdID[1]]

    return X, Y


def sorting(Z):
    sortedID = sorted(range(len(Z)), key=lambda k: Z[k])
    return sortedID


def evoStep(X, Y, Z):
    _, minId = min((value, id) for (id, value) in enumerate(Z))
    X = X[:]
    Y = Y[:]
    Z = Z[:]

    X.pop(minId)
    Y.pop(minId)
    Z.pop(minId)

    return X, Y, Z


def evoSteps(X, Y):
    results = []

    for i in range(4):
        arrZ = [qZ(x, Y[i]) for i, x in enumerate(X)]
        X, Y, Z = evoStep(X, Y, arrZ)
        X, Y = exchangeScheme(X, Y, sorting(Z))
        results.append([X, Y, qSumZ(arrZ), arrZ])

    return X, Y, results


X = [-5, -3, -2, -1]
Y = [-1, -2, 0, 1]

results = evoSteps(X, Y)

for i in range(len(results[2])):
    print(f'max_{i + 1}_step: {results[2][i][2]}')

qualityArrZ = []
for i in range(len(results[2])):
    qualityArrZ += results[2][i][3]

print(f'max Z: {max(qualityArrZ)}')