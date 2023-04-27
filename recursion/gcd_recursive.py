def gcd(n1, n2):
    if n1 == n2:
        return n1

    if n1 > n2:
        return gcd(n1 - n2,n2)
    else:
        return gcd(n1 - n2, n1)


if __name__ == "__main__":
    n1 = 10
    n2 = 9

    gcd(n1, n2)