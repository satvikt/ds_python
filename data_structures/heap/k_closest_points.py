import heapq, math
def k_closest_points(points, k):
    heap = []
    for pt in points:
        heapq.heappush(heap, (math.sqrt(pt[0]**2 + pt[1]**2), pt))

    res = []
    for _ in range(k):
        _, pt = heapq.heappop(heap)
        res.append(pt)

    return res

if __name__ == '__main__':
    points = []
    n = int(input())
    for _ in range(n):
        points.append(tuple(int(x) for x in input().strip().split()))
    k = int(input())
    res = k_closest_points(points, k)
    print('\n'.join('{} {}'.format(x[0], x[1]) for x in res))