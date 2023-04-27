import heapq

if __name__ == "__main__":
    arr = [15, 16, 10, 9, 6, 7, 17]
    heapq._heapify_max(arr)
    max = heapq.nlargest()
