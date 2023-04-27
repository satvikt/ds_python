import math


def binary_search(arr, start, end, key):
    while start <= end:
        mid = start + (end-start)//2
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1

def search_in_infinite_array(reader, key):
    start = 0
    end = 1
    while key > reader.get(end):
        new_start = end + 1
        end = end + (end-start+1)*2
        start = new_start

    return binary_search(reader.arr, start, end, key)



class ArrayReader(object):
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]





if __name__ == "__main__":
    # reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    # print(search_in_infinite_array(reader, 16))
    # print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    # print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader.arr, 200))
    
