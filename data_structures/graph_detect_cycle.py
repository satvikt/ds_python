"""
My notes - Uses DFS (Goes till the full depth of a path, before backtracking and continuing with the next child of the immediate ancestor)

Description
-------------
For each node, we start a recursive call with detect_cycle_rec. The function maintains a stack (not to be confused with the stack data structure) of nodes called rec_node_stack along with a visited list.

The vertices that have been traversed in the current recursion are added to rec_node_stack and visited keeps a record of all the nodes that have been traversed regardless of the recursive call.

For a cycle to occur, we must reach a node that was already present in the recursion stack. If the recursion ends and no such node is found, the stack is reset again and the next iteration of detect_cycle starts.

Complexity
---------
O(V+E), which we already know is the complexity of traversing the adjacency list that represents our graph.

"""

from data_structures.Graph import Graph


def detect_cycle(g):
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.vertices
    # rec_node_stack keeps track of the nodes which are part of
    # the current recursive call
    rec_node_stack = [False] * g.vertices
    for node in range(g.vertices):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True
    return False

def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in recursion stack. Cycle found.
    if rec_node_stack[node]:
        return True
    # It has been visited before this recursion
    if visited[node]:
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True
    head_node = g.array[node].head_node
    while head_node is not None:
        # Pick adjacent node and call it recursively
        adjacent = head_node.data
        # If the node is visited again in the same recursion => Cycle found
        if detect_cycle_rec(g, adjacent, visited, rec_node_stack):
            return True
        head_node = head_node.next_element
    # remove the node from the recursive call
    """
    needed to reset the stack in a "directed" graph
    Eg. If a path follows 1 > 3 > 4 > 5 reaching a dead end here (no cycle) then 5
    must be reset for the next path which might be 
    3 > 6
    3 > 2 > 5 (not a cycle in case of directed graph)
    Otherwise the condition on line 30 will hold true (wrongly)
     
    """
    rec_node_stack[node] = False
    return False

if __name__ == "__main__" :
    g1 = Graph(6)
    # g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 4)
    g1.add_edge(4, 5)
    g1.add_edge(1, 5)

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    # print(detect_cycle(g2))