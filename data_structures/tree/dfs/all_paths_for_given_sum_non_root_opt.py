class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

result = 0
def pathSum( root, target):
    # define global result and path
    global result
    cache = {0:1}

    # recursive to get result
    dfs(root, target, 0, cache)

    # return result
    return result

def dfs(root, target, currPathSum, cache):
    global result
    # exit condition
    if root is None:
        return
        # calculate currPathSum and required oldPathSum
    currPathSum += root.val
    oldPathSum = currPathSum - target
    # update result and cache
    result += cache.get(oldPathSum, 0)
    cache[currPathSum] = cache.get(currPathSum, 0) + 1

    # dfs breakdown
    dfs(root.left, target, currPathSum, cache)
    dfs(root.right, target, currPathSum, cache)
    # when move to a different branch, the currPathSum is no longer available, hence remove one. 
    cache[currPathSum] -= 1


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
    print(pathSum(root, k))
    # print(numOfPaths)