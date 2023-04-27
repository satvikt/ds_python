def max_profit(arr):
    min_ele = arr[0]
    cost = 0
    max_cost = 0
    output = []

    for i in range(1, len(arr)):
        min_ele = min(min_ele, arr[i])
        cost = arr[i] - min_ele
        if cost > 0:
            min_ele = 0
            output.append(cost)
        # max_cost = max(max_cost, cost)
    return sum(output)

prices = [ 7, 1, 5, 3, 6, 4 ]
print(max_profit(prices))