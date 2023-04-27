# Binary Tree Node
""" utility that allocates a newNode
with the given key """
class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

numOfPaths = 0

def pathSum( root, target):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    # define global return var

    # 1st layer DFS to go through each node
    dfs(root, target)
    # return result
    return numOfPaths

# define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
def dfs( node, target):
    # exit condition
    if node is None:
        return
        # dfs break down
    test(node, target) # you can move the line to any order, here is pre-order
    dfs(node.left, target)
    dfs(node.right, target)

# define: for a given node, DFS to find any path that sum == target, if find numOfPaths += 1
def test( node, target):
    global numOfPaths
    # exit condition
    if node is None:
        return
    node_val = node.val
    if node_val == target:
        numOfPaths += 1

    # test break down
    new_target = target- node_val
    test(node.left, new_target)
    test(node.right, new_target)

# Driver Code
if __name__ == '__main__':

    root = newNode(1)
    root.left = newNode(3)
    root.left.left = newNode(2)
    root.left.right = newNode(1)
    root.left.right.left = newNode(1)
    root.right = newNode(-1)
    root.right.left = newNode(4)
    root.right.left.left = newNode(1)
    root.right.left.right = newNode(2)
    root.right.right = newNode(5)
    root.right.right.right = newNode(2)
    # root.right.right.right.right = newNode(3)

    k = 5
    pathSum(root, k)
    print(numOfPaths)