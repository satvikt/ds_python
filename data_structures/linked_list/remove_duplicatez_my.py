class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def print_ll(head):
    while head:
        print(head.data, end= " ")
        head = head.next


def remove_duplicates(head):
    curr = head
    prev = head

    visited = set()

    if not head or not curr.next:
        return

    while curr:
        if curr.data in visited:
            prev.next = curr.next
            curr = curr.next
            continue

        visited.add(curr.data)
        prev = curr
        curr = curr.next

    return head
if __name__ == "__main__":
    head = Node(2)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(5)


    print_ll(head)
    n = 8
    print()
    print_ll(remove_duplicates(head))