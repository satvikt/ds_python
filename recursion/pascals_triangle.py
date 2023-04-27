def pascals_triangle(n):
    return pascals_rec(n, n)

def pascals_rec(n, k):
    if n == 0:
        base = [1]
        print(base)
        # print(" " * ((k - n)*2 - 2) + str(base))
        return base

    else:
        line = [1]

        previous_line = pascals_rec(n - 1, k)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        print(str(line))
        # print(" " * ((k - n)*2 - 2) + str(line))
    return line


if __name__ == "__main__":
    n = int(input("Number of rows of pascal's triangle: "))
    pascals_triangle(n)