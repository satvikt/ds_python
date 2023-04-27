def binary(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        modulo = n % 2
        return binary(n // 2) + str(modulo)



if __name__ == "__main__":
    n1 = 10
    n2 = 9

    print(binary(9))