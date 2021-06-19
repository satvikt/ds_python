from data_structures.Graph import Graph
from data_structures.Stack import MyStack


def dfs_helper(g, visited, source):

    stack = MyStack()
    stack.push(source)
    visited[source] = True

    result = ""

    while not stack.is_empty():
        node = stack.pop()
        result += str(node)

        temp = g.array[node].head_node

        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                visited[temp.data] = True
            else:
                return "Graph has cycle"
            temp = temp.next_element

    return result


def dfs(g, source):
    if g.vertices == 0:
        return

    visited = []
    # result = ""
    for i in range(1,g.vertices+1):
        visited.append(False)

    result = dfs_helper(g, visited, source)

    return result


if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(3,6)
    g.add_edge(2,5)
    g.add_edge(2,4)

    print(dfs(g, 1))