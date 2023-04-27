class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def has_path(root, target):
    if root == None:
        return None

    if root.val == target and root.right is None and root.left is None:
        return True

    return has_path(root.left, target - root.val)


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
