from collections import deque
from typing import Dict, List
def length_of_shortest_path(graph: Dict[int, List[int]], a: int, b: int) -> int:

    def get_neighbors(node):
        return graph[node]
    def bfs(root, target):
        queue = deque([root])
        visited = set()
        # visited.add(root)
        level = 0
        while len(queue) > 0:
            n = len(queue) # get # of nodes in the current level
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
if __name__ == '__main__':
    # graph = {None}
    # for i in range(int(input())):
    #     graph += {i: list(map(int, input().split()))}
    graph = {i: list(map(int, input().split())) for i in range(int(input()))}
    a = int(input())
    b = int(input())
    res = length_of_shortest_path(graph, a, b)
    print(res)