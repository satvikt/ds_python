def square_sorted_arr(arr):
    output = [0]*len(arr)
    neg_ind = 0
    pos_ind = len(arr) - 1
    op_ind = len(arr) - 1
    while (neg_ind <= pos_ind):
        if arr[neg_ind]**2 < arr[pos_ind]**2:
            output[op_ind] = arr[pos_ind]**2
            pos_ind -= 1
        else:
            output[op_ind] = arr[neg_ind]**2
            neg_ind += 1
        op_ind -= 1

    return output

if __name__ == '__main__':
    A = [-2, -1, 0, 2, 3]

    print(square_sorted_arr(A))
    # print(make_squares(A))