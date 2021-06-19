from data_structures.Graph import Graph
from data_structures.MyQueue import MyQueue


def bfs_helper(g, source, visited):
    result = ""

    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True

    while not queue.is_empty():
        curr_node = queue.dequeue()
        result += str(curr_node)

        temp = g.array[curr_node].head_node

        while temp:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
            else:
                # print("Graph has cycle")
                return True
            temp = temp.next_element

    return False


def bfs(g, source):
    if g.vertices == 0:
        return
    num_of_vertices = g.vertices

    visited = []

    for i in range(1,num_of_vertices+1):
        visited.append(False)

    result = bfs_helper(g, source, visited)

    return result

if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(3,6)
    # g.add_edge(2,1)
    g.add_edge(2,5)
    g.add_edge(2,4)

    print(bfs(g, 1))