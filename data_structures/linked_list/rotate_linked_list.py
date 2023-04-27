class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_ll(node):
    while node:
        print(node.val, end=" ")
        node = node.next


def find_length(head):
    count = 0
    if head is None:
        return
    while head is not None:
        count += 1
        head = head.next
    return count


def adjust_rotations_needed(n, length):
    # if n>0:
    #     n = n % length
    # else:
    if n > length:
        n = n - length
    elif n < 0:
        n = n + length
    return n


def rotate_list(head, n):
    if head is None or n == 0:
        return

    length = find_length(head)

    # note that n will be the number of nodes to be shifted from the right
    n = adjust_rotations_needed(n, length)

    # this will be give the pos
    rotations_needed = length - n -1

    temp = head
    while rotations_needed > 0:
        temp = temp.next
        rotations_needed -= 1
    #
    # if n == 0:
    #     return head
    #
    #
    new_node = temp.next
    temp.next = None

    temp = new_node

    while temp.next:
        temp = temp.next

    temp.next = head
    return new_node





if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)


    print_ll(head)
    print()
    print_ll(rotate_list(head, 7))