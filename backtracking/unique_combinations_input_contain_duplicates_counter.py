from typing import List


def combinationSum2( candidates: List[int], target: int) -> List[List[int]]:

    def backtrack(comb, remain, start, results):

        if remain == 0:
            # make a deep copy of the resulted combination
            results.append(list(comb))
            return

        for i in range(start, len(candidates)):

            if i > start \
                    and candidates[i] == candidates[i - 1]:
                continue

            pick = candidates[i]
            # optimization: skip the rest of elements starting from 'curr' index
            if remain - pick < 0:
                break

            comb.append(pick)
            backtrack(comb, remain - pick, i + 1, results)
            comb.pop()

    candidates.sort()

    comb, results = [], []
    backtrack(comb, target, 0, results)

    return results

if __name__ == "__main__":
    arr = [1,1, 3]
    sum = 4
    print(combinationSum2(arr, sum))