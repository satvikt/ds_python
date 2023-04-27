def mod(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError
    if dividend < divisor:
        return dividend
    else:
        return mod(dividend - divisor, divisor)


if __name__ == "__main__":
    dividend = 54
    divisor = 11
    print(mod(dividend, divisor))