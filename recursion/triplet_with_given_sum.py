# python program for above approach

array = [1, 4, 45, 6, 10, 8]
target = 22
n = len(array)


# The check function recursively checks all possible subsets of the array
# to see if any of them sum to the target value
def check(array, n, target, triplet):
    # If the target value has been reached and the length of the triplet is 3,
    # then a triplet with a sum of target has been found and is printed
    if target == 0 and len(triplet) == 3:
        print(triplet)
        return True

    # If there are no more elements in the array or the target value has gone negative,
    # then a triplet with a sum of target cannot be found
    if n == 0 or target < 0 or len(triplet) == 3:
        return False

    # Recursively check if target can be reached by including the current element in the triplet
    # or by excluding the current element and checking the remaining elements
    return (check(array, n - 1, target - array[n - 1], triplet + [array[n - 1]])
            or check(array, n - 1, target, triplet))


# Call the check function with an empty triplet to start checking all possible subsets of the array
if not check(array, n, target, []):
    print('does not exist')

# this code is contributed by bhardwajji
