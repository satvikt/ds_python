import heapq

if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    print(arr)
    heapq._heapify_max(arr)
    print(arr)
    heapq.heappush(arr, 1)
    print(arr)