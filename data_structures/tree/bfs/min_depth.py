from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    min_depth = 0
    while queue:
        level_size = len(queue)
        current_level = []
        min_depth += 1
        for i in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if not node.left and not node.right:
                return min_depth

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def main():
    root = TreeNode(12)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(10)
    # root.right.left = TreeNode(20)
    # root.right.left.right = TreeNode(17)
    # root = TreeNode(12)
    # root.left = TreeNode(7)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(9)
    # root.right.left = TreeNode(10)
    # root.right.left.left = TreeNode(20)
    # root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()