def min_cost_path(matrix, point):
    x, y = point
    if not matrix or not matrix[x-1][y-1]:
        return

    row = len(matrix)
    col = len(matrix[0])

    min_cost = [[0]*col for i in range(row)]

    # Filling leftmost 0th col
    for i in range(1, row):
        min_cost[i][0] = min_cost[i-1][0] + matrix[i][0]

    # Filling topmost 0th row
    for j in range(1, col):
        min_cost[0][j] = min_cost[0][j-1] + matrix[0][j]

    for i in range(row):
        for j in range(col):
            # min cost to reach [i,j] is
            # cost of having reached 1 cell to left [i-1,j] OR cost having reached 1 cell above [i,j-1]  -> min of these 2
            # plus cost of jumping to [i,j]

            min_cost[i][j] = min(min_cost[i-1][j], min_cost[i][j-1]) + matrix[i][j]

    return min_cost[x][y]

if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24]]
    point = (2,3)
    print(min_cost_path(matrix, point))