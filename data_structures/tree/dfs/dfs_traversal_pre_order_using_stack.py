# Tree Node
class Node:

    def __init__(self, data = 0):
        self.data = data
        self.left = None
        self.right = None

# Iterative function to do Preorder traversal of the tree
def preorderIterative(root):

    if (root == None):
        return

    st = []

    # start from root node (set current node to root node)
    curr = root

    # run till stack is not empty or current is
    # not NULL
    while (len(st) or curr != None):

        # Print left children while exist
        # and keep appending right into the
        # stack.
        while (curr != None):

            print(curr.data, end = " ")

            if (curr.right != None):
                st.append(curr.right)

            curr = curr.left

        # We reach when curr is NULL, so We
        # take out a right child from stack
        if (len(st) > 0):
            curr = st[-1]
            st.pop()

# Driver Code

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.left.left = Node(70)
root.left.right = Node(50)
root.right.left = Node(60)
root.left.left.right = Node(80)

preorderIterative(root)

# This code is contributed by Arnab Kundu
