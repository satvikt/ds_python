"""
Compass interview - 16 June 2021

"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import copy


def solution(H, X, Y):
    # write your code in Python 3.6
    comb_x = []
    comb_y = []
    comb_x = combination(H, X)
    comb_y = combination(H, Y)
    number_cars = 0

    if len(comb_y) == 0 and len(comb_x) != 0:
        number_cars += len(comb_x)
        for i in comb_x:
            H.remove(i)
        for j in H:
            Y -= j
            if Y >= 0:
                number_cars += 1
            else:
                break

    elif len(comb_x) == 0 and len(comb_y) != 0:
        number_cars += len(comb_y)
        for i in comb_y:
            H.remove(i)
        for j in H:
            X -= j
            if X >= 0:
                number_cars += 1
            else:
                break

    elif len(comb_x) != 0 and len(comb_y) != 0:
        number_cars += len(comb_x)
        number_cars += len(comb_y)




    else:
        if X >= Y:
            for i in H:
                X -= i
                if X >= 0:
                    number_cars += 1
                    H.remove(i)
                else:
                    break
            for i in H:
                Y -= i
                if Y >= 0:
                    number_cars += 1
                else:
                    break

        else:
            for i in H:
                Y -= i
                if Y >= 0:
                    number_cars += 1
                    H.remove(i)
                else:
                    break
            for i in H:
                X -= i
                if X >= 0:
                    number_cars += 1
                else:
                    break

    return number_cars


def combination(arr, sum):
    arr.sort(reverse=False)
    local = []
    res = combination_rec(0, 0, sum, local, arr, [])
    if res:
        return res
    return []

def combination_rec(length, total, sum, local, arr, final):
    if total == sum:
        sub_final = copy.copy(local)
        final.append(sub_final)
        # return final

    for i in range(length, len(arr), 1):

        if total + arr[i] > sum:
            continue

        if (i > length and arr[i] == arr[i - 1]):
            continue

        local.append(arr[i])

        final = combination_rec(i + 1, total + arr[i], sum, local, arr, final)

        local.remove(local[len(local) - 1])

    return final

if __name__ == "__main__":
    print(combination([6, 5, 5, 4, 3], 8))

    # solution([6, 5, 2, 1, 8], 17, 5)