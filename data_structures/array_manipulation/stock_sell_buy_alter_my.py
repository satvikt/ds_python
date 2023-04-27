prices = [ 7, 1, 5, 3, 6, 4 ]

# Stock prices on consecutive days
def maxProfit(prices):
    min_price = prices[0]
    cost = 0
    max_cost = 0
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        cost = prices[i] - min_price
        max_cost = max(cost, max_cost)

    return max_cost



print(maxProfit(prices))
