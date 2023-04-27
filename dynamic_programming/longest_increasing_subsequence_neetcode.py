def LIS_length(seq):
    # cache - initializing the length of longest increasing subsequence at index i as 1
    LIS = [1] * len(seq)

    # starting at last index and moving backward to know the LIS at index i
    for i in range(len(seq) - 1, -1, -1):
        # checking for the jth index, exactly 1 step after i, and getting the max out of
        # only LIS at i, vs (1 + LIS[j])
        # note 1: no need to move more than 1 step forward, that has already been calculated
        # note 2: the max LIS checking only applies of num at i < num at j
        for j in range(i + 1, len(seq)):
            if seq[i] < seq[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)


def main():
    seq = [1, 2, 4, 3]



    length = LIS_length(seq)

    print(f"the LIS is {length}")

"""
Loop i - run 1: seq[3] = 3. since this is teh final element, LIS[3] = 1
Loop i - run 2: seq[2] -> max(1, 1 + LIS[3]). since seq[2] > seq[3], this doesn't work

https://youtu.be/cjWnW0hdF1Y?t=660
 
"""

if __name__ == "__main__":
    main()
