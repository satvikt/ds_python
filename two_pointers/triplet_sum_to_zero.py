def sum_pair(arr, start, target_sum, final):
    end = len(arr) - 1

    while start < end:
        curr_sum = arr[start] + arr[end]

        if curr_sum < target_sum:
            start += 1
        elif curr_sum > target_sum:
            end -= 1
        else:
            final.append([arr[start], arr[end]])
            start += 1
            end -= 1

            while start < end and arr[start] == arr[start - 1]:
                start += 1
            while start < end and arr[end] == arr[end + 1]:
                end -= 1


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum

def triplet_sum_to_zero(arr, sum):
    arr.sort()
    final = []
    for i in range(len(arr)):
        if arr[i-1] == arr[i]:
            continue
        sum_pair(arr,i+1, arr[i], final)

    return final


def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
            continue
        search_pair(arr, -arr[i], i+1, triplets)

    return triplets


if __name__ == '__main__':
    A = [-2, -1, -1, 0, 2, 3]
    sum = 4
    print(search_triplets(A))
    # print(make_squares(A))
    # print(triplet_sum_to_zero(A, sum))