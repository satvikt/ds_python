def dfs_on_graph(graph):
    output = []
    def get_neighbours(node):
        return graph[node]
    def dfs(node, visited):
        output.append(node)
        visited.add(node)
        neighbours = get_neighbours(node)
        for neighbor in neighbours:
            if neighbor in visited:
                continue
            dfs(neighbor, visited)
        return output
    return dfs(0, set())


if __name__ == "__main__":
    graph = {i: list(map(int, input().split())) for i in range(int(input()))}
    print(dfs_on_graph(graph))