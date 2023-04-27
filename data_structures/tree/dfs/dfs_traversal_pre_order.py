class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_helper(root, output):
    if root:
        output.append(root.val)

        if root.left:
            dfs_helper(root.left, output)
        if root.right:
            dfs_helper(root.right, output)

    return output


def traverse(root):
    output = []

    return dfs_helper(root, output)




def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(22)
    root.left.left.left = TreeNode(88)
    root.left.left.right = TreeNode(55)

    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))

main()