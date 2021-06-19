from data_structures.Graph import Graph

def detect_cycle_rec(g, node, visited, rec_stack):

    # TODO - Using the stack DS
    if rec_stack[node]:
        return True

    if visited[node]:
        return False

    visited[node] = True
    rec_stack[node] = True

    curr_node = g.array[node].head_node

    while curr_node:
        data = curr_node.data

        if detect_cycle_rec(g, data, visited, rec_stack):
            return True
        curr_node = curr_node.next_element
    rec_stack[node] = False
    return False


def detect_cycle(g):

    rec_stack = [False] * g.vertices
    visited = [False] * g.vertices

    for node in range(g.vertices):
        if detect_cycle_rec(g, node, visited, rec_stack):
            return True

    return False

if __name__ == "__main__" :
    g1 = Graph(6)
    # g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 4)
    g1.add_edge(4, 5)
    g1.add_edge(5, 1)

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    print(detect_cycle(g2))