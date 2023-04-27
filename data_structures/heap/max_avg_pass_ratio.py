import heapq

def maxAverageRatio(classes, extra_stud):
    h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
    heapq.heapify(h)
    while extra_stud:
        v, a, b = heapq.heappop(h)
        a, b = a + 1, b + 1
        heapq.heappush(h, (-(a + 1) / (b + 1) + a / b, a, b))
        extra_stud -= 1
    return sum(a / b for v, a, b in h) / len(h)


if __name__ == "__main__":
    classes = [[2,4],[3,9],[4,5],[2,10]]
    extraStudents = 4
    print(maxAverageRatio(classes, extraStudents))
