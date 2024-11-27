class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def is_complete_binary_tree(root):
    """Check if the binary tree is complete."""
    if not root:
        return True

    queue = [root]
    found_empty = False

    while queue:
        current = queue.pop(0)

        if current:
            if found_empty:
                return False
            queue.append(current.left)
            queue.append(current.right)
        else:
            found_empty = True

    return True

def build_tree():
    """Build a tree from user input."""
    nodes = input("Enter elements separated by spaces (use 'None' for missing nodes): ").split()
    nodes = [None if val == 'None' else int(val) for val in nodes]

    if not nodes or nodes[0] is None:
        return None

    root = Node(nodes[0])
    queue = [root]
    i = 1

    while i < len(nodes):
        current = queue.pop(0)
        
        if i < len(nodes) and nodes[i] is not None:
            current.left = Node(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = Node(nodes[i])
            queue.append(current.right)
        i += 1

    return root

# Main Program
root = build_tree()
if is_complete_binary_tree(root):
    print("The binary tree is complete.")
else:
    print("The binary tree is not complete.")
