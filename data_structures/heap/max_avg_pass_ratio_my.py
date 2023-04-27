import heapq


def maxAverageRatio(classes, extraStudents):
    # arr = [(a/b - (a+1)/(b+1), a, b) for a,b in classes]
    arr = [(a/b, a, b) for a,b in classes]
    heapq.heapify(arr)
    while extraStudents:
        avg, a, b = heapq.heappop(arr)
        a, b = a+1, b+1
        heapq.heappush(arr, ((a/b - (a+1)/(b+1), a,b)))
        extraStudents -=1
    return sum(a/b for v,a,b in arr)/len(arr)


if __name__ == "__main__":
    classes = [[2,4],[3,9],[4,5],[2,10]]
    extraStudents = 4
    print(maxAverageRatio(classes, extraStudents))
