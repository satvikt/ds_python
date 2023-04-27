class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_ll(head):
    while head:
        print(head.val, end= " ")
        head = head.next


def find_length(head):
    count = 0
    while head:
        head = head.next
        count += 1
    return count


def adjust_rotations(n, length):
    if n> length:
        n = n - length
    elif n < 0:
        while n < 0:
            n = n + length
    return n


def rotate_list(head, n):
    if head is None:
        return

    length = find_length(head)

    n = adjust_rotations(n, length)

    rotations = length - n - 1

    temp = head

    while rotations > 0:
        temp = temp.next
        rotations -= 1

    new_head = temp.next

    temp.next = None

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
    head.next.next.next.next.next = Node(6)


    print_ll(head)
    n = 8
    print()
    print_ll(rotate_list(head, n))