def search_next_letter(arr, key):
    start = 0
    end = len(arr) -1
    # mid = 0
    if key > arr[len(arr) - 1]:
        return arr[0]

    while start <=end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return arr[start % len(arr)]




def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    # print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()