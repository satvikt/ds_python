def dfs(root, target):
    if root == None:
        return None


    left = dfs(root.left, target)
    if left is not None:
        return left

    # at this point, we know left is null, and right could be null or non-null
    # we return right child's recursive call result directly because
    # - if it's non-null we should return it
    # - if it's null, then both left and right are null, we want to return null

    return dfs(root.right, target)

"""
Short FOrm
----------
def dfs(root, target):
    if root == None:
        return None
    if root.val == target:
        return root.val

    return dfs(root.left, target) or dfs(root.right, target)
Notes

1. Uses

Time:

Since this algorithm traverses the whole graph once, its time complexity is O(V + E).
"""