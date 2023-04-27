class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_ll(node):
    while node:
        print(node.val, end=" ")
        node = node.next
def find_length(head):
    length = 0

    while head:
        length += 1
        head = head.next

    return length

def adjust_rotations_needed(n, length):
    # If n is positive then number of rotations performed is from right side
    # and if n is negative then number of rotations performed from left side
    # Let's optimize the number of rotations.
    # Handle case if 'n' is a negative number.
    n = n % length

    if n < 0:
        n = n + length

    return n

def rotate_list(head, n):

    if head is None or n is 0:
        return

    # find length of the linked list
    length = find_length(head)

    # Let's optimize the number of rotations.
    # Handle case if 'n' is a negative number.

    # If n (number of rotations required) is bigger than
    # length of linked list or if n is negative then
    # we need to adjust total number of rotations needed
    n = adjust_rotations_needed(n, length)

    if n == 0:
        return head

    # Find the start of rotated list.
    # If we have 1, 2, 3, 4, 5 where n = 2,
    # 4 is the start of rotated list.
    rotations_count = length - n - 1
    temp = head

    while rotations_count > 0:
        rotations_count -= 1
        temp = temp.next

    # After the above loop temp will be pointing
    # to one node prior to rotation point
    new_head = temp.next

    # Set new end of list.
    temp.next = None

    # Iterate to the end of list and
    # link that to original head.
    temp = new_head
    while temp.next:
        temp = temp.next

    temp.next = head

    return new_head

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print_ll(head)
    print()
    print_ll(rotate_list(head, 3))