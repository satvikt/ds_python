def TowerOfHanoi(n, source, dest, helper, count):
    count += 1
    if n == 1:
        print("Moving plate " + str(n) + " from " + source + " to " + dest)
        return

    TowerOfHanoi(n-1, source, helper, dest, count)
    print("Moving plate " + str(n) + " from " + source + " to " + dest)
    TowerOfHanoi(n-1, helper, dest, source, count)

if __name__ == '__main__':
    n = 4
    count = 0
    TowerOfHanoi(n, 'A', 'C', 'B', count)