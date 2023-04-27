pages = [12, 34, 67, 90]
m = 2

def func(pages, m):
    # end = len(pages)
    # i = 0
    # arr = []
    # while i < end:
    #     sum1 = sum(pages[0:i])
    #     sum2 = sum(pages[i:end])
    #
    #     arr.append([sum1, sum2])
    #     i += 1
    #
    # total = min(map(max, arr))
    # print(total)
    #

    div = len(pages)//m
    arr2 = [0]*m

    for i in range(0, m):
        arr2[i] = pages[i:i+div]

    total = min(arr2)
    print(arr2)



    

    return total

if __name__ == "__main__":
    print(func(pages, 4))