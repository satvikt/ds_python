from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, root):
        visited = set()
        # output = []
        return self.DFSUtil(root, visited, [])

    def DFSUtil(self, root, visited, output):
        visited.add(root)
        output.append(root)

        for neighbour in self.graph[root]:
            if neighbour in visited:
                continue
            self.DFSUtil(neighbour, visited, output)

        return output


if __name__ == "__main__":
    # Create a graph given
    # in the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    print(g.DFS(2))