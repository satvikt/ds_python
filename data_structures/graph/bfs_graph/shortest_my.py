from collections import deque


def get_neighbours(node):
    return graph[node]


def length_of_shortest_path(graph, a, b):
    def bfs(node, target):
        queue = deque()
        queue.append(node)
        visited = set()
        visited.add(node)
        level = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                neighbours = get_neighbours(node)

                for nei in neighbours:
                    if nei in visited:
                        continue
                    queue.append(nei)
                    visited.add(nei)

            level += 1

    return bfs(a,b)
if __name__ == '__main__':
    # graph = {None}
    # for i in range(int(input())):
    #     graph += {i: list(map(int, input().split()))}
    graph = {i: list(map(int, input().split())) for i in range(int(input()))}
    a = int(input())
    b = int(input())
    res = length_of_shortest_path(graph, a, b)
    print(res)