from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def binary_tree_min_depth(root: TreeNode) -> int:
    queue = deque([root]) # at least one element in the queue to kick start bfs
    depth = 0 # we start from -1 because popping root will add 1 depth
    while len(queue) > 0: # as long as there is element in the queue
        depth += 1
        n = len(queue) # number of nodes in current level
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            if node.left is None and node.right is None: # found leaf node, early return
                return depth
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
    return depth

def main():
    root = TreeNode(12)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(10)
    root.right.left = TreeNode(20)
    # root.right.left.right = TreeNode(17)
    # root = TreeNode(12)
    # root.left = TreeNode(7)
    # root.right = TreeNode(1)
    # root.left.left = TreeNode(9)
    # root.right.left = TreeNode(10)
    # root.right.left.left = TreeNode(20)
    # root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(binary_tree_min_depth(root)))


main()