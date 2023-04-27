def maxProfit(prices):

    n = len(prices)
    cost = 0
    maxcost = 0

    if (n == 0):
        return 0

    # Store the first element of
    # array in a variable
    min_price = prices[0]

    for i in range(n):

        # Now compare first element with all
        # the element of array and find the
        # minimum element
        min_price = min(min_price, prices[i])

        # Since min_price is smallest element
        # of the array so subtract with every
        # element of the array and return the
        # maxCost
        cost = prices[i] - min_price

        maxcost = max(maxcost, cost)

    return maxcost

# Driver Code
prices = [ 7, 1, 5, 3, 6, 4 ]

# Stock prices on consecutive days
print(maxProfit(prices))

# This code is contributed by avanitrachhadiya2155
