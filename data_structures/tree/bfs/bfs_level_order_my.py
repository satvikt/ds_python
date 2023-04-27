from collections import deque


class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root):
    result = []
    if root == None:
        return None
    queue = deque()
    queue.append(root)
    correct = True
    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if correct:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(list(current_level))

        correct = not correct
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))

main()