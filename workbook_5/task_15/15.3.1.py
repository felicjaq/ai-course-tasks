class Tree:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


t = Tree('a', Tree('b', Tree('d'), Tree('e')), Tree('c', None, Tree('f')))

print("Root is:", t.name)
print("Left tree:", t.left.name, t.left.left.name, t.left.right.name)
print("Right tree:", t.right.name, t.right.right.name)
