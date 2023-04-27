def cyclic_sort(nums):
    for i in range(len(nums)):
        # print(i)
        # print(arr[i])
        # print(arr[arr[i]])
        while i < len(nums):
            j = nums[i]
            if j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1
        print("------")
    return nums


def main():
    print(cyclic_sort([0, 1, 6, 4, 2]))
    # print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    # print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()