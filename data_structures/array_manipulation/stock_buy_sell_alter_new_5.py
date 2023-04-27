def stockBuySell(price, n):
    if n == 1:
        return

    # for i in range(n):
    #     if price[i] <
    i = 0
    while i < n-1:
        # buy = 0
        # find local minima
        while i < n-1 and price[i+1] <= price[i]:
            i += 1

        if i==n-1:
            break

        buy = i

        while i < n-1 and price[i+1] >= price[i]:
            i += 1

        sell = i

        print("Buy at ", buy+1, "sell at ", sell+1)

if __name__ == "__main__":
    # Driver code

    # Stock prices on consecutive days
    price = [100, 180, 260, 310, 40, 535, 695]
    n = len(price)

    # Function call
    stockBuySell(list(reversed(pnrice)), n)