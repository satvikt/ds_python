class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def print_ll(head):
    while head:
        print(head.data, end= " ")
        head = head.next

def remove_duplicates(head):
    current_node = head
    prev_node = head
    # To store values of nodes which we already visited
    visited_nodes = set()
    # If List is not empty and there is more than 1 element in List
    if (head and current_node.next):
        while current_node:
            value = current_node.data
            if value in visited_nodes:
                # current_node is already in the HashSet
                # connect prev_node with current_node's next element
                # to remove it
                prev_node.next = current_node.next
                current_node = current_node.next
                continue
            # Visiting currentNode for first time
            visited_nodes.add(current_node.data)
            prev_node = current_nodeNN
            current_node = current_node.next

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