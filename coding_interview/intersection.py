"""Write a function that takes in 3 lists of integers and returns the intersection of them

[1], [2], [3] => []
[1], [1,2], [1,2,3] => [1]
[1,3], [1,3], [1,2,3] => [1,3]

Company - Ground Truth
Date - 28 June

"""
#
# Brute force
#
# # max_len = max(len(l1), len(l2), len(l3))
#
# for  in l1:
#     If i in l2 and i in l3:
#     continue
# else:
#     Break;
#
# d1 = {}
# D2= {}
#
# Output = []
#
# for i in l1:
#     If i in D1:
#     D1[i] += 1
# Else:
# D1[i] = 1	 #d1 1,3
# For j in l2:
# If j in D1:
# Val = j + 1
# D2[j] = D1[j] #d2 1
#
#
# For k in l3:
# If k in D2:
# output.append(k)
#
#
# [1,1,3], [1,3], [1,1,2,3] - > [1,3]
#
# D1 = {1:2, 3:1}
# D2 = {1:1, 3:0}
# D3 = {1:-1, 3:-1}
#
# {1:-2}


def intersection(lst):
    d1 = dict()
    d2 = dict()
    d3 = dict()
    for item in lst[0]:
        if item not in d1:
            d1[item] = 1
        else:
            d1[item] += 1
        # else:
        #     d1[item] += 1
        # {1:2,3:1}
    # print(lst[0])
    print(d1)
    for item in lst[1]:
        if item not in d2:
            # continue
            d2[item] = 1
        else:
            d2[item] += 1
    # print(lst[1])
    print(d2)

    for item in lst[2]:
        if item not in d3:
            d3[item] = 1
        else:
            d3[item] += 1
    # print(lst[2])
    # print(d3)

    print(max(d1,d2,d3, key=len))

    d4 = {}
    # for i in range(len(d1)):
    output = []
    for i in lst[0]:
        try:
            # if d1[i] > 0 and d2[i] > 0 and d3[i] > 0:
            #     output.append(i)

            d4[i] = min(d1[i], d2[i], d3[i])

        except KeyError:
            continue

    # return output
    for key, value in d4.items():
        i = 0
        while i < value:
            output.append(key)
            i += 1
    return output

    # for i in len

    # return list(d3.keys())



if __name__ == "__main__":
    l1 = [[1], [2], [3]]
    l2 = [[1], [1,2], [1,2,3]]
    l3 = [[1,1,3], [1,3], [1,2,3]]
    l4 = [[1,1,3], [1,2,3], [1,1,1,2,3]]

    # print(intersection(l1))
    # print(intersection(l2))
    print(intersection(l4))

    max_list = max(l4, key=len)
    max_len = max(map(len, l4))
    # print(max_list)
    # print(max_len)