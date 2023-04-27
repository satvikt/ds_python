class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths_recursive(node, required_sum, currPath, allPaths):
    if node is None:
        return

    currPath.append(node.val)

    if node.val == required_sum and node.left == None and node.right == None:
        allPaths.append(currPath)

    else:
        find_paths_recursive(node.left, required_sum - node.val, currPath, allPaths)
        find_paths_recursive(node.right, required_sum - node.val, currPath, allPaths)

    del currPath[-1]




def find_paths(root, required_sum):
    allPaths = []
    find_paths_recursive(root, required_sum, [], allPaths)
    return allPaths



def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
          ": " + str(find_paths(root, required_sum)))


main()