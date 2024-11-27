class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def maxValue(node):
    """Returns the maximum value in the tree rooted at `node`."""
    if node is None:
        return float('-inf')
    return max(node.data, maxValue(node.left), maxValue(node.right))

def minValue(node):
    """Returns the minimum value in the tree rooted at `node`."""
    if node is None:
        return float('inf')
    return min(node.data, minValue(node.left), minValue(node.right))

def isBST(node):
    """Checks whether a binary tree is a BST."""
    if node is None:
        return True
    if node.left and maxValue(node.left) >= node.data:
        return False
    if node.right and minValue(node.right) <= node.data:
        return False
    return isBST(node.left) and isBST(node.right)

def insert(node, value):
    """Inserts a new value into the BST."""
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

if __name__ == "__main__":
    root = None
    print("Enter the values for the nodes of the binary tree (enter 'done' to finish):")

    while True:
        value = input("Enter a value: ")
        if value.lower() == 'done':
            break
        try:
            value = int(value)
            root = insert(root, value)
        except ValueError:
            print("Please enter a valid integer.")

    if isBST(root):
        print("The binary tree is a BST.")
    else:
        print("The binary tree is not a BST.")
