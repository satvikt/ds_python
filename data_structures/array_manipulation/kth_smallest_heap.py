import heapq

if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    heapq.heapify(arr)
    print("smallest ", heapq.heappop(arr))
    print("2nd smallest", heapq.heappop(arr))
    print("3rd smallest", heapq.heappop(arr))
    print("Heap afterwars", arr)