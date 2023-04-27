def stockBuySell(price, n):
    if n <2:
        return
    i = 0
    arr = []
    while i < n:
        while(i<n-1) and price[i+1] <= price[i]:
            i += 1

        if i == n-1:
            break
        buy = i
        i += 1

        # while (i<n) and price[i] > price[i-1]:
        #     i += 1
        # sell = i -1

        while (i<n-1) and price[i+1] > price[i]:
            i += 1
        sell = i



        arr.append((buy, sell))

        print("buy at ", buy+1,"\t", "sell at ", sell+1)
    return arr







if __name__ == "__main__":
    # Driver code

    # Stock prices on consecutive days
    price = [100, 180, 260, 310, 40, 535, 695]
    n = len(price)

    # Function call
    stockBuySell(price, n)