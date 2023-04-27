from collections import Counter


def permuteUnique(lis):
    output = []
    def dfs(comb, counter):
        if len(comb) == len(lis):
            output.append(list(comb))
            return

        for num in counter:
            if counter[num] > 0:
                comb.append(num)
                counter[num] -= 1

                dfs(comb, counter)

                comb.pop()
                counter[num] +=1

    dfs([], Counter(lis))
    return output



if __name__ == "__main__":
    print(permuteUnique("AAC"))