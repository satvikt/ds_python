import math


class ArrayReader(object):
    def __init__(self, arr):
        self.arr = list(sorted(arr))

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def binary_search(reader, start, end, key):
    while start <= end:
        mid = start + (end - start)//2
        mid_element = reader.get(mid)
        if key > mid_element:
            start = mid + 1
        elif key < mid_element:
            end = mid - 1
        else:
            return mid
    return -1

def search_in_infinite_array(reader, key):
    start = 0
    end = 1

    while reader.get(end) < key:
        new_start = end + 1
        end = end + (end - start + 1)*2
        start = new_start

    return binary_search(reader, start, end, key)


def main():
    reader = ArrayReader([1, 3, 8, 10, 15, 4, 8, 66, 23, 77, 48, 9, 47])
    print(search_in_infinite_array(reader, 15))
    # print(search_in_infinite_array(reader, 200))

main()