class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) > 1:
            # get the max (0th) element
            max = self.heap[0]

            # assign the final element to the 0th
            self.heap[0] = self.heap[-1]

            # delete the final element
            del self.heap[-1]

            # call max_heapify on
            self.__maxHeapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    def __percolateUp(self, index):
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.heap[parent] > self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolateUp(parent)



    def __maxHeapify(self, index):
        left = index * 2 + 1
        right = (index * 2) + 2
        largest = index
        # check if left child exists and is less than smallest
        if len(self.heap) > left and self.heap[left] > self.leap[largest]:
            largest= left
        # check if right child exists and is less than smallest
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        # check if current index is not the smallest
        if largest != index:
            # swap current index value with smallest
            tmp = self.heap[smallest]
            heap[smallest] = heap[index]
            heap[index] = tmp
            # minHeapify the new node
            minHeapify(heap, smallest)
        return heap


if __name__ == "__main__":
    heap = MaxHeap()