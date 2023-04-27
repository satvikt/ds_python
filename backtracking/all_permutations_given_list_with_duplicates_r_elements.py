from collections import Counter


def permuteUnique(arr, r):
    results = []
    def backtrack(comb, counter):
        if len(comb) == r:
            results.append(list(comb))
            return

        for i in counter:
            if counter[i] > 0:
                comb.append(i)
                counter[i] -= 1

                backtrack(comb, counter)

                comb.pop()
                counter[i] += 1

    backtrack(comb=[], counter=Counter(arr))

    return results



if __name__ == "__main__":
    r = 2
    # print(permuteUnique([1,1,2], r))
    #
    # print(permuteUnique([1,1,2, 4],r ))
    #
    print(permuteUnique([1,3,2], 3))


    # print(permuteUnique([1,3,2, 4], 3))
