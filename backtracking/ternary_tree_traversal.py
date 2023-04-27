class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def ternary_tree_paths(root):
    # dfs helper function
    def dfs(root, path, res):
        # exit condition, reached leaf node, append paths to results
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + root.val)
            return

        # dfs on each non-null child
        for child in root.children:
            if child is not None:
                path.append(root.val)
                dfs(child, path, res)
                path.pop()

    res = []
    if root: dfs(root, [], res)
    return res

if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val, [])
        for _ in range(3): cur.children.append(build_tree(nodes))
        return cur
    root = build_tree(iter(input().split()))
    paths = ternary_tree_paths(root)
    for path in sorted(paths): print(path)

    root = Node(1)
    root.children = [2, 4, 6]

