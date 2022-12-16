class Tree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                elif self.data < data:
                    if self.right is None:
                        self.right = Tree(data)
                    else:
                        self.right.insert(data)
                else:
                    self.left.insert(data)

        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()


root = Tree(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()

root = Tree(10)
root.printTree()
