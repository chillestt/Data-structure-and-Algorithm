class TreeNode:
    def __init__(self, val):
        self.val = val
        self.positions = []
        self.left = None
        self.right = None


def insert(root, val, position):
    if root is None:
        root = TreeNode(val)
        root.positions.append(position)
        return root
    else:
        if val < root.val:
            root.positions.append(position)
            root.left = insert(root.left, val, position)
        elif val > root.val:
            root.right = insert(root.right, val, position)
        else:
            root.positions.append(position)
        return root


def findMinPosition(n, a):
    root = None
    for i in range(n):
        root = insert(root, a[i], i + 1)

    if root:
        return root.positions
    else:
        return []

n = 5
a = [1, 2, 1, 2, 1]
result = findMinPosition(n, a)
print(result)
