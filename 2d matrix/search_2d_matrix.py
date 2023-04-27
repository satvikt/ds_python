def searchMatrix(matrix, target):
    if matrix == None or len(matrix) < 1 or len(matrix[0]) < 1:
        return False
    col = len(matrix[0]) - 1
    row = 0

    while col > 0 and row < len(matrix)-1:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1

    return False


if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5

    searchMatrix(matrix, target)