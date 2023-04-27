# The main function that returns index
# of row with maximum number of 1s.
def rowWithMax1s(mat) :

    # Initialize max using values from first row.
    max_row_index = 0;
    max = first(mat[0], 0, C - 1)

    # Traverse for each row and count number of 1s
    # by finding the index of first 1
    for i in range(1, R):

        # Count 1s in this row only if this row
        # has more 1s than max so far

        # Count 1s in this row only if this row
        # has more 1s than max so far
        if (max != -1 and mat[i][C - max - 1] == 1):

            # Note the optimization here also
            index = first (mat[i], 0, C - max)

            if (index != -1 and C - index > max):
                max = C - index
                max_row_index = i
        else:
            max = first(mat[i], 0, C - 1)

    return max_row_index;

# This code is contributed by Dharanendra L V
