class Perceptron:

    def __init__(self, N):
        self.w = list()
        for i in range(N):
            self.w.append(0)

    def calc(self, x):
        res = 0
        for i in range(len(self.w)):
            res = res + self.w[i] * x[i]
        return res

    def sign(self, x):
        if self.calc(x) > 0:
            return 1
        else:
            return -1

    def learn(self, la, x, y):
        if y * self.calc(x) <= 0:
            for i in range(len(self.w)):
                self.w[i] = self.w[i] + la * y * x[i]

    def learning(self, la, T):
        for n in range(100):
            for t in T:
                self.learn(la, t[0], t[1])


perceptron = Perceptron(2)
la = 0.1

T = list()
T.append([[2, 1], 1])
T.append([[3, 2], 1])
T.append([[4, 1], 1])
T.append([[1, 2], -1])
T.append([[2, 3], -1])
T.append([[5, 7], -1])

perceptron.learning(la, T)
print(perceptron.w)

print(perceptron.sign([1.5, 2]))
print(perceptron.sign([3, 1.5]))
print(perceptron.sign([5, 1]))
print(perceptron.sign([5, 10]))
