def reverse_list(arr):
    if len(arr) == 1:
        return arr
    else:
        return reverse_list(arr[1:]) + [arr[0]]


if __name__ == "__main__":
    print(reverse_list([1,2,3,4]))