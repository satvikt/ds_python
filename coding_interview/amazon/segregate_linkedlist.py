"""
Given a singly LL of random negative, positive and zeroes, rearrange the list in the order negatives -> zeroes > positives
	1. Caveat - Order should be maintained

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_ll(node):
    while node:
        print(node.val)
        node = node.next


def rearrange(head):
    left = None
    mid = None
    right = None

    while head:
        if head.val < 0:
            left = head
            left = left.next
        elif head.val == 0:
            mid = head
            mid = mid.next
        else:
            right = head
            right = right.next
        head = head.next

    if neg:




if __name__ == "__main__":
    head = Node(-2)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(-1)
    head.next.next.next.next = Node(0)

    print_ll(rearrange(head))


"""
1. What if there are no negative nodes
2. What if the head part does not start with a negative numner 
"""