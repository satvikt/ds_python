from collections import deque

def shortest_path(graph, a, b):
    def get_neighbors(node):
        return graph[node]
    def bfs(root, target):
        queue = deque()
        queue.append(root)
        visited = set()
        visited.add(root)
        level = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                neighbors = get_neighbors(node)

                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            level += 1
    return bfs(a, b)

if __name__ == "__main__":
    graph= {i: list(map(int, input().split())) for i in range(int(input()))}
    a = int(input())
    b = int(input())

    print(shortest_path(graph, a, b))