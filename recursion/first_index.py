def search(arr, targetNumber, currentIndex):
    if len(arr) == 0:
        return
    if arr[currentIndex] == targetNumber:
        return currentIndex
    return search(arr, targetNumber, currentIndex+1)




if __name__ == "__main__":
    arr = [9, 8, 1, 8, 1, 7]
    targetNumber = 1
    currentIndex = 0

    print(search(arr, targetNumber, currentIndex))