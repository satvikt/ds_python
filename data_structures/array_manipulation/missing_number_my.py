def get_missing_number(arr, n):
    # n = len(arr)
    rem = n % 4
    if rem == 0:
        xor_all = n
    elif rem == 1:
        xor_all = 1
    elif rem == 2:
        xor_all = n+1
    else: # rem == 3
        xor_all = 0

    for ele in arr:
        xor_given = xor_all ^ ele
    return xor_given

def xor_given(arr, n):
    xor = 1
    for i in range(2,n+1):
        xor = xor^i
    print(xor)

    xor_one = arr[0]
    for i in range(1,n-1):
        xor_one = xor_one^arr[i]
    print(xor_one)
    return xor_one^xor



def get_missing_number2(arr, n):

    total = 1
    length = len(arr)
    for i in range(2, length + 2):
        total += i
        total -= arr[i-2]
    return total

if __name__ == "__main__":
    arr = [5,2,3,4,1]
    n = 6
    # print(get_missing_number(arr, 5))
    # print(get_missing_number2(arr, 5))
    print(xor_given(arr,n))
