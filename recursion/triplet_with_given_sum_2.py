array = [1, 4, 45, 6, 10, 8]
target = 22
n = len(array)


def check(array, n, target, triplet):
    if target == 0 and len(triplet) == 3:
        print(triplet)
        return True
    if n == 0 or target < 0 or len(triplet) == 3:
        return False

    return (check(array, n-1, target-array[n-1], triplet+[array[n-1]])
            or check(array, n-1, target, triplet))

# val = check(array, n, target, [])

if not check(array, n, target, []):
    print('does not exist')