def dfs_on_graph(graph):
    output = []
    def get_neighbors(node):
        return graph[node]

    def dfs(root, visited):
        visited.add(root)
        output.append(root)
        for neighbor in get_neighbors(root):
            if neighbor in visited:
                continue
            dfs(neighbor, visited)
        return output

    dfs(0, set())

if __name__ == "__main__":
    graph= {i: list(map(int, input().split())) for i in range(int(input()))}

    print(dfs_on_graph(graph))